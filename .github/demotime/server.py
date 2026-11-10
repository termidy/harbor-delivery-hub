"""DemoTime MCP server (course sandbox).

DemoTime is DemoConsult's time-tracking and resourcing tool in the Harbor story.
This small server gives an agent DemoTime's tools over MCP (stdio, JSON-RPC 2.0).
It uses only the Python standard library and reads its data from workload.json
next to this file. Changes made by log_time and set_planned_hours are kept in
memory only: they last until the server stops at the end of the run.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "workload.json"), encoding="utf-8") as f:
    DATA = json.load(f)
PEOPLE = {p["id"]: p for p in DATA["people"]}
WEEKS = DATA["weeks"]
VERSIONS = ["2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05"]

WEEK = {"type": "integer", "minimum": 1, "maximum": WEEKS}
PERSON = {"type": "string", "description": "Person id from list_people, for example migration-lead."}

TOOLS = [
    {"name": "list_people",
     "description": "List the Harbor team in DemoTime: id, name, role and weekly capacity in hours.",
     "inputSchema": {"type": "object", "properties": {}},
     "annotations": {"readOnlyHint": True}},
    {"name": "get_workload",
     "description": "Planned hours against capacity for every person on Harbor, for one project week "
                    "or a range of weeks. Shows free hours and who is planned over capacity.",
     "inputSchema": {"type": "object", "required": ["from_week"],
                     "properties": {"from_week": WEEK,
                                    "to_week": dict(WEEK, description="Last week of the range. Default: from_week.")}},
     "annotations": {"readOnlyHint": True}},
    {"name": "get_timesheet",
     "description": "Hours a person booked in one project week, by task.",
     "inputSchema": {"type": "object", "required": ["person", "week"],
                     "properties": {"person": PERSON, "week": WEEK}},
     "annotations": {"readOnlyHint": True}},
    {"name": "log_time",
     "description": "Book hours for a person in one project week, with the task.",
     "inputSchema": {"type": "object", "required": ["person", "week", "hours", "task"],
                     "properties": {"person": PERSON, "week": WEEK,
                                    "hours": {"type": "number", "minimum": 0.5, "maximum": 60},
                                    "task": {"type": "string"}}},
     "annotations": {"readOnlyHint": False, "destructiveHint": False}},
    {"name": "set_planned_hours",
     "description": "Change a person's planned hours for one project week.",
     "inputSchema": {"type": "object", "required": ["person", "week", "hours"],
                     "properties": {"person": PERSON, "week": WEEK,
                                    "hours": {"type": "number", "minimum": 0, "maximum": 60}}},
     "annotations": {"readOnlyHint": False, "destructiveHint": True}},
]


def log(msg):
    print("demotime: " + msg, file=sys.stderr, flush=True)


def person(pid):
    if pid not in PEOPLE:
        raise ValueError("Unknown person '%s'. Call list_people for the ids." % pid)
    return PEOPLE[pid]


def week(w):
    if not isinstance(w, int) or not 1 <= w <= WEEKS:
        raise ValueError("Week must be a project week from 1 to %d." % WEEKS)
    return w


def list_people(_):
    lines = ["Harbor team in DemoTime (%d people). Capacity is hours a week." % len(PEOPLE)]
    for p in DATA["people"]:
        lines.append("- %s: %s, %s, capacity %g h" % (p["id"], p["name"], p["role"], p["capacity"]))
    return "\n".join(lines)


def get_workload(args):
    first = week(args.get("from_week"))
    last = week(args.get("to_week", first))
    if last < first:
        raise ValueError("to_week must not be before from_week.")
    lines = ["Harbor workload in DemoTime, Week %d to Week %d: planned hours / capacity." % (first, last)]
    over = []
    for w in range(first, last + 1):
        lines.append("Week %d" % w)
        for p in DATA["people"]:
            planned, cap = p["planned"][w - 1], p["capacity"]
            free = cap - planned
            note = "%g h free" % free if free > 0 else ("no free hours" if free == 0 else "%g h over capacity" % -free)
            lines.append("- %s: %g / %g h, %s" % (p["name"], planned, cap, note))
            if free < 0:
                over.append("Week %d: %s, %g h planned, capacity %g h" % (w, p["name"], planned, cap))
    lines.append("Planned over capacity: " + ("; ".join(over) if over else "nobody") + ".")
    return "\n".join(lines)


def get_timesheet(args):
    p, w = person(args.get("person")), week(args.get("week"))
    rows = [t for t in DATA["timesheets"] if t["person"] == p["id"] and t["week"] == w]
    if not rows:
        return "%s booked no hours in Week %d." % (p["name"], w)
    lines = ["%s, Week %d, booked hours:" % (p["name"], w)]
    lines += ["- %g h: %s" % (t["hours"], t["task"]) for t in rows]
    lines.append("Total: %g h" % sum(t["hours"] for t in rows))
    return "\n".join(lines)


def log_time(args):
    p, w = person(args.get("person")), week(args.get("week"))
    hours, task = float(args.get("hours", 0)), str(args.get("task", "")).strip()
    if hours <= 0 or not task:
        raise ValueError("Give the hours and the task.")
    DATA["timesheets"].append({"person": p["id"], "week": w, "hours": hours, "task": task})
    return "Booked %g h for %s in Week %d: %s." % (hours, p["name"], w, task)


def set_planned_hours(args):
    p, w = person(args.get("person")), week(args.get("week"))
    hours = float(args.get("hours", -1))
    if hours < 0:
        raise ValueError("Give the planned hours.")
    old = p["planned"][w - 1]
    p["planned"][w - 1] = hours
    return "Planned hours of %s in Week %d changed from %g h to %g h." % (p["name"], w, old, hours)


HANDLERS = {"list_people": list_people, "get_workload": get_workload, "get_timesheet": get_timesheet,
            "log_time": log_time, "set_planned_hours": set_planned_hours}


def handle(msg):
    method, params = msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        asked = params.get("protocolVersion")
        return {"protocolVersion": asked if asked in VERSIONS else VERSIONS[1],
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "demotime", "version": "1.0.0"},
                "instructions": "DemoTime: the Harbor team's planned hours, capacity and timesheets."}
    if method == "ping":
        return {}
    if method == "tools/list":
        return {"tools": TOOLS}
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        log("call %s %s" % (name, json.dumps(args, sort_keys=True)))
        if name not in HANDLERS:
            raise LookupError("Unknown tool: %s" % name)
        try:
            return {"content": [{"type": "text", "text": HANDLERS[name](args)}], "isError": False}
        except ValueError as e:
            return {"content": [{"type": "text", "text": str(e)}], "isError": True}
    raise LookupError("Method not found: %s" % method)


def main():
    log("started, %d people, %d tools" % (len(PEOPLE), len(TOOLS)))
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            print(json.dumps({"jsonrpc": "2.0", "id": None,
                              "error": {"code": -32700, "message": "Parse error"}}), flush=True)
            continue
        if "id" not in msg:
            continue  # a notification, such as notifications/initialized
        try:
            reply = {"jsonrpc": "2.0", "id": msg["id"], "result": handle(msg)}
        except LookupError as e:
            reply = {"jsonrpc": "2.0", "id": msg["id"], "error": {"code": -32601, "message": str(e)}}
        print(json.dumps(reply), flush=True)


if __name__ == "__main__":
    main()

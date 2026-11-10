# DemoTime MCP server

DemoTime is DemoConsult's time-tracking and resourcing tool. This folder holds a small MCP server for it, so that an
agent can read the Harbor team's workload, which GitHub does not have. In the course it stands in for the server that
DemoConsult runs: the data is invented, and nothing here connects to a real system.

## Tools

| Tool | What it does | Reads or writes |
|---|---|---|
| `list_people` | The Harbor team: id, name, role and weekly capacity in hours | Reads |
| `get_workload` | Planned hours against capacity for every person, for one project week or a range of weeks | Reads |
| `get_timesheet` | Hours a person booked in one project week, by task | Reads |
| `log_time` | Books hours for a person in one project week | Writes |
| `set_planned_hours` | Changes a person's planned hours for one project week | Writes |

Allow only the tools a job needs. The weekly status report needs `get_workload`.

## Files

- `server.py`: the server. Python standard library only; it talks MCP over standard input and output.
- `workload.json`: the data. Ten DemoConsult people on Harbor, planned hours and capacity for Week 1 to Week 12, and the
  timesheets of Week 1 and Week 2.

The writing tools change a copy in memory: the change lasts until the server stops at the end of the run.

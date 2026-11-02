"""Course helper for the Harbor Delivery Hub (run by .github/workflows/harbor-setup.yml, never by hand).

Creates what "Use this template" does not copy: labels, milestones M1-M4 with due dates relative to today, and the
issues of the project in a fixed order (so that every copy has the same issue numbers). With a later "start", it also
adds the files each earlier section produced (.github/harbor-setup/sections/sN/) as one commit per section, and
the issues of the later weeks (sections/sN.issues.json).
Safe to run twice: existing labels, milestones and files are kept; issues are created only in a copy that has none.
"""
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ["REPO"]
TOKEN = os.environ["GH_TOKEN"]
START = os.environ.get("START", "Course start (Week 2)")

# the section the learner starts at, and the project week it is then (milestone dates count back from today)
SECTIONS = {"Course start": (2, 2), "Start of section 3": (3, 2), "Start of section 4": (4, 4),
            "Start of section 5": (5, 5), "Start of section 6": (6, 7)}
section, week_now = next(v for k, v in SECTIONS.items() if START.startswith(k))


def api(method, path, body=None):
    req = urllib.request.Request(f"https://api.github.com{path}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as r:
                text = r.read().decode()
                return json.loads(text) if text else None
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and attempt < 4:   # secondary rate limit on creating many issues: wait and retry
                time.sleep(20 * (attempt + 1))
                continue
            if e.code >= 500 and attempt < 4 and method == "GET":
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError(f"{method} {path}: {e.code} {e.read().decode()[:300]}")


def load(name):
    with open(os.path.join(HERE, name), encoding="utf-8") as f:
        return json.load(f)


def labels():
    have = {l["name"] for l in api("GET", f"/repos/{REPO}/labels?per_page=100")}
    for l in load("labels.json"):
        if l["name"] not in have:
            api("POST", f"/repos/{REPO}/labels", l)
    print(f"labels: {len(load('labels.json'))} in the copy")


def milestones():
    monday = dt.date.today() - dt.timedelta(days=dt.date.today().weekday())
    week1 = monday - dt.timedelta(weeks=week_now - 1)
    have = {m["title"]: m["number"] for m in api("GET", f"/repos/{REPO}/milestones?state=all&per_page=100")}
    numbers = {}
    for m in load("milestones.json"):
        friday = week1 + dt.timedelta(weeks=m["week"] - 1, days=4)
        if m["title"] in have:
            numbers[m["title"]] = have[m["title"]]
            continue
        made = api("POST", f"/repos/{REPO}/milestones", {"title": m["title"], "description": m["description"],
                                                         "due_on": f"{friday.isoformat()}T17:00:00Z"})
        numbers[m["title"]] = made["number"]
    print(f"milestones: Week 1 starts {week1.isoformat()}, project week now {week_now}")
    return numbers


def all_issues():
    out, page = [], 1
    while True:
        part = api("GET", f"/repos/{REPO}/issues?state=all&per_page=100&page={page}&sort=created&direction=asc")
        out += [x for x in part if "pull_request" not in x]
        if len(part) < 100:
            return sorted(out, key=lambda x: x["number"])
        page += 1


def create_issue(body):
    """POST an issue; a 5xx may still have created it, so look before trying again (a second copy would shift every number)"""
    for attempt in range(4):
        try:
            return api("POST", f"/repos/{REPO}/issues", body)
        except RuntimeError as e:
            if ": 5" not in str(e) or attempt == 3:
                raise
            time.sleep(8 * (attempt + 1))
            last = all_issues()
            if last and last[-1]["title"] == body["title"]:
                return last[-1]


def issues(numbers, items, first=1):
    for i, it in enumerate(items, 1):
        if i < first:
            continue
        body = {"title": it["title"], "body": it["body"], "labels": it.get("labels", [])}
        if it.get("milestone"):
            body["milestone"] = numbers[it["milestone"]]
        made = create_issue(body)
        if made["number"] != i:   # an empty copy: the position in the list is the issue number
            print(f"WARNING issue {it['title']!r} got #{made['number']}, expected #{i}")
        if it.get("state") == "closed":
            api("PATCH", f"/repos/{REPO}/issues/{made['number']}", {"state": "closed", "state_reason": it.get("state_reason", "completed")})
        time.sleep(1.2)   # GitHub limits how fast content is created
    print(f"issues: {len(items)} created")


def section_files():
    """files of every section before the chosen one, one commit per section (sections/s3 = what section 3 ends with)"""
    root = os.path.dirname(os.path.dirname(HERE))
    git = lambda *a: subprocess.run(["git", *a], cwd=root, check=True)
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    added = 0
    for s in range(2, section):
        src = os.path.join(HERE, "sections", f"s{s}")
        if not os.path.isdir(src):
            continue
        shutil.copytree(src, root, dirs_exist_ok=True)
        git("add", "-A")
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=root).returncode != 0:
            git("commit", "-q", "-m", f"Harbor: what section {s} produced")
            added += 1
    if added:
        git("push", "-q")
    print(f"section files: {added} commit(s)")


def main():
    labels()
    numbers = milestones()
    items = load("issues.json")
    for s in range(3, section + 1):   # issues that appear in later weeks of the story
        extra = os.path.join(HERE, "sections", f"s{s}.issues.json")   # outside the copied folder sections/sN
        if os.path.exists(extra):
            with open(extra, encoding="utf-8") as f:
                items += json.load(f)
    have = all_issues()
    # a copy with our first issues (an earlier run that stopped, or an earlier section): go on from there; a copy with
    # other issues: create none, the numbers the course uses would not match
    if [x["title"] for x in have] == [x["title"] for x in items[:len(have)]] and [x["number"] for x in have] == list(range(1, len(have) + 1)):
        if len(have) < len(items):
            issues(numbers, items, first=len(have) + 1)
        else:
            print("issues: all there already")
    else:
        print("issues: the copy has other issues, none created (the course's issue numbers would not match)")
    section_files()
    print(f"Harbor is ready at: {START}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # one clear line in the Actions log
        print(f"Set up Harbor failed: {e}")
        sys.exit(1)

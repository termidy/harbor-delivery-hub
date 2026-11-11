# Harbor Delivery Hub

The working documents of Harbor, the project that DemoConsult runs for DemoFoods. DemoFoods, a wholesale food distributor, is moving its orders, inventory, invoicing and payments to a new ERP, DemoERP, in 12 weeks.

There is no code here. The Hub holds requirements, meeting notes, the RAID log and the status reports. The work is planned on the Harbor Delivery board. All names and data are invented.

The project is now at the end of Week 2.

## Folder map

| Folder | What is in it |
|---|---|
| `requirements/` | Requirements for orders, payments, inventory and invoicing, and the status report standard (`report-spec.md`) |
| `meetings/` | Meeting notes: the kickoff, the design workshop and the weekly client sync |
| `raid/` | The RAID log: risks, assumptions, issues and decisions |
| `reports/` | The status report template and the Friday status reports |
| `.github/ISSUE_TEMPLATE/` | The client request form |
| `.github/harbor-setup/` | Data for the "Set up Harbor" workflow: labels, milestones, issues, and the files each section adds |
| `.github/demotime/` | The DemoTime MCP server: the team's planned hours, which GitHub does not have |

## Getting started

1. **Make your own copies.** Click **Use this template** > **Create a new repository**. Make two copies: a **public** copy for the GitHub platform section, and a **private** copy for the rest of the course.
2. **Fill your copy with the project data.** In your copy, open **Actions** > **Set up Harbor** > **Run workflow**. It creates the labels, the milestones M1 to M4, the Week 1 backlog and the client requests. To catch up with the course, choose the **start of section** you need (see **Catching up** below).
3. **Build the board.** Create the Harbor Delivery board as the course shows you.

## Catching up

Set up Harbor can also bring your private copy to the start of a later section. Choose that section in **Run workflow**. The helper sets the milestone dates for that week of the project and adds the files the earlier sections made, one commit per section:

| You choose | Project week | Files added |
|---|---|---|
| Course start (Week 2) | 2 | None |
| Start of section 3 (Copilot) | 2 | None: section 2 works in the public copy, on the board and the wiki |
| Start of section 4 (Design) | 4 | `prompt-library.md` and the Market Scout agent, `.github/agents/market-scout.agent.md` |
| Start of section 5 (Build) | 5 | The same: section 4 designs and adds no files |
| Start of section 6 (Human in the loop) | 7 | The same, and the two skills in `.github/skills/`: `harbor-report-style` and `meeting-minutes` |

A file your copy already has is kept as it is.

Some things are not files, or the helper cannot add them. Make them as the lessons show:

- The Harbor Delivery board (section 2), from the issues of your public copy.
- The Discussions category Status reports (the setup lesson).
- The Weekly Status Report workflow and its two secrets (section 5). GitHub does not let a workflow add workflow files, and the report needs your own account name and your own board.
- The Client Request Intake automation (section 5). It is a setting on the Agents tab, not a file.

# Status report standard

| | |
|---|---|
| Owner | Owen Clarke, Head of Delivery (PMO), DemoConsult |
| Status | Approved |
| Version | 2.0 |
| Applies to | Every DemoConsult project. For Harbor, agreed with Laura Chen at the kickoff (D-002, D-003). |
| Template | `reports/template.md` |

## Purpose

The client gets one honest status report every Friday. Every project uses the same sections and the same RAG rules, so a reader can compare projects and trust the colour.

## When and who

- The status report covers one project week and is ready every Friday.
- The delivery manager writes it, or checks the draft when someone else prepares it.
- **The delivery manager approves the report before it reaches the client.** Nothing goes to the client without this approval.
- The approved report goes to the client sponsor (for Harbor: Laura Chen).

## Sections

Use the sections of `reports/template.md` in this order. Do not add or remove sections.

1. **Summary.** The RAG status and at most three sentences: what changed this week and what matters next.
2. **Milestones.** Every milestone with its planned date, its forecast date and the slip in days.
3. **Done this week.** The main finished work, with issue and pull request numbers.
4. **Next week.** The main planned work.
5. **Top risks and issues.** At most five, from the RAID log, with their IDs (R-014, I-009), owner and due week.
6. **Decisions this week.** New decisions from the RAID log, with their IDs (D-021).
7. **Client requests.** New, open and closed client requests, with issue numbers.
8. **What we need from DemoFoods.** Each need with an owner and a due week.

## RAG rules

The RAG status is set by these rules only. Nobody chooses a colour by feeling.

| RAG | Rule |
|---|---|
| Green | No milestone has slipped. |
| Amber | A milestone has slipped by 1-3 days, or a high risk has no owner. |
| Red | A milestone has slipped by more than 3 days. |

- A Red status also triggers an escalation to Owen Clarke, Head of Delivery, in the same week.
- A high risk is a risk with High impact and Medium or High probability (see `raid/raid-log.md`).
- When more than one rule applies, the worst colour wins.

## Accuracy

- Every date and every number in the report must match the board (the Harbor Delivery board). If the report and the board differ, the board is right and the report is fixed before approval.
- Every risk, issue and decision is quoted with its RAID ID. Do not invent new IDs in the report.
- Every issue and pull request is quoted with its number (#12).
- No guesses. If something is not known, write "not known yet" and add it to "What we need from DemoFoods".

## Style

- One page.
- Plain, short sentences. The reader may not be a native English speaker.
- Facts first, no sales language. Bad news is written as clearly as good news.
- Project weeks ("Week 7"), not vague words like "soon" or "shortly".

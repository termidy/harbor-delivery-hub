# Harbor kickoff

Week: Week 1
Type: project kickoff
Notes by: Delivery manager

## Attendees

DemoFoods:
- Laura Chen, Finance Operations Director (sponsor)
- IT lead
- Order desk lead
- Warehouse manager
- Two members of the Finance team (added after the meeting, see I-003)

DemoConsult:
- Delivery manager
- Aisha Rahman, business analyst
- Tom Becker, solution architect
- Owen Clarke, Head of Delivery (PMO), first 30 minutes
- Data migration lead, test lead, training lead

## Agenda

1. Goals and scope of Harbor
2. Plan and milestones
3. Ways of working: the Hub, the board, client requests
4. Status report and RAG rules
5. Data migration scope
6. First risks
7. Next steps

## Notes

1. **Goals and scope.** DemoFoods moves orders, inventory, invoicing and payments from the old order system to DemoERP. Laura: the go-live date matters most. "No surprises with the date. If it moves, I want to hear it early."
2. **Plan.** 12 weeks, team of 15. Four milestones agreed (D-001). Six 2-week sprints (D-006).
3. **Ways of working.** All documents in the Harbor Delivery Hub (D-004). Tom: signed documents change only through a pull request that he reviews. Client requests come through the form in the Hub (D-005). Laura reads the Hub but does not edit it. Weekly client sync (D-007). Aisha owns the requirements, Tom reviews (D-008).
4. **Status report.** Owen presented the PMO standard (`requirements/report-spec.md`). One page, every Friday (D-002). RAG by the PMO rules (D-003). Laura: "I want the honest colour, not a green one."
5. **Data migration.** Scope agreed (D-009). Finance does not need invoice history older than two years (A-004). Data moves once, at go-live, no parallel run (A-003). DemoFoods IT will deliver the extracts (A-005).
6. **First risks.** Customer master data quality (R-002). Bank file format (R-004). Workshop availability in the busy season (R-001). Sign-off by Week 3 (R-007).
7. **Partial payments.** Laura: some large customers pay one invoice in two or three parts. The old system cannot do this, and Finance matches these payments by hand. She asked if DemoERP can do it. Aisha: not in the payments draft yet. Agreed to log it as a change request.

## Decisions

| ID | Decision |
|---|---|
| D-001 | Harbor runs for 12 weeks with four milestones: M1 Week 3, M2 Week 7, M3 Week 10, M4 Week 12. |
| D-002 | The status report goes to DemoFoods every Friday on the PMO template. |
| D-003 | The RAG status follows the PMO rules in `requirements/report-spec.md`. |
| D-004 | All Harbor documents live in the Harbor Delivery Hub. A signed document changes only through a reviewed pull request. |
| D-005 | DemoFoods files client requests through the client request form in the Hub. |
| D-006 | The team works in six 2-week sprints. Sprint 1 starts in Week 1. |
| D-007 | A client sync with Laura Chen takes place every week. |
| D-008 | Aisha Rahman owns all requirements documents. Tom Becker reviews them before sign-off. |
| D-009 | Migration scope: customers, products, open orders, open invoices and two years of paid invoices. |

## Actions

| Action | Owner | Due |
|---|---|---|
| Log the partial payments request as a change request (#12) | Delivery manager | Week 1 |
| Set up the RAID log in `raid/raid-log.md` | Delivery manager | Week 1 |
| Plan the design workshop for order entry and payments | Aisha Rahman | Week 1 |
| Name the key users for the design workshop | Laura Chen | Week 2 |
| Ask the bank to confirm the payment file format | Laura Chen | Week 2 |
| Send the first draft of the payments requirements | Aisha Rahman | Week 2 |

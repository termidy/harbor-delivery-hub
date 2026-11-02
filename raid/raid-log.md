# Harbor RAID log

Owner: Delivery manager
Last updated: end of Week 2
Updated: every Friday, before the status report

How to read this log:
- Probability and impact: Low, Medium or High.
- A risk is **high** when its impact is High and its probability is Medium or High.
- Every high risk needs a named owner. A high risk without an owner makes the status report Amber (see `requirements/report-spec.md`).
- Status: Open or Closed. Closed entries stay in the log.

## Risks

| ID | Risk | Probability | Impact | Owner | Status | Due week |
|---|---|---|---|---|---|---|
| R-001 | DemoFoods key users are not free for design workshops in the busy season. | Medium | High | Laura Chen | Closed | Week 2 |
| R-002 | Customer master data has duplicates and old delivery addresses. Bad data moves to DemoERP. | High | High | Data migration lead | Open | Week 5 |
| R-003 | Change requests before M1 grow the scope and delay the sign-off. | Medium | Medium | Delivery manager | Open | Week 3 |
| R-004 | The bank has not confirmed the payment file format for DemoERP. | Medium | High | Tom Becker | Open | Week 4 |
| R-005 | Warehouse scanners may not work with DemoERP. | Low | High | Tom Becker | Open | Week 6 |
| R-006 | Order desk staff change before training. New staff miss the training. | Low | Medium | Training lead | Open | Week 9 |
| R-007 | Requirements sign-off for all four areas slips past Week 3 (M1). | Medium | High | Aisha Rahman | Open | Week 3 |
| R-008 | The old order system licence ends soon after go-live. There is little room to move M4. | Low | High | Laura Chen | Open | Week 12 |
| R-009 | The partial payments change (#12) changes the payments design after sign-off. | Medium | Medium | Tom Becker | Open | Week 3 |
| R-010 | DemoFoods has not named the key users for user acceptance testing. | Medium | Medium | Delivery manager | Open | Week 4 |
| R-011 | Two departments keep their own price lists. The migrated prices may not match. | Medium | Medium | Aisha Rahman | Open | Week 4 |
| R-012 | Real customer bank details end up in test data or in documents. | Low | High | Tom Becker | Open | Week 6 |
| R-013 | Delivery routes are kept in a spreadsheet, not in a system. Route data may be out of date. | Medium | Low | Aisha Rahman | Open | Week 5 |
| R-014 | The test extract from the old order system may not be ready for the M2 rehearsal. DemoFoods IT has not named who runs the extract. | High | High | | Open | Week 5 |

## Assumptions

| ID | Assumption | Owner | Status | Check by |
|---|---|---|---|---|
| A-001 | DemoFoods gives key users two days a week during user acceptance testing (Weeks 8-10). | Laura Chen | Open | Week 4 |
| A-002 | Standard DemoERP functions cover payments. No custom development is needed. | Tom Becker | Open | Week 3 |
| A-003 | Data moves to DemoERP once, at go-live. There is no parallel run of the two systems. | Tom Becker | Confirmed | Week 1 |
| A-004 | Finance does not need invoice history older than two years in DemoERP. | Aisha Rahman | Confirmed | Week 1 |
| A-005 | DemoFoods IT delivers all data extracts from the old order system. | Laura Chen | Open | Week 3 |
| A-006 | The old order system stays available, read only, for three months after go-live. | Laura Chen | Open | Week 6 |

## Issues

| ID | Issue | Priority | Owner | Status | Due week |
|---|---|---|---|---|---|
| I-001 | The DemoERP test environment is not ready. Design checks wait for it. | High | Tom Becker | Open | Week 3 |
| I-002 | Two versions of the price list are in use. Nobody knows which one is current. | Medium | Aisha Rahman | Open | Week 3 |
| I-003 | The kickoff notes missed two Finance attendees. | Low | Delivery manager | Closed | Week 1 |
| I-004 | The order desk lead is on leave in Week 3. Order stories need her review. | Medium | Delivery manager | Open | Week 3 |
| I-005 | The customer master data export breaks names with accents. | Medium | Data migration lead | Open | Week 4 |
| I-006 | The bank has not replied about the payment file format (see R-004). | High | Laura Chen | Open | Week 3 |
| I-007 | The design workshop ran over time. The payments session was cut short. | Low | Aisha Rahman | Closed | Week 2 |
| I-008 | The credit limit rule is not clear: block the order or only flag it. The workshop gave two answers. | High | Aisha Rahman | Open | Week 3 |
| I-009 | The DemoConsult team has no access to reports in the old order system. | Medium | Laura Chen | Open | Week 3 |

## Decisions

| ID | Decision | Made by | Where | Week |
|---|---|---|---|---|
| D-001 | Harbor runs for 12 weeks with four milestones: M1 Week 3, M2 Week 7, M3 Week 10, M4 Week 12. | Laura Chen, Delivery manager | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-002 | The status report goes to DemoFoods every Friday on the PMO template. | Owen Clarke, Laura Chen | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-003 | The RAG status follows the PMO rules in `requirements/report-spec.md`. | Owen Clarke | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-004 | All Harbor documents live in the Harbor Delivery Hub. A signed document changes only through a reviewed pull request. | Tom Becker | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-005 | DemoFoods files client requests through the client request form in the Hub. | Laura Chen, Delivery manager | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-006 | The team works in six 2-week sprints. Sprint 1 starts in Week 1. | Delivery manager | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-007 | A client sync with Laura Chen takes place every week. | Laura Chen, Delivery manager | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-008 | Aisha Rahman owns all requirements documents. Tom Becker reviews them before sign-off. | Delivery manager | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-009 | Migration scope: customers, products, open orders, open invoices and two years of paid invoices. | Laura Chen, Tom Becker | [Kickoff](../meetings/week-01-kickoff.md) | Week 1 |
| D-010 | Only the order desk enters orders in DemoERP. Customers do not enter orders themselves in this project. | Order desk lead, Aisha Rahman | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-011 | The cut-off for next-day delivery stays at 2 pm. | Order desk lead | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-012 | When a product is out of stock, the order desk offers a substitute. The customer must agree before it goes on the order. | Order desk lead | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-013 | The minimum order value stays as today. DemoERP checks it at order entry. | Order desk lead, Credit control lead | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-014 | Payments v1.0 does not include partial payments. The request (#12) is handled as a change request after sign-off. | Aisha Rahman, Tom Becker | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-015 | A customer payment is matched to an invoice by the invoice number in the bank reference. | Credit control lead, Tom Becker | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-016 | Laura Chen decides the credit limit rule (block or flag) in Week 3 (see I-008). | Aisha Rahman | [Design workshop](../meetings/week-02-design-workshop.md) | Week 2 |
| D-017 | Payments requirements v1.0 are signed off by Laura Chen and Tom Becker. | Laura Chen, Tom Becker | [Client sync](../meetings/week-02-client-sync.md) | Week 2 |
| D-018 | The inventory requirements review moves into Week 3. It stays inside M1. | Laura Chen, Aisha Rahman | [Client sync](../meetings/week-02-client-sync.md) | Week 2 |
| D-019 | No real customer bank details go into test data or into any document in the Hub. | Laura Chen, Tom Becker | [Client sync](../meetings/week-02-client-sync.md) | Week 2 |
| D-020 | The M2 rehearsal uses a full extract of the old order system, not a sample. | Tom Becker | [Client sync](../meetings/week-02-client-sync.md) | Week 2 |
| D-021 | M2 stays in Week 7 for now. It is reviewed at the Week 3 sync, after DemoFoods names an owner for the extract (R-014). | Laura Chen, Delivery manager | [Client sync](../meetings/week-02-client-sync.md) | Week 2 |

# Weekly client sync

Week: Week 2
Type: weekly client sync
Notes by: Delivery manager

## Attendees

- Laura Chen, Finance Operations Director, DemoFoods
- DemoFoods IT lead
- DemoFoods finance systems analyst
- Delivery manager, DemoConsult
- Aisha Rahman, business analyst, DemoConsult
- Tom Becker, solution architect, DemoConsult

## Agenda

1. Progress since Week 1
2. Payments requirements: sign-off
3. Inventory and invoicing requirements
4. M2 data migration rehearsal
5. Client requests
6. Any other business

## Notes

1. **Progress.** Week 1 report was Green. Design workshop held this week. Payments session was cut short (I-007), a follow-up call closed the gaps. Order entry stories start next week (#23).
2. **Payments sign-off.** Laura and Tom signed off payments v1.0 (D-017). Laura asked again about partial payments. Delivery manager: it is #12, a change request after sign-off (D-014). Tom will bring the impact check in Week 3. Laura: "Fine, but it must be in before testing starts."
3. **Inventory and invoicing.** Inventory review moves into Week 3 (D-018). Still inside M1, but there is no spare time now (R-007). Invoicing draft: Finance has comments on payment terms. Aisha will update the draft.
4. **M2 rehearsal.** Tom: the rehearsal needs a full extract of the old order system, not a sample (D-020). DemoFoods IT lead: the extract needs a person who knows the old database, and that person is busy with year-end work. Nobody is named yet. This is a new high risk with no owner (R-014). If the extract is late, M2 in Week 7 is at risk. Agreed to keep Week 7 for now and review at the Week 3 sync (D-021).
5. **Client requests.** New requests came in through the form this week. Some have no urgency or no date. Delivery manager will go through them and ask for the missing details. Laura asked her team to check for open requests before they file a new one.
6. **Test data.** Laura: real customer bank details must never be in test data or in the Hub (D-019). Tom agreed. Linked to R-012.
7. **Any other business.** Laura asked how other food distributors handled their ERP migrations: what went wrong, how long the rehearsal took, how they trained warehouse staff. She would like a short summary of general practice, with sources. Delivery manager to prepare it.

## Decisions

| ID | Decision |
|---|---|
| D-017 | Payments requirements v1.0 are signed off by Laura Chen and Tom Becker. |
| D-018 | The inventory requirements review moves into Week 3. It stays inside M1. |
| D-019 | No real customer bank details go into test data or into any document in the Hub. |
| D-020 | The M2 rehearsal uses a full extract of the old order system, not a sample. |
| D-021 | M2 stays in Week 7 for now. It is reviewed at the Week 3 sync, after DemoFoods names an owner for the extract (R-014). |

## Actions

| Action | Owner | Due |
|---|---|---|
| Name an owner at DemoFoods IT for the old order system extract (R-014) | Laura Chen | Week 3 |
| Impact check for partial payments (#12) | Tom Becker | Week 3 |
| Update the invoicing draft with Finance comments on payment terms | Aisha Rahman | Week 3 |
| Review client requests and ask for missing details | Delivery manager | Week 3 |
| Summary of how other food distributors ran ERP migrations, with sources | Delivery manager | Week 4 |
| Name the key users for user acceptance testing (R-010) | Laura Chen | Week 4 |

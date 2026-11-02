# Design workshop: order entry and payments

Week: Week 2
Type: design workshop (half day)
Facilitator: Aisha Rahman
Notes by: Aisha Rahman (raw notes, cleaned up a little)

## Attendees

DemoFoods:
- Order desk lead
- Two order desk team members
- Credit control lead (joined at 10:30)
- Warehouse supervisor (order entry part only)
- Finance systems analyst

DemoConsult:
- Aisha Rahman, business analyst
- Tom Becker, solution architect
- Delivery manager (first hour)

## Agenda

1. How orders come in today
2. Order entry in DemoERP: what the order desk needs
3. Stock, substitutes and delivery dates
4. Credit checks
5. Payments: bank file, matching, partial payments
6. Open points and next steps

## Notes

### 1. How orders come in today

- Phone about 60%, email about 30%, sales reps about 10% (order desk lead's estimate, not measured).
- Peak is 7-10 am. "Everybody calls at once."
- Most customers order the same things every week. Order desk keeps their own list of "usual orders" in a spreadsheet (!) -> this should be in DemoERP.
- Email orders: retyped by hand. Typos in product codes happen a lot. Wrong code = wrong product delivered.

### 2. Order entry: what the order desk needs

- Find the customer fast: by name, by account code, or by phone number. Team member: "Phone number is fastest when they call."
- Repeat last order: copy the last order (or the "usual order") and then change quantities. Big time saver for them.
- Product search by code or by name. Show unit (case / pallet) next to the product. See also inventory requirements, INV-03.
- Show the delivery date options for the customer's route. Each route has fixed delivery days (spreadsheet today, see R-013).
- Cut-off for next-day delivery: 2 pm. After 2 pm the order goes to the next delivery day for that route. Agreed to keep 2 pm (D-011).
- Minimum order value: keep as today (D-013). Warn the user at order entry, not at the end. Order desk lead can still accept a small order "for a good customer" - needs a reason.
- Order confirmation to the customer: they want it. Email from DemoERP? Tom: standard function, check. Nice to have, not must have (Aisha to confirm with Laura).
- Customers ordering online themselves: not now (D-010). Maybe a later phase.

### 3. Stock, substitutes, delivery dates

- Show available stock while entering the line. Not just "in stock", the real number.
- Out of stock: order desk offers a substitute (same product, other brand or pack size). Customer must say yes on the phone first (D-012). Today there is no list of substitutes, they know it by heart.
- Warehouse supervisor: if a substitute is used, it must show on the picking list, otherwise the warehouse picks the wrong thing.
- Best-before dates: the warehouse picks the oldest first. Not an order entry topic, parked for inventory.

### 4. Credit checks

- Today credit checks happen after the order is entered, sometimes after delivery. Too late.
- Order desk wants to see the customer's available credit when they open the order (limit minus open invoices).
- Order desk lead: **"Orders over the credit limit must be blocked. No exceptions. That is the rule from Finance."**
- (10:30, credit control lead joined)
- Credit control lead, later in the session: **"We never block an order. We flag it, and sales can release it. If we block, we lose the customer."**
- -> These two statements conflict. Not resolved in the room. Logged as I-008. Laura to decide (D-016).
- Who can release a flagged order, if we flag? Sales manager? Credit control? Not agreed.

### 5. Payments (session cut short, see I-007)

- Bank file comes once a day. Payments matched to invoices by the invoice number in the bank reference (D-015).
- When the reference is missing or wrong -> list of unmatched payments for credit control to check by hand. Today this list is a spreadsheet too.
- Overpayment: keep as customer credit. Use it on the next invoice.
- Partial payments: credit control raised it again ("three of our biggest customers do it every month"). Same request as Laura at kickoff (#12). Tom: changes the payment matching design, needs impact check. Agreed: payments v1.0 goes to sign-off without it, and #12 is handled as a change request after sign-off (D-014).
- Credit notes: approved by credit control lead before they reduce an invoice. Already in the draft (PAY-07).

### 6. Open points

- Can an order be changed after the 2 pm cut-off? Order desk says yes "if the truck is not loaded". Warehouse supervisor says no, picking starts at 3 pm. **Open question**, Aisha to follow up with both.
- Who releases a flagged order (if Laura chooses "flag")?
- Order confirmation email: must have or nice to have?
- Where does the route and delivery day data come from at go-live? (R-013)

## Decisions

| ID | Decision |
|---|---|
| D-010 | Only the order desk enters orders in DemoERP. Customers do not enter orders themselves in this project. |
| D-011 | The cut-off for next-day delivery stays at 2 pm. |
| D-012 | When a product is out of stock, the order desk offers a substitute. The customer must agree before it goes on the order. |
| D-013 | The minimum order value stays as today. DemoERP checks it at order entry. |
| D-014 | Payments v1.0 does not include partial payments. The request (#12) is handled as a change request after sign-off. |
| D-015 | A customer payment is matched to an invoice by the invoice number in the bank reference. |
| D-016 | Laura Chen decides the credit limit rule (block or flag) in Week 3 (see I-008). |

## Actions

| Action | Owner | Due |
|---|---|---|
| Write user stories with acceptance criteria for order entry from these notes (#23) | Aisha Rahman | Week 3 |
| Ask Laura Chen to decide the credit limit rule (I-008) | Aisha Rahman | Week 3 |
| Follow up on changes after cut-off with the order desk and the warehouse | Aisha Rahman | Week 3 |
| Check that DemoERP can send order confirmations by email | Tom Becker | Week 3 |
| Impact check for partial payments (#12) | Tom Becker | Week 3 |
| Send the list of substitute products in use today | Order desk lead | Week 3 |

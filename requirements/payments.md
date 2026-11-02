# Payments requirements

| | |
|---|---|
| Owner | Aisha Rahman |
| Status | Signed off |
| Version | 1.0 |
| Reviewers | Tom Becker, DemoFoods credit control lead |
| Signed off | Week 2, by Laura Chen (DemoFoods) and Tom Becker (DemoConsult), D-017 |

This document is signed off. Changes go through a pull request reviewed by Tom Becker (D-004).

## Scope

How DemoFoods receives customer payments in DemoERP and matches them to invoices. It covers the daily bank file, matching, unmatched payments, overpayments, direct debits and credit notes.

Out of scope for this version:
- Payments to suppliers.
- Partial payments on an invoice. Handled as a change request after sign-off (#12, D-014).

## Requirements

| ID | Requirement |
|---|---|
| PAY-01 | DemoERP imports the bank file with customer payments once a day. |
| PAY-02 | DemoERP matches each payment to an invoice by the invoice number in the bank reference (D-015). |
| PAY-03 | A payment with a missing or unknown invoice number goes to a list of unmatched payments. The credit control team checks this list every day. |
| PAY-04 | A payment is applied to an invoice only when it covers the full open amount of that invoice. Partial payments on an invoice are not allowed. |
| PAY-05 | When a customer pays more than the open amount, the difference is kept as customer credit and used on the next invoice. |
| PAY-06 | DemoERP creates direct debit collections for customers with a direct debit agreement. |
| PAY-07 | A credit note reduces an open invoice only after the credit control lead approves it. |
| PAY-08 | The order desk can see the payment status of each invoice: open, paid or overdue. |

## Open questions

None. All questions were closed before sign-off.

## Change history

| Version | Week | Change | By |
|---|---|---|---|
| 0.1 | Week 1 | First draft | Aisha Rahman |
| 0.2 | Week 2 | Matching rule and unmatched payments added after the design workshop | Aisha Rahman |
| 1.0 | Week 2 | Signed off | Laura Chen, Tom Becker |

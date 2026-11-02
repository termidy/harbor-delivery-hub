# Invoicing requirements

| | |
|---|---|
| Owner | Aisha Rahman |
| Status | Draft |
| Version | 0.4 |
| Reviewers | Tom Becker, DemoFoods finance systems analyst |

Finance comments on payment terms are expected in Week 3 (`meetings/week-02-client-sync.md`).

## Scope

How DemoERP creates invoices and credit notes for DemoFoods customers, and how invoices reach the customer. Payments against invoices are in `requirements/payments.md`.

## Requirements

| ID | Requirement |
|---|---|
| BIL-01 | DemoERP creates the invoice when the delivery is confirmed. |
| BIL-02 | Invoice numbers continue the numbering of the old order system. |
| BIL-03 | Payment terms are 30 days for all customers. |
| BIL-04 | Tax is calculated for each invoice line. |
| BIL-05 | Customers with a weekly invoice agreement get one invoice for all deliveries of the week. |
| BIL-06 | Invoices are sent to the customer as PDF files. |
| BIL-07 | A credit note always refers to the invoice it corrects. |

## Open questions

1. Do some customers need a monthly statement of all open invoices?
2. Is the invoice history of two years enough for Finance reports (A-004)?
3. Which customers have a weekly invoice agreement today? List needed from Finance.

## Change history

| Version | Week | Change | By |
|---|---|---|---|
| 0.1 | Week 1 | First draft | Aisha Rahman |
| 0.4 | Week 2 | Weekly invoices and credit notes added | Aisha Rahman |

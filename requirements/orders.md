# Orders requirements

| | |
|---|---|
| Owner | Aisha Rahman |
| Status | Draft |
| Version | 0.3 |
| Reviewers | Tom Becker, DemoFoods order desk lead |

This draft is updated with the results of the design workshop in Week 2 (`meetings/week-02-design-workshop.md`). User stories for order entry follow in #23.

## Scope

How the DemoFoods order desk takes customer orders in DemoERP: finding the customer, entering order lines, stock and substitutes, delivery dates, minimum order value and credit checks. Only the order desk enters orders (D-010).

## Requirements

| ID | Requirement |
|---|---|
| ORD-01 | The order desk can find a customer by name, account code or phone number. |
| ORD-02 | The order desk can copy a customer's last order and change it before saving. |
| ORD-03 | The order desk can find a product by code or by name. The unit (case or pallet) shows next to the product. |
| ORD-04 | DemoERP shows the available stock for each order line while the line is entered. |
| ORD-05 | When a product is out of stock, the order desk can add a substitute product, but only after the customer agrees (D-012). |
| ORD-06 | DemoERP offers only the delivery days of the customer's route. Orders after 2 pm go to the next delivery day (D-011). |
| ORD-07 | DemoERP warns at order entry when the order is below the minimum order value (D-013). |
| ORD-08 | DemoERP shows the customer's available credit (credit limit minus open invoices) when the order is opened. |

## Open questions

1. What happens when an order is over the credit limit: block it or flag it? Laura Chen decides in Week 3 (I-008, D-016).
2. If orders are flagged, who can release them?
3. Can an order be changed after the 2 pm cut-off?
4. Is the order confirmation to the customer a must have or a nice to have?

## Change history

| Version | Week | Change | By |
|---|---|---|---|
| 0.1 | Week 1 | First draft | Aisha Rahman |
| 0.2 | Week 1 | Delivery days and cut-off added | Aisha Rahman |
| 0.3 | Week 2 | Workshop results: copy last order, substitutes, available credit | Aisha Rahman |

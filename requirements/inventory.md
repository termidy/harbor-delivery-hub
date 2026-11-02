# Inventory requirements

| | |
|---|---|
| Owner | Aisha Rahman |
| Status | In review |
| Version | 0.9 |
| Reviewers | Tom Becker, DemoFoods warehouse manager |

The review moved into Week 3 (D-018).

## Scope

How DemoFoods keeps stock in DemoERP: stock by location, units, best-before dates, picking, stock reservations and stock counts. Warehouse scanners are covered by the interface list, not by this document.

## Requirements

| ID | Requirement |
|---|---|
| INV-01 | DemoERP keeps stock by warehouse and by location in the warehouse. |
| INV-02 | Every stock item has a lot number and a best-before date. |
| INV-03 | Each product has one sales unit: case or pallet. |
| INV-04 | The picking list shows the oldest best-before date first, so the warehouse picks it first. |
| INV-05 | Stock is reserved when an order line is saved, and released when the line is cancelled. |
| INV-06 | The warehouse can run a stock count for one location without stopping work in other locations. |
| INV-07 | A substitute product used on an order shows on the picking list (D-012). |

## Open questions

1. Do product codes stay the same in DemoERP? Customers order by code.
2. Some customers buy the same product by the case and by the pallet. Is one sales unit per product enough (INV-03)?
3. Stock that is past its best-before date: blocked automatically or checked by a person?

## Change history

| Version | Week | Change | By |
|---|---|---|---|
| 0.5 | Week 1 | First draft | Aisha Rahman |
| 0.9 | Week 2 | Substitutes on the picking list added | Aisha Rahman |

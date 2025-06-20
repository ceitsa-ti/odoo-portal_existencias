# odoo-portal_existencias

This Odoo 17 module allows portal users to view stock availability without consuming internal licenses. It adds a "Stock" link on the website that lists the on-hand quantity for each sellable product.

### Installation

Zip **only** the contents of the `portal_existencias` directory (do not include this repository's root). The zip should contain the module folder itself:

```
portal_existencias/
    __init__.py
    __manifest__.py
    controllers/
    security/
    views/
```

### Usage

Portal users will see a **Stock** link in the main website navigation. The page lists all sellable products with their current quantity on hand.


Odoo 17 module that displays product stock availability to portal users without consuming internal licenses. It also
adds a website menu entry that lists the stock on hand for each sellable product.
main

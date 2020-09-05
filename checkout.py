from product import BaseProduct


class ProductDoesntExist(Exception):
    """That product doesn't exist"""


class Checkout:

    def __init__(self, pricing_rules=None):
        """
        Items keeps a track of the items in the cart.
        """
        self.items = []
        self.skus = set()
        self.pricing_rules = pricing_rules

    def scan(self, sku):
        """"""
        product = BaseProduct.get_catalog_product(sku)
        if not product:
            raise ProductDoesntExist
        self.skus.add(sku)
        self.items.append(
            CheckoutItem(sku=sku, price=product.price)
        )
        return product

    def total(self):
        """Get the total cost for the cart"""

        # Copy the items because pricing rules can modify the items
        items = self.items
        for sku in self.skus:
            items = self.pricing_rules.apply_rule(sku, items)

        cost = sum([item.price for item in items])
        return cost


class CheckoutItem:

    def __init__(self, price, sku):
        self.price = price
        self.sku = sku

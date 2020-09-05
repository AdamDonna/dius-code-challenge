import collections
from product import MacbookPro, SuperIpad, AppleTV, VGAadapter
from checkout import CheckoutItem


class PricingRules:

    def apply_rule(self, sku, items):
        mapping = {
            MacbookPro.sku: self.free_item_discount,
            SuperIpad.sku: self.bulk_discount_price,
            AppleTV.sku: self.discount_pricing_rule,
        }
        rule = mapping.get(sku, lambda items: items)
        return rule(items)

    def discount_pricing_rule(self, items):
        """
        Eg:// Buy 3 pay for the price of 2
        """
        return items

    def bulk_discount_price(self, items):
        """
        Eg:// price drops when there are more than x in the cart
        Specifically implemented for the scenario where a user buys more than 4 Superipads and gets a discount
        """
        occurrences = collections.Counter(item.sku for item in items)
        # If we add the ability to remove items this will need to be updated
        if occurrences.get(SuperIpad.sku, 0) > 4:
            for item in items:
                if item.sku == SuperIpad.sku:
                    item.price = 499.99

        return items

    def free_item_discount(self, items):
        """
        Get a free item when a different item is purchased
        Specifically implemented for the macbook pro getting a free VGA adapter
        """
        for item in items:
            if item.sku == MacbookPro.sku:
                items.append(CheckoutItem(sku=VGAadapter.sku, price=0))
        return items

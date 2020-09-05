import collections
from product import MacbookPro, SuperIpad, AppleTV, VGAadapter
from checkout import CheckoutItem


class PricingRules:

    def apply_rule(self, sku, items):
        """
        For ever sku we can map them to their rule.
        In an ideal world we can make each of these functions return a function so the conditions are configurable
        """
        mapping = {
            MacbookPro.sku: self.free_item_discount,
            SuperIpad.sku: self.bulk_discount_price,
            AppleTV.sku: self.discount_pricing_rule,
        }
        # When no rules need to be applied then return the unmodified list
        rule = mapping.get(sku, lambda items: items)
        return rule(items)

    def discount_pricing_rule(self, items):
        """
        Eg:// Buy 3 pay for the price of 2
        Specifically implemented for a user buying 3 but paying for 2 apple tvs
        # TODO: Make this work for mutliples of 3
        """
        occurrences = collections.Counter(item.sku for item in items)
        # If we add the ability to remove items this will need to be updated to revert pricing
        if occurrences.get(AppleTV.sku, 0) >= 3:
            for item in items:
                if item.sku == AppleTV.sku:
                    item.price = 0
                    break

        return items

    def bulk_discount_price(self, items):
        """
        Eg:// price drops when there are more than x in the cart
        Specifically implemented for the scenario where a user buys more than 4 Superipads and gets a discount
        """
        occurrences = collections.Counter(item.sku for item in items)
        # If we add the ability to remove items this will need to be updated to revert pricing
        if occurrences.get(SuperIpad.sku, 0) > 4:
            for item in items:
                if item.sku == SuperIpad.sku:
                    item.price = 499.99

        return items

    def free_item_discount(self, items):
        """
        Get a free item when a different item is purchased
        Specifically implemented for the macbook pro getting a free VGA adapter
        1) already has item -> Make it free
        2) doesnt have item -> Add and make it free
        """
        new_items = []
        occurrences = collections.Counter(item.sku for item in items)
        if occurrences.get(MacbookPro.sku, 0) > 0:
            for item in items:
                if item.sku == VGAadapter.sku and item.price != 0:
                    item.price = 0
                else:
                    new_items.append(CheckoutItem(sku=VGAadapter.sku, price=0))
        items.extend(new_items)
        return items

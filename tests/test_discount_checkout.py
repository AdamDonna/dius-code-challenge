import unittest
from checkout import Checkout
from pricing_rules import PricingRules


class CheckoutDiscountTestCase(unittest.TestCase):
    """High level test suite to make sure the output is functionally correct and implements the expected interface"""

    @classmethod
    def setUpClass(cls):
        cls.price_rules = PricingRules()

    def create_checkout(self, sku_list):
        """Helper method to create a checkout populated with skus"""
        checkout = Checkout(self.price_rules)
        for sku in sku_list:
            checkout.scan(sku)
        return checkout

    def test_no_discounts_needed(self):
        """**Scenario** User buys 2 vga adapters, no discounts are expected"""
        checkout = self.create_checkout(['vga', 'vga'])
        total = checkout.total()
        self.assertEqual(total, 60.00)

    def test_price_discount_not_applied(self):
        """**Scenario** User buys 2 apple tvs. They pay for both"""
        checkout = self.create_checkout(['atv', 'atv'])
        total = checkout.total()
        self.assertEqual(total, 219)

    def test_price_discount_is_applied(self):
        """**Scenario** User buys 3 apple tvs. They pay for 2"""
        checkout = self.create_checkout(['atv', 'atv', 'atv'])
        total = checkout.total()
        self.assertEqual(total, 219)

    def test_bulk_discount_not_applied(self):
        """**Scenario** User buys below the bulk discount price threshold"""
        checkout = self.create_checkout(['ipd', 'ipd', 'ipd', 'ipd'])
        total = checkout.total()
        self.assertEqual(total, 2199.96)

    def test_bulk_discount_applied(self):
        """**Scenario** User buys above the bulk discount price threshold"""
        checkout = self.create_checkout(['ipd', 'ipd', 'ipd', 'ipd', 'ipd'])
        total = checkout.total()
        self.assertEqual(total, 2499.95)

    def test_free_product_applied(self):
        """**Scenario** User buys a mac book pro and gets a free vga adapter"""
        checkout = self.create_checkout(['mbp'])
        total = checkout.total()
        self.assertEqual(total, 1399.99)
        item_skus = [item.sku for item in checkout.items]
        # asserts items are equal not just the count. It's a misleading assertion name
        self.assertCountEqual(['mbp', 'vga'], item_skus)

    def test_free_product_applied_for_every_macbook(self):
        """**Scenario** User buys a mac book pro and gets a free vga adapter"""
        checkout = self.create_checkout(['mbp', 'mbp'])
        total = checkout.total()
        self.assertEqual(total, 2799.98)
        item_skus = [item.sku for item in checkout.items]
        # asserts items are equal not just the count. It's a misleading assertion name
        self.assertCountEqual(['mbp', 'vga', 'mbp', 'vga'], item_skus)

    def test_example_scenario_one(self):
        """**Scenario** 3 atv and a vga cable for 249.00"""
        checkout = self.create_checkout(['atv', 'atv', 'atv', 'vga'])
        total = checkout.total()
        self.assertEqual(total, 249.00)

    def test_example_scenario_two(self):
        """**Scenario** atv, ipd, ipd, atv, ipd, ipd, ipd Total expected: $2718.95"""
        checkout = self.create_checkout(['atv', 'ipd', 'ipd', 'atv', 'ipd', 'ipd', 'ipd'])
        total = checkout.total()
        self.assertEqual(total, 2718.95)

    def test_example_scenario_three(self):
        """**Scenario** mbp, vga, ipd Total expected: $1949.98"""
        checkout = self.create_checkout(['mbp', 'vga', 'ipd'])
        total = checkout.total()
        self.assertEqual(total, 1949.98)

    def test_discount_pricing_multiples_of_three(self):
        """**Scenario** User buys 6 apple tvs but only pays for 4"""
        checkout = self.create_checkout(['atv', 'atv', 'atv', 'atv', 'atv', 'atv'])
        total = checkout.total()
        self.assertEqual(total, 438)

    def test_discount_pricing_multiples_of_three_offset(self):
        """**Scenario** User buys 5 apple tvs but only pays for 4"""
        checkout = self.create_checkout(['atv', 'atv', 'atv', 'atv', 'atv'])
        total = checkout.total()
        self.assertEqual(total, 438)

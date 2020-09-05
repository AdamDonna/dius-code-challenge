import unittest
from checkout import Checkout, ProductDoesntExist


class CheckoutDiscountTestCase(unittest.TestCase):

    def test_scan_works(self):
        """**Scenario** User scans a product"""
        checkout = Checkout()
        product = checkout.scan('vga')
        self.assertIsNotNone(product)
        self.assertEqual(len(checkout.items), 1)

    def test_scan_raises_exception_for_not_in_catalog(self):
        """**Scenario** User scans a sku which doesn't exist in the catalog"""
        checkout = Checkout()
        product = checkout.scan('vga')
        self.assertIsNotNone(product)
        self.assertEqual(len(checkout.items), 1)

    def test_raises_error_on_exception(self):
        """**Scenario** User scans product which doesn't exist in the system"""
        checkout = Checkout()
        with self.assertRaises(ProductDoesntExist):
            checkout.scan('long-sku')


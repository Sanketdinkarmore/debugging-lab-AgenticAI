import unittest
from cart import calculate_total

class TestShoppingCart(unittest.TestCase):

    def test_empty_cart(self):
        self.assertEqual(calculate_total([]), 0)

    def test_single_item(self):
        items = [{"price": 10, "quantity": 1}]
        self.assertEqual(calculate_total(items), 10.8)

    def test_multiple_quantities(self):
        items = [
            {"price": 10, "quantity": 2},
            {"price": 5, "quantity": 1}
        ]
        self.assertEqual(calculate_total(items), 27.0)

    def test_discount(self):
        items = [{"price": 100, "quantity": 1}]
        self.assertEqual(
            calculate_total(items, discount_percent=10),
            97.2
        )

if __name__ == "__main__":
    unittest.main()
import unittest

from utils.calculate_points import CalculatePoints


class MockItem:
    def __init__(self, shortDescription, price):
        self.shortDescription = shortDescription
        self.price = price


class MockReceipt:
    def __init__(self, retailer, purchaseDate, purchaseTime, total, items):
        self.retailer = retailer
        self.purchaseDate = purchaseDate
        self.purchaseTime = purchaseTime
        self.total = total
        self.items = items


class TestCalculatePoints(unittest.TestCase):
    """
    Test suite for the calculate_points function.
    """

    def test_points_for_valid_receipt(self):
        """
        Test the calculate_points function with a valid receipt.
        """
        items = [
            MockItem("Mountain Dew 12PK", "6.49"),
            MockItem("Emils Cheese Pizza", "12.25"),
            MockItem("Knorr Creamy Chicken", "1.26"),
            MockItem("Doritos Nacho Cheese", "3.35"),
            MockItem("   Klarbrunn 12-PK 12 FL OZ  ", "12.00")
        ]
        receipt = MockReceipt("Target", "2022-01-01", "13:01", "35.35", items)
        calculator = CalculatePoints(receipt)
        expected_points = 28
        self.assertEqual(calculator.calculate_points(), expected_points)

    def test_points_for_round_total(self):
        """
        Test the calculate_points function for a receipt with a round total.
        """
        items = [
            MockItem("Gatorade", "2.25"),
            MockItem("Gatorade", "2.25"),
            MockItem("Gatorade", "2.25"),
            MockItem("Gatorade", "2.25")
        ]
        receipt = MockReceipt("M&M Corner Market", "2022-03-20", "14:33", "9.00", items)
        calculator = CalculatePoints(receipt)
        expected_points = 109
        self.assertEqual(calculator.calculate_points(), expected_points)

if __name__ == '__main__':
    unittest.main()
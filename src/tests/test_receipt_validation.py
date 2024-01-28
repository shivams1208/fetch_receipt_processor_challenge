import unittest

from utils.receipt_validation import ReceiptValidation


class TestReceiptValidation(unittest.TestCase):
    """
    Test suite for the is_valid_receipt function.
    These tests check the validation of various aspects of a receipt,
    including retailer name, purchase date and time, total amount, and item details.
    """

    def test_valid_receipt(self):
        """
        Test is_valid_receipt with a receipt that meets all validation criteria.
        Ensures that a valid receipt passes all checks.
        """

        valid_receipt = {
            "retailer": "Valid Retailer",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "15:00",
            "total": "100.00",
            "items": [
                {"shortDescription": "Valid Item", "price": "50.00"},
                {"shortDescription": "Another Valid Item", "price": "50.00"}
            ]
        }

        validator = ReceiptValidation(valid_receipt)
        is_valid, _ = validator.is_valid_receipt()
        self.assertTrue(is_valid)


    def test_invalid_retailer_format(self):
        """
        Test is_valid_receipt with an invalid retailer format.
        Ensures that incorrect retailer name formats are caught.
        """

        invalid_receipt = {
            "retailer": " ",  # Invalid characters
            # ... remaining valid fields
        }

        validator = ReceiptValidation(invalid_receipt)
        is_valid, _ = validator.is_valid_receipt()
        self.assertFalse(is_valid)


    def test_invalid_purchase_date_format(self):
        """
        Test is_valid_receipt with an invalid purchase date format.
        Ensures that incorrect date formats are caught.
        """

        invalid_receipt = {
            "retailer": "Valid Retailer",
            "purchaseDate": "01-01-2022",  # Incorrect date format
            # ... remaining valid fields
        }

        validator = ReceiptValidation(invalid_receipt)
        is_valid, _ = validator.is_valid_receipt()
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()

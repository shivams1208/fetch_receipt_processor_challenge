import re
from datetime import datetime

from data_models.process_receipts_dto import ReceiptDataModel
from pydantic import ValidationError


class ReceiptValidation:

    def __init__(self, receipt_data):
        """
        Initializes the ReceiptValidator with receipt data.

        Args:
            receipt_data (dict): Data of the receipt to be validated.
        """
        self.receipt_data = receipt_data


    def is_valid_receipt(self):
        """
        Validates the given receipt data against a set of predefined rules.

        This function checks if the receipt data conforms to the expected format
        and content rules, including the retailer name format, correct date and time formats,
        valid total amount, and proper item descriptions and prices.

        Args:
            receipt_data (dict): The receipt data to validate, expected to be in a format
                                compatible with ReceiptDataModel.

        Returns:
            tuple: A boolean indicating if the receipt is valid, and the validated
                ReceiptDataModel object or an error message.
        """
        try:
            receipt = ReceiptDataModel(**self.receipt_data)
        except ValidationError as e:
            return False, str(e)

        # Validate retailer (non-empty, matching pattern)
        if len((receipt.retailer).strip()) == 0:
            return False, "Invalid retailer format"

        # Validate purchaseDate (correct format)
        try:
            datetime.strptime(receipt.purchaseDate, '%Y-%m-%d')
        except ValueError:
            return False, "Invalid purchaseDate format"

        # Validate purchaseTime (correct format)
        try:
            datetime.strptime(receipt.purchaseTime, '%H:%M')
        except ValueError:
            return False, "Invalid purchaseTime format"

        # Validate total (correct pattern)
        if not re.match(r'^\d+\.\d{2}$', receipt.total):
            return False, "Invalid total format"

        # Validate items
        if not receipt.items or len(receipt.items) == 0:
            return False, "Receipt must have at least one item"

        for item in receipt.items:
            if not re.match(r'^[\w\s\-]+$', item.shortDescription):
                return False, "Invalid item description format"
            if not re.match(r'^\d+\.\d{2}$', item.price):
                return False, "Invalid item price format"

        return True, receipt

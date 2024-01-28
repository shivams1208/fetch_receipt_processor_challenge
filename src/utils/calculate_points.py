import math
from datetime import datetime, time


class CalculatePoints:

    def __init__(self, receipt):
        """
        Initializes the PointsCalculator with a receipt.

        Args:
            receipt: An object representing a receipt, which includes details
                     such as the retailer's name, purchase date and time, items,
                     and the total amount.
        """
        self.receipt = receipt


    def calculate_points(self):
        """
        Calculates and returns the total points for the receipt based on various criteria.

        Returns:
            int: The total points calculated for the receipt.
        """
        points = 0

        # One point for every alphanumeric character in the retailer name
        points += sum(c.isalnum() for c in self.receipt.retailer)

        # 50 points if the total is a round dollar amount with no cents
        total_amount = float(self.receipt.total)
        if total_amount.is_integer():
            points += 50

        # 25 points if the total is a multiple of 0.25
        if total_amount % 0.25 == 0:
            points += 25

        # 5 points for every two items on the receipt
        points += (len(self.receipt.items) // 2) * 5

        # Points based on item description and price
        for item in self.receipt.items:
            if len(item.shortDescription.strip()) % 3 == 0:
                points += math.ceil(float(item.price) * 0.2)

        # 6 points if the day in the purchase date is odd
        day = datetime.strptime(self.receipt.purchaseDate, '%Y-%m-%d').day
        if day % 2 != 0:
            points += 6

        # 10 points if the time of purchase is after 2:00pm and before 4:00pm
        purchase_time = datetime.strptime(self.receipt.purchaseTime, '%H:%M').time()
        if time(14, 0) < purchase_time < time(16, 0):
            points += 10

        return points

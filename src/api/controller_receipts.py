from uuid import uuid4

from data_models.get_points_response_dto import PointsResponseModel
from data_models.process_receipts_dto import (ReceiptDataModel,
                                              ReceiptResponseDataModel)
from flask import jsonify, request
from flask.views import MethodView
from utils.calculate_points import CalculatePoints
from utils.receipt_validation import ReceiptValidation

receipts = {}

class ReceiptAPI(MethodView):
    """
    Flask view handling receipt processing and points retrieval.

    This view supports POST requests for processing receipts and GET requests
    for retrieving points associated with a specific receipt.
    """


    # process_receipt
    def post(self):
        """
        Process a receipt and store it in memory.

        This method validates the receipt data, generates a unique ID for the receipt,
        and stores it. It returns the ID of the processed receipt.

        Returns:
            - JSON response with receipt ID on success (status code 200).
            - Error message on invalid receipt data (status code 400).
        """
        validator = ReceiptValidation(request.json)
        valid, result = validator.is_valid_receipt()

        if not valid:
            return jsonify({"Message": "The receipt is invalid"}), 400

        receipt_dto = result
        receipt_id = str(uuid4())
        receipt_dto.id = receipt_id
        receipts[receipt_id] = receipt_dto.model_dump()

        response_model = ReceiptResponseDataModel(id=receipt_id)
        return jsonify(response_model.model_dump()), 200

    # get_points
    def get(self, receipt_id):
        """
        Retrieve the points associated with a given receipt ID.

        This method calculates the points for the receipt based on predefined rules
        and returns the total points.

        Args:
            receipt_id (str): The unique identifier for the receipt.

        Returns:
            - JSON response with the total points on success (status code 200).
            - Error message if the receipt is not found (status code 404).
        """
        receipt_dict = receipts.get(receipt_id)

        if not receipt_dict:
            return jsonify({"Message": "No receipt found for that id"}), 404

        receipt = ReceiptDataModel(**receipt_dict)
        calculator = CalculatePoints(receipt)
        
        calculated_points = calculator.calculate_points()

        response = PointsResponseModel(points = calculated_points)
        return jsonify(response.model_dump()), 200


import unittest

from api.controller_receipts import ReceiptAPI
from flask import Flask, json


class TestReceiptAPI(unittest.TestCase):
    """
    Test suite for the ReceiptAPI class in the Flask application.
    """

    def setUp(self):
        """
        Set up a Flask test client before each test.
        This method initializes the Flask app and registers different routes
        with unique view function names for testing purposes.
        """

        self.app = Flask(__name__)
        self.app.add_url_rule('/receipts/process', 
                              view_func=ReceiptAPI.as_view('receipt_api_process'), 
                              methods=['POST'])
        self.app.add_url_rule('/receipts/<string:receipt_id>/points', 
                              view_func=ReceiptAPI.as_view('receipt_api_points'), 
                              methods=['GET'])
        self.client = self.app.test_client()


    def test_post_receipt_valid(self):
        """
        Test the POST method of ReceiptAPI with valid receipt data.
        It verifies that the API responds with a 200 status code for valid data.
        """

        valid_receipt_data = {
                                "retailer": "Target",
                                "purchaseDate": "2022-01-02",
                                "purchaseTime": "13:13",
                                "total": "1.25",
                                "items": [
                                        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
                                ]
                            }
        
        response = self.client.post('/receipts/process', json=valid_receipt_data)
        self.assertEqual(response.status_code, 200)


    def test_post_receipt_invalid(self):
        """
        Test the POST method of ReceiptAPI with invalid receipt data.
        It checks that the API responds with a 400 status code for invalid data.
        """

        invalid_receipt_data = {
                                "retailer": "Target",
                                "purchaseDate": "2022-01-02",
                                "purchaseTime": "13:13",
                                "items": [
                                        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
                                ]
                            }
        
        response = self.client.post('/receipts/process', json=invalid_receipt_data)
        self.assertEqual(response.status_code, 400)


    def test_get_points_existing(self):
        """
        Test the GET method of ReceiptAPI for an existing receipt.
        This test first creates a receipt with a POST request and then attempts
        to retrieve points for it with a GET request, verifying a 200 status response.
        """

        receipt_data = {
                        "id": "7fb1377b-b223-49d9-a31a-5a02701dd310",
                        "retailer": "Target",
                        "purchaseDate": "2022-01-02",
                        "purchaseTime": "13:13",
                        "total": "1.25",
                        "items": [
                                    {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
                        ]
                    }
        
        post_response = self.client.post('/receipts/process', json=receipt_data)
        post_data = json.loads(post_response.data)
        receipt_id = post_data.get('id')

        get_response = self.client.get(f'/receipts/{receipt_id}/points')
        self.assertEqual(get_response.status_code, 200)


    def test_get_points_non_existing(self):
        """
        Test the GET method of ReceiptAPI for a non-existing receipt.
        It verifies that the API correctly responds with a 404 status code
        when attempting to retrieve points for a non-existent receipt ID.
        """

        response = self.client.get('/receipts/non_existing_id/points')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

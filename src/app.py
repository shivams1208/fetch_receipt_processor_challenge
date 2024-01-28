from api.controller_receipts import ReceiptAPI
from flask import Flask, jsonify

app = Flask(__name__)

receipt_view = ReceiptAPI.as_view('receipt_api')
app.add_url_rule('/receipts/process', view_func=receipt_view, methods=['POST'])
app.add_url_rule('/receipts/<receipt_id>/points', view_func=receipt_view, methods=['GET'])

@app.errorhandler(400)
def bad_request_error(e):
    return jsonify({"Message" : "The receipt is invalid"}), 400

if __name__ == '__main__':
    app.run()

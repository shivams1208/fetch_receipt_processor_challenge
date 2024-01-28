from typing import List, Optional

from pydantic import BaseModel


class ItemDataModel(BaseModel):
    """
    Pydantic model representing an item in a receipt.

    Attributes:
        shortDescription (str): A brief description of the item.
        price (str): The price of the item, represented as a string.
    """
    shortDescription: str
    price: str


class ReceiptDataModel(BaseModel):
    """
    Pydantic model representing the structure of a receipt.

    Attributes:
        id (Optional[str]): An optional unique identifier for the receipt. Default is None.
        retailer (str): The name of the retailer or store.
        purchaseDate (str): The date of purchase in 'YYYY-MM-DD' format.
        purchaseTime (str): The time of purchase in 'HH:MM' format.
        items (List[ItemDataModel]): A list of items included in the receipt.
        total (str): The total amount of the receipt, represented as a string.
    """
    id: Optional[str] = None
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: List[ItemDataModel]
    total: str


class ReceiptResponseDataModel(BaseModel):
    """
    Pydantic model representing a response containing a receipt ID.

    This model is used in responses where only the receipt ID needs to be conveyed.

    Attributes:
        id (str): The unique identifier of the receipt.
    """
    id: str

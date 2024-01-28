from pydantic import BaseModel


class PointsResponseModel(BaseModel):
    """
    Pydantic model for representing the response structure of points data.

    This model is used to structure the response for requests that retrieve
    the total points associated with a processed receipt. It encapsulates the
    number of points as an integer.

    Attributes:
        points (int): The total number of points calculated for a receipt.
    """
    points: int
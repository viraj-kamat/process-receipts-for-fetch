import points_rules  
from fastapi import FastAPI, HTTPException
import collections
import uvicorn
import uuid

from models.item import Item  
from models.receipt import Receipt

app = FastAPI()

receipts = collections.defaultdict()
receipts_points = collections.defaultdict()

@app.get("/")
def read_root():
    """
    Welcome to the Receipt Processing API!

    This endpoint serves as a simple sanity check for the API and returns a welcome message.

    :return: A JSON object containing the welcome message
    :rtype: dict
    """
    return {"message": "Welcome to the Receipt Processing API!"}


@app.get("/receipts/{id}/points")
def read_item(id: str):
    """
    Returns the points awarded for the receipt with the given id.

    :param id: The ID of the receipt
    :type id: str
    :return: The points awarded for the receipt
    :rtype: int
    :raises HTTPException: If no receipt found for that id
    """
    if id in receipts_points:
        return {"points": receipts_points[id]} 
    else:
        raise HTTPException(status_code=400, detail="No receipt found for that id")



@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    
    """
    Submits a receipt for processing.

    This endpoint takes a receipt object and adds it to the receipts dictionary.
    It then runs the receipt through the points rules and assigns the points to the receipt.
    Finally, it returns the id associated with the receipt.

    :param receipt: The receipt to be processed
    :type receipt: Receipt
    :return: The id associated with the receipt
    :rtype: dict
    """

    id = str(uuid.uuid4())
    receipts[id] = receipt

    points = 0
    points += points_rules.points_for_alphanumeric(receipt.retailer)
    points += points_rules.points_if_whole_number(receipt.total)
    points += points_rules.points_if_multiple_of_pointtwofive(receipt.total)
    points += points_rules.points_based_on_date(receipt.purchaseDate)
    points += points_rules.points_based_on_time(receipt.purchaseTime)
    points += points_rules.points_for_every_two_items(receipt.items)

    for item in receipt.items:
        points += points_rules.points_based_on_name_of_items(item.shortDescription, item.price)

    receipts_points[id] = points

    return {"id": id} 

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
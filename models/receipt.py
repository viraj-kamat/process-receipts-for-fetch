from pydantic import BaseModel
from models.item import Item

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[Item]
    total: float


    def __str__(self):
        return f"{self.retailer} - {self.purchaseDate} - {self.purchaseTime} - {self.total}"
    

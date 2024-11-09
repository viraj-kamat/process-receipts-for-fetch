from pydantic import BaseModel

class Item(BaseModel):
    shortDescription: str
    price: float    

    def __str__(self):
        return f"{self.shortDescription} - ${self.price}"
    

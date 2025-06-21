from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# MongoDB Setup
MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["simple_app"]
collection = db["items"]

# Models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ItemOut(Item):
    id: str

# Helper
def item_helper(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "description": item.get("description"),
        "price": item["price"]
    }

# Routes
@app.post("/items", response_model=ItemOut)
async def create_item(item: Item):
    new_item = await collection.insert_one(item.dict())
    created_item = await collection.find_one({"_id": new_item.inserted_id})
    return item_helper(created_item)

@app.get("/items", response_model=List[ItemOut])
async def get_items():
    items = []
    async for item in collection.find():
        items.append(item_helper(item))
    return items

@app.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: str):
    item = await collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return item_helper(item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=ItemOut)
async def update_item(item_id: str, item: Item):
    updated = await collection.update_one({"_id": ObjectId(item_id)}, {"$set": item.dict()})
    if updated.modified_count:
        updated_item = await collection.find_one({"_id": ObjectId(item_id)})
        return item_helper(updated_item)
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    deleted = await collection.delete_one({"_id": ObjectId(item_id)})
    if deleted.deleted_count:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool


# Base de données en mémoire
items: List[Item] = []


@app.get("/items")
def get_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(item: Item):
    for existing in items:
        if existing.id == item.id:
            raise HTTPException(status_code=400,
                                detail="Item ID already exists")
    items.append(item)
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for i in range(len(items)):
        if items[i].id == item_id:
            items[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for i in range(len(items)):
        if items[i].id == item_id:
            del items[i]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

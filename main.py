from typing import Optional, Dict
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from enum import Enum
from nanoid import generate


app = FastAPI()

class ItemColor(str, Enum):
    red = "red"
    green = "green"
    blue = "blue"

type ItemId = str

class ItemBase(BaseModel):
    name: str=Field(description="상품명")
    color: Optional[ItemColor] = Field(default=None, description="상품색깔")
    # color: ItemColor | None = None

class Item(ItemBase):
    id: ItemId = Field(..., description="상품ID")

id1 = generate(size=10)
id2 = generate(size=10)

temp_items = {
    id1: Item(id=id1, name="아이템A", color=ItemColor.red),
    id2: Item(id=id2, name="아이템B", color=ItemColor.green),
}

def raise_error(code: int, detail: Optional[str] = None):
    raise HTTPException(status_code=code, detail=detail)

def item_or_404(item_id:ItemId):
    if item_id not in temp_items:
        raise HTTPException(status_code=404, detail="아이템이 없습니다")
    return temp_items[item_id]

@app.get("/") # GET /
def root():
    return {"message": "Hello World"}

@app.get("/items", summary="모든아이템 조회")
def read_items() -> Dict[str,dict]:
    return jsonable_encoder(temp_items)

@app.get("/items/{item_id}") # GET /items/{item_id}
def read_item(item_id: ItemId) -> Item:
    item_or_404(item_id)
    return temp_items[item_id]

@app.post("/items", status_code=201, summary="2.1 상품등록 0921") # POST /items
def create_item(item: ItemBase) -> Item:
    item_id = generate(size=10)
    if item_id in temp_items:
        raise_error(400, "아이템이 이미 있어요")
    temp_items[item_id] = Item(id= item_id, **item.model_dump())
    # temp_items[item_id] = Item(id= item_id, name=item.name, color=item.color)
    return temp_items[item_id]

@app.put("/items/{item_id}", status_code=202, summary="2.2 상품수정 0921")
def put_item(item_id: ItemId, item: ItemBase):
    _ = item_or_404(item_id)
    temp_items[item_id] = Item(id = item_id, **item.model_dump())
    return temp_items[item_id]


@app.delete("/items/{item_id}", status_code=204, summary="2.3 상품수정 0921")
def delete_item(item_id: ItemId):
    _ = item_or_404(item_id)
    del temp_items[item_id]
    return {"deleted": True}
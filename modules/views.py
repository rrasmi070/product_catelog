from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import utils, models, schemas
from configs.db import get_db

product_router = APIRouter()

@product_router.post("/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return await utils.create_product(db, product)

@product_router.get("/{product_id}", response_model=schemas.Product)
async def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = await utils.get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@product_router.get("/", response_model=list[schemas.Product])
async def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = await utils.get_products(db, skip=skip, limit=limit)
    return products

@product_router.put("/{product_id}", response_model=schemas.Product)
async def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = await utils.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@product_router.delete("/{product_id}", response_model=schemas.Product)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = await utils.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

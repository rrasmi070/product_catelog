from sqlalchemy.orm import Session
from .models import Product
from .schemas import ProductCreate, ProductUpdate

async def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

async def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

async def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

async def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = await get_product(db, product_id)
    if db_product:
        for key, value in product.dict().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

async def delete_product(db: Session, product_id: int):
    db_product = await get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return db_product

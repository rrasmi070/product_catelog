from fastapi import FastAPI
from modules.views import product_router
from configs.db import Base, engine
app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(product_router, prefix="/products", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product Catalog API!"}

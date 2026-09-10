# from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
# from pydantic import BaseModel
# app=FastAPI()

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query,status
from sqlmodel import Session

from app.schemas import ProductCreate,ProductResponse
from app import  crud
from app.logger import structlog,log
import time

from sqlalchemy import create_engine

from app.metrics import request,errors,duration,active,operation_total,db_duration

from app.database import get_db

engine = create_engine("sqlite://", echo=True)




router = APIRouter(
    prefix="/products",
    tags=["Products"]
)




# class Item(BaseModel):
    
#     name: str | None = None
#     price: int
#     stock: int  










# GET /products
@router.get("/")
def get_all_products(db: Session = Depends(get_db)):
   active.inc()
   start = time.time()

   try:
#    log.info("request received", endpoint="/products", method="GET")
       
#    log.info("request received", endpoint="/products", method="GET")

      log.info("request received", endpoint="/products", method="GET")
      
      db_start = time.time()
    #   time.sleep(3) v  # testiong ke liye likhe teh
   
      result = crud.get_all_products(db)    #yeh db call hua to yaha metrics hai db dureation lagega
      db_duration.observe(time.time() - db_start)

      request.labels(method="GET", endpoint="/products").inc()

      return result

   finally:
      active.dec()
      duration.observe(time.time() - start)
    #   db_duration.observe(time.time() - start)





#get product id
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    #monitor ho rha hai time and requrest ka count dekh rheho n bhai

    active.inc()
    start = time.time()

    try:
        log.info("request received", endpoint="/products/{product_id}", method="GET", product_id=product_id)

        db_start = time.time()
        # time.sleep(3)

        product = crud.get_product(db, product_id)
        db_duration.observe(time.time() - db_start)

        if product is None:
            log.error("product not found", product_id=product_id)

            errors.inc()     #mistaekk hua tha mjaine erros.inc() ko raise http ke ander likha hta but yeh paramerter nhi hai

            raise HTTPException(

                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
           
            )

        request.labels(method="GET", endpoint="/products/{product_id}").inc()

        return product

    finally:
        active.dec()
        duration.observe(time.time() - start)
        # db_duration.observe(time.time() - start)

   




# post/products

# Ye FastAPI ko batata hai ki API response ka format ProductResponse model jaisa hona chahiye.


@router.post("/",response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate,db: Session = Depends(get_db)):

    active.inc()
    start = time.time()

    try:
        log.info("request received", endpoint="/products", method="POST")

        db_start=time.time()

        new_product=crud.create_product(db,product)
        db_duration.observe(time.time() - db_start)

        request.labels(method="POST", endpoint="/products").inc()
        operation_total.labels(operation="create").inc()

        return product
        

    finally:
        active.dec()
        duration.observe(time.time() - start)
        # db_duration.observe(time.time() - start)





# PUT /products/{product_id}
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):

    active.inc()
    start = time.time()

    try:
        log.info("request received", endpoint="/products/{product_id}", method="PUT", product_id=product_id)

        db_start=time.time()
        

        updated_product = crud.update_product(db, product_id, product)
        db_duration.observe(time.time() - db_start)

        if updated_product is None:
            log.error("product not found", product_id=product_id)


            errors.inc()

            raise HTTPException(

                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"

            )

        request.labels(method="PUT", endpoint="/products/{product_id}").inc()
        operation_total.labels(operation="update").inc()

        return updated_product

    finally:
        active.dec()
        duration.observe(time.time() - start)
        # db_duration.observe(time.time() - start)





#delete product id se hi dundhoge obvisouly
@router.delete("/{product_id}",response_model=ProductResponse)
def delete_product(product_id:int,db: Session = Depends(get_db)):
            
            
    active.inc()
    start = time.time()

    try:
        log.info("request received", endpoint="/products/{product_id}", method="DELETE", product_id=product_id)

        db_start = time.time()
            
        deleted_product=crud.delete_product(db,product_id)
        db_duration.observe(time.time() - db_start)

        if deleted_product is None:
            log.error("product not found", product_id=product_id)

            errors.inc()
                 
            raise HTTPException(
                      
                status_code=404,
                detail="Product not found"
            )

        request.labels(method="DELETE", endpoint="/products/{product_id}").inc()
        operation_total.labels(operation="delete").inc()

        return deleted_product

    finally:
        active.dec()
        duration.observe(time.time() - start)
        # db_duration.observe(time.time() - start)



 #try finally use kreneh  hi obviously finaaly humesha execute hoga error aaye ya nhi aaya isilye req deactiveate humesha hogi 
 # # error aaya to bhi req khtm , error nhi aaaya to bhi kaam kr baad req khtm


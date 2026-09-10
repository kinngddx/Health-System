# # app/routers/products.py

# from fastapi import APIRouter, HTTPException, status

# router = APIRouter(
#     prefix="/products",
#     tags=["Products"]
# )

# # Temporary data (baad me PostgreSQL use karenge)
# products = [
#     {
#         "id": 1,
#         "name": "Laptop",
#         "price": 55000,
#         "stock": 10
#     },
#     {
#         "id": 2,
#         "name": "Mouse",
#         "price": 800,
#         "stock": 100
#     }
# ]


# # GET /products
# @router.get("/")
# def get_all_products():
#     return products


# # GET /products/{id}
# @router.get("/{product_id}")
# def get_product(product_id: int):

#     for product in products:
#         if product["id"] == product_id:
#             return product

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Product not found"
#     )


# # POST /products
# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_product(product: dict):

#     product["id"] = len(products) + 1
#     products.append(product)

#     return {
#         "message": "Product created successfully",
#         "product": product
#     }


# # PUT /products/{id}
# @router.put("/{product_id}")
# def update_product(product_id: int, updated_product: dict):

#     for product in products:
#         if product["id"] == product_id:
#             product.update(updated_product)

#             return {
#                 "message": "Product updated successfully",
#                 "product": product
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Product not found"
#     )


# # DELETE /products/{id}
# @router.delete("/{product_id}")
# def delete_product(product_id: int):

#     for index, product in enumerate(products):

#         if product["id"] == product_id:
#             deleted = products.pop(index)

#             return {
#                 "message": "Product deleted successfully",
#                 "product": deleted
#             }

#     raise HTTPException(
#         status_code=404,
#         detail="Product not found"
#     )














from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
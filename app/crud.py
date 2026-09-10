#actual database operations (create, get, update, delete) likhenge

#4 opearions honege to obvisouly tere ko charo operaiton krene ke liye funciton s likne ka j ruruat hai i think brother


from app.database import SessionLocal
from app.models import Product
from app.schemas import ProductCreate,ProductResponse
from sqlalchemy.orm import session,Session
from sqlalchemy import select
from app.routers import products
import time


#PRODUCTS
def create_product(db:session,product:ProductCreate):
    new_product=Product(
        name=product.name,
        price=product.price,
        stock=product.stock


    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product



def get_all_products(db:Session):

    stmt = select(Product)   # product sleection kiya

    result = db.execute(stmt)   # query chalaya sql me

    products = result.scalars().all()   # most impo hia bcz object list me return kiya
    time.sleep(6)
    return products




def get_product(db: Session, product_id: int):
    stmt = select(Product).where(Product.id == product_id)
    result = db.execute(stmt)
    return result.scalar_one_or_none()








def update_product(db: Session, product_id: int, product: ProductCreate):
    existing_product = get_product(db, product_id)

    if existing_product is None:
        return None

    existing_product.name = product.name
    existing_product.price = product.price
    existing_product.stock = product.stock

    db.commit()
    db.refresh(existing_product)

    return existing_product






def delete_product(db: Session, product_id: int):
    existing_product = get_product(db, product_id)

    if existing_product is None:
        return None
    
    db.delete(existing_product)
    db.commit

    return existing_product

    









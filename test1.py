from app.database import engine, Base
from app.models import Product

conn = engine.connect()
print("Database Connected ho gya bc")

Base.metadata.create_all(bind=engine)
conn.close()
# fastapi dev  = running commnad hai
# uvicorn app.main:app --reload    running commnad hai 

# from fastapi import FastAPI
# app=FastAPI()


# @app.get("/")
# async def root():
#     return { "Lets build something fucking things"}



from fastapi import FastAPI
from app.routers import products
from prometheus_fastapi_instrumentator import Instrumentator    # fast api se direct integrate krne me easy hota hai 


from app.database import engine, Base
from app.models import Product

from app.metrics import app_info
from app.tracing import configure_tracing
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from app.routers import postmortem







# conn = engine.connect()
# print("Database Connected ho gya bc")

Base.metadata.create_all(bind=engine)
# conn.close()



app=FastAPI(title="Demo hai banega jldi hi best")


#yaha pr pura opentelemarty kr rhe bhai
configure_tracing()
FastAPIInstrumentor.instrument_app(app)
SQLAlchemyInstrumentor().instrument(engine=engine)

app.include_router(postmortem.router)



# Pass structural configurations inside the Instrumentator() initialization
Instrumentator(
    should_group_status_codes=True,  # Groups 200, 201 into 2xx (Default)
    should_ignore_untemplated=True   # Hides paths that don't match structural routes
).instrument(app).expose(app)



# Instrumentator().instrument(app, group_paths=True).expose(app)


app.include_router(products.router)


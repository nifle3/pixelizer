from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine 


SQL_ALCHEMY_URL_CONNECTION = ""
engine = create_async_engine(SQL_ALCHEMY_URL_CONNECTION, echo=True)

app = FastAPI()


@app.get("/")
def index():
    return {"message": "hello world"}

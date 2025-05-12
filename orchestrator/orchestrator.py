from fastapi import FastAPI, Request
from pydantic import BaseModel
import requests

app = FastAPI()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(query: Query):
    market_data = requests.post("http://localhost:8001/market", json={"query": query}).json()

    earnings = requests.post("http://localhost:8002/earnings", json={"query": query}).json()

    answer = f"Today, your Asia tech allocation is {market_data['allocation']}% of AUM. " \
             f"{earnings['summary']}"
    return {"response": answer}

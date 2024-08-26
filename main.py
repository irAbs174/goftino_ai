from datetime import datetime

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

@app.webhooks.post("/webhook")
def new_subscription(request: Request):
    data = request.json()
    print("Received data:")
    print(data)
    return {"status": "success", "received": data}
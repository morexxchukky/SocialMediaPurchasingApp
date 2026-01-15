from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow HTML files to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple data storage (memory)
DATA = {
    "services": {
        "accounts": 49.99,
        "likes": 19.99,
        "followers": 29.99
    }
}

class Pricing(BaseModel):
    accounts: float
    likes: float
    followers: float

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.get("/api/config")
def get_config():
    return DATA

@app.post("/api/pricing")
def update_pricing(pricing: Pricing):
    DATA["services"] = pricing.dict()
    return {"message": "Prices updated"}

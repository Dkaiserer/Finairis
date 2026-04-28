from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from backend.database import Database

app = FastAPI()
db = Database()

# --------------------
# MODELL
# --------------------
class Transaction(BaseModel):
    amount: int
    is_income: bool
    category: str

# --------------------
# ADD TRANSACTION
# --------------------
@app.post("/transactions")
def add_transaction(t: Transaction):
    date = datetime.now().strftime("%Y-%m-%d")

    db.add_transaction(
        t.amount,
        t.is_income,
        t.category,
        date
    )

    return {"status": "ok"}

# --------------------
# GET ALL
# --------------------
@app.get("/transactions")
def get_transactions():
    data = db.get_transactions()

    balance = 0
    for t in data:
        if t["is_income"]:
            balance += t["amount"]
        else:
            balance -= t["amount"]

    return {
        "balance": balance,
        "transactions": data
    }

# --------------------
# DELETE
# --------------------
@app.delete("/transactions/{tx_id}")
def delete_transaction(tx_id: int):
    db.delete_transaction(tx_id)
    return {"status": "deleted"}
@app.get("/")
def root():
    return {"message": "Finance API is running 🚀"}
@app.get("/stats")
def get_stats():
    data = db.get_transactions()

    stats = {}

    for t in data:
        if not t["is_income"]:
            cat = t["category"]
            stats[cat] = stats.get(cat, 0) + t["amount"]

    return stats
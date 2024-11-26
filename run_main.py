import os
import uvicorn
from fastapi import FastAPI, Query
from pymongo import MongoClient
from datetime import datetime
from typing import Dict
from dotenv import load_dotenv


load_dotenv('dev.env')

MONGO_CLIENT= str(os.getenv('MONGO_CLIENT'))

app = FastAPI(title="Real-Time MQTT Message Processing with RabbitMQ and FastAPI")


mongo_client = MongoClient(MONGO_CLIENT)
db = mongo_client["mqtt_db"]
collection = db["mqtt_messages"]

@app.get("/status_counts/")
def get_status_counts(start_time: datetime = Query(..., description="Start time 2024-11-26T10:00:00"), end_time: datetime = Query(..., description="End time 2024-11-26T15:00:00")) -> Dict[int, int]:
    pipeline = [
        {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
        {"$group": {"_id": "$status", "count": {"$sum": 1}}}
    ]

    results = collection.aggregate(pipeline)
    return {item["_id"]: item["count"] for item in results}


if __name__ == "__main__":
   uvicorn.run("run_main:app", host="127.0.0.1", port=8000, reload=True)

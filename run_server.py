import os
import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
from datetime import datetime
from dotenv import load_dotenv


load_dotenv('dev.env')

MONGO_CLIENT= str(os.getenv('MONGO_CLIENT'))
CLIENT_SUBSCRIBE = str(os.getenv('CLIENT_SUBSCRIBE'))

mongo_client = MongoClient(MONGO_CLIENT)
db = mongo_client["mqtt_db"]
collection = db["mqtt_messages"]

def on_message(client, userdata, msg):
    try:
        decoded_message = msg.payload.decode()
        message = json.loads(decoded_message)
        message["timestamp"] = datetime.utcnow()
        collection.insert_one(message)
        print(f"Inserted: {message}")
    except json.JSONDecodeError as err:
        print(f"Error while json decode: {err}")

def start_server():
    client = mqtt.Client()
    client.connect("localhost", 1883)
    client.subscribe(CLIENT_SUBSCRIBE)
    client.on_message = on_message
    client.loop_forever()

if __name__ == "__main__":
    start_server()

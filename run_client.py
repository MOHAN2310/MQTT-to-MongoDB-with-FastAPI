import os
import json
import paho.mqtt.client as mqtt
import random
import time
from dotenv import load_dotenv

load_dotenv('dev.env')

CLIENT_SUBSCRIBE = str(os.getenv('CLIENT_SUBSCRIBE'))

broker = "localhost"
port = 1883

client = mqtt.Client()

def publish_messages():
    client.connect(broker, port)
    while True:
        message = json.dumps({"status": random.randint(0, 6)})
        client.publish(CLIENT_SUBSCRIBE, str(message))
        print(f"Published: {message}")
        time.sleep(1)

if __name__ == "__main__":
    publish_messages()

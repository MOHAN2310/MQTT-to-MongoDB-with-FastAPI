# MQTT-to-MongoDB-with-FastAPI
This project demonstrates a real-time messaging system that integrates MQTT with RabbitMQ and FastAPI.

## **Project Overview**
This project demonstrates a real-time messaging system that integrates MQTT with RabbitMQ and FastAPI. It consists of three main components:
1. **`run_client.py`**: Publishes MQTT messages containing random `status` values every second.
2. **`run_server.py`**: Consumes these MQTT messages and stores them in MongoDB.
3. **`run_main.py`**: Exposes an API endpoint to query the MongoDB data for counts of each `status` value within a specified time range.

---

## **Features**
- Real-time message publishing and processing.
- Integration with RabbitMQ for MQTT messaging.
- MongoDB for data storage and querying.
- FastAPI-based API for retrieving message statistics.

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Prerequisites](#prerequisites)
3. [Project Setup](#project-setup)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)

## Getting Started
Follow the instructions below to set up and run your FastAPI project.

### Prerequisites
Ensure you have the following installed:

- Python >= 3.12
- MongoDB
- RabbitMQ[enable mqtt port]

### Project Setup
1. Clone the project repository:
    ```bash
    git clone https://github.com/MOHAN2310/MQTT-to-MongoDB-with-FastAPI.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd MQTT-to-MongoDB-with-FastAPI/
    ```

3. Create and activate a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set up environment variables by copying the example configuration:
    ```bash
    cp .env.example .env
    ```


## Running the Application
Start the Client:
    ```
    Python run_client.py
    ```

Start the Server:
    ```
    Python run_server.py
    ```

Start the main:
    ```
    Python run_main.py
    ```

---

## API Documentation

The API provides an endpoint for querying message statistics based on a time range.

### **Endpoint**
- **URL**: `http://127.0.0.1:8000/status_counts`
- **Method**: `POST`

### **Request Body**
Provide the start and end times in ISO 8601 format (`YYYY-MM-DDTHH:MM:SS`):
```json
{
  "start_time": "2024-11-25T12:00:00",
  "end_time": "2024-11-25T12:30:00"
}
```

### **Response**
Returns the count of each status value within the specified time range:
```json
{
  "status_counts": {
    "0": 5,
    "1": 10,
    "2": 8,
    "3": 7,
    "4": 4,
    "5": 6,
    "6": 9
  }
}
```


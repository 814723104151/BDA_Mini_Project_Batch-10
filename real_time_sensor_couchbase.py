# real_time_sensor_couchbase.py
"""
Real-Time Sensor Data Storage using Couchbase
Mini Project for Big Data Analysis

This program simulates multiple sensors generating temperature, humidity,
and pressure readings and stores them in Couchbase as JSON documents in real-time.
"""

from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.collection import UpsertOptions
from couchbase.exceptions import CouchbaseException
import random
import datetime
import time

# -----------------------
# Couchbase Configuration
# -----------------------
COUCHBASE_HOST = 'couchbase://127.0.0.1'  # Couchbase server URL
USERNAME = 'Administrator'                 # Couchbase username
PASSWORD = 'password'                      # Couchbase password
BUCKET_NAME = 'sensor_data'                # Couchbase bucket name

# -----------------------
# Connect to Couchbase
# -----------------------
try:
    cluster = Cluster(COUCHBASE_HOST, ClusterOptions(PasswordAuthenticator(USERNAME, PASSWORD)))
    bucket = cluster.bucket(BUCKET_NAME)
    collection = bucket.default_collection()
    print("[INFO] Connected to Couchbase bucket:", BUCKET_NAME)
except CouchbaseException as e:
    print("[ERROR] Failed to connect to Couchbase:", e)
    exit(1)

# -----------------------
# Sensor Simulation
# -----------------------
SENSOR_IDS = ['S001', 'S002', 'S003']  # List of sensors

def generate_sensor_reading(sensor_id):
    """Generate random sensor reading."""
    return {
        "sensor_id": sensor_id,
        "timestamp": datetime.datetime.utcnow().isoformat(),  # UTC timestamp
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": random.randint(40, 60),
        "pressure": random.randint(1000, 1025)
    }

# -----------------------
# Insert Data into Couchbase
# -----------------------
def insert_sensor_data(reading):
    """Insert or update sensor reading into Couchbase."""
    doc_id = f"{reading['sensor_id']}::{reading['timestamp']}"
    try:
        collection.upsert(doc_id, reading, UpsertOptions(timeout=5))
        print(f"[INSERTED] {reading}")
    except CouchbaseException as e:
        print("[ERROR] Failed to insert document:", e)

# -----------------------
# Query Example
# -----------------------
def query_last_readings(sensor_id, limit=5):
    """Query last N readings for a sensor."""
    query = f"""
    SELECT sensor_id, timestamp, temperature, humidity, pressure
    FROM `{BUCKET_NAME}`
    WHERE sensor_id = '{sensor_id}'
    ORDER BY timestamp DESC
    LIMIT {limit};
    """
    try:
        result = cluster.query(query)
        print(f"\n[INFO] Last {limit} readings for {sensor_id}:")
        for row in result:
            print(row)
    except CouchbaseException as e:
        print("[ERROR] Query failed:", e)

# -----------------------
# Main Loop
# -----------------------
def main():
    print("[INFO] Starting sensor data simulation...")
    try:
        while True:
            for sensor_id in SENSOR_IDS:
                reading = generate_sensor_reading(sensor_id)
                insert_sensor_data(reading)
            time.sleep(1)  # Simulate 1-second interval between readings
    except KeyboardInterrupt:
        print("\n[INFO] Simulation stopped by user.")
        # Example: Query last 5 readings for S001 after stopping
        query_last_readings('S001', limit=5)

# -----------------------
# Run the Script
# -----------------------
if __name__ == "__main__":
    main()

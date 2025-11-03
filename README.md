# Real-Time Sensor Data Storage using Couchbase

## 1. Title
**Real-Time Sensor Data Storage using Couchbase**

---

## 2. Introduction
With the rapid growth of IoT devices, real-time sensor data is generated continuously.  
Storing and analyzing this data requires a **scalable, high-performance database**.  

This project demonstrates how **Couchbase**, a NoSQL distributed database, can be used to **store, query, and analyze real-time sensor data**.  
It simulates multiple sensors generating readings such as **temperature, humidity, and pressure**, enabling **Big Data Analysis** applications.

---

## 3. Objective
- Simulate real-time sensor data for multiple IoT devices.  
- Store sensor readings in Couchbase as **JSON documents**.  
- Query and retrieve sensor data efficiently for analysis.  
- Demonstrate **integration of NoSQL databases with real-time applications**.  

---

## 4. Existing System
Traditional relational databases face challenges handling high-velocity IoT data.  

### Limitations:
- Rigid schemas make adding new sensor types difficult.  
- Low performance with frequent inserts.  
- Limited horizontal scalability.  
- Hard to integrate with real-time analytics dashboards.  

---

## 5. Proposed System
The proposed system uses **Couchbase for real-time, scalable storage**:

- Each sensor reading stored as a **JSON document**.  
- Supports multiple sensors simultaneously.  
- Enables **fast querying** using N1QL.  
- Flexible schema for new sensors or reading types.  
- Compatible with visualization tools for **real-time analytics**.  

---

## 6. Algorithm / Methodology
### Steps:
1. **Setup Couchbase:**  
   - Install Couchbase server and create a bucket named `sensor_data`.  

2. **Sensor Simulation:**  
   - Simulate multiple sensors generating readings for temperature, humidity, and pressure.  

3. **Data Storage:**  
   - Store sensor readings in Couchbase using Python SDK.  
   - Each reading stored as a JSON document with unique key (`sensor_id::timestamp`).  

4. **Querying & Analytics:**  
   - Retrieve last N readings for any sensor using N1QL.  
   - Perform basic analytics or integrate with visualization dashboards.  

5. **Real-Time Processing:**  
   - Continuously generate and store data at 1-second intervals.  
   - Handle multiple sensors concurrently.  

---

## 7. Tools and Software Used

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Simulation and data insertion |
| **Couchbase Server (Community Edition)** | NoSQL database for storing sensor data |
| **Couchbase Python SDK** | Connect and interact with Couchbase from Python |
| **VS Code / Jupyter Notebook** | Development and execution |
| **Matplotlib / Pandas** | Optional: Data analysis and visualization |
| **GitHub** | Version control and repository hosting |

---

## 8. System Architecture 
1. **Sensor Layer:** Generates simulated sensor data.  
2. **Data Ingestion Layer:** Python script inserts data into Couchbase.  
3. **Database Layer:** Couchbase stores readings as JSON documents.  
4. **Analytics Layer:** Queries and analyzes sensor readings.  
5. **Visualization Layer:** Optional dashboards show trends and patterns.  

---

## 9. Dataset Schema (Input Format)
| Column Name      | Description |
|-----------------|-------------|
| `sensor_id`     | Unique identifier for each sensor (e.g., S001) |
| `timestamp`     | UTC timestamp of the reading |
| `temperature`   | Temperature in Celsius |
| `humidity`      | Humidity percentage |
| `pressure`      | Atmospheric pressure in hPa |

---

## 10. Workflow / Steps
1. Install Couchbase Server and create a bucket (`sensor_data`).  
2. Configure Couchbase credentials in the Python script.  
3. Run the simulation script to generate and store sensor readings.  
4. Insert readings as JSON documents in real-time.  
5. Query last N readings for analysis.  
6. Optionally visualize trends using Python or dashboards.  

---

## 11. Advantages
- Real-time data storage with minimal latency.  
- Flexible schema for different sensor types.  
- Scalable horizontally for large IoT networks.  
- Fast querying and analytics support.  
- Easy integration with visualization dashboards.  

---

## 12. Applications
- Industrial IoT sensor monitoring.  
- Smart homes and smart cities data collection.  
- Environmental monitoring (weather stations, air quality).  
- Predictive maintenance using real-time sensor analytics.  
- Educational demonstrations of NoSQL and Big Data integration.  

---

## 13. Conclusion
The **Real-Time Sensor Data Storage using Couchbase** project demonstrates how to **simulate, store, and analyze IoT sensor data** in real-time.  
It provides a **flexible and scalable solution** for handling high-velocity data and enables **real-time analytics and monitoring** for Big Data applications.  

---

## 14. Future Enhancement
- Integrate **real-time dashboards** using Grafana or Kibana.  
- Add **predictive analytics** for forecasting sensor trends.  
- Support **dynamic addition of sensors and readings**.  
- Implement **alerts for abnormal readings**.  

---

## 15. References
1. Couchbase Documentation – [https://docs.couchbase.com](https://docs.couchbase.com)  
2. Python SDK for Couchbase – [https://pypi.org/project/couchbase](https://pypi.org/project/couchbase)  
3. IoT Sensor Data Handling and Storage Techniques – IEEE Journals  
4. Tanenbaum, A., & van Steen, M., **Distributed Systems: Principles and Paradigms**, 3rd Edition  
5. Python Documentation – `pandas`, `matplotlib`, `datetime`  

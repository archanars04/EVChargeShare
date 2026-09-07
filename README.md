# 🚗⚡ EVChargeShare

### Smart EV Charging Station Recommendation System

EVChargeShare is a Python-based application that helps EV users choose the most suitable charging station based on multiple real-world factors such as battery level, distance, waiting time, charging cost, and charger availability.

Instead of simply finding nearby charging stations, EVChargeShare **ranks available stations and recommends the best option for the user's current situation.**

---

## 💡 Problem

EV drivers may find multiple charging stations nearby, but choosing the best one can be difficult.

A station may be:
- Close but have a long waiting time
- Cheap but far away
- Fast but have limited charger availability

EVChargeShare addresses this decision-making problem using a **multi-factor scoring algorithm**.

---

## 🚀 Features

- 🔋 Battery-level based recommendation
- 📍 Distance consideration
- ⏳ Waiting-time consideration
- 💰 Charging-cost consideration
- 🔌 Available-charger consideration
- 🧮 Multi-factor station scoring
- 🏆 Automatic best-station recommendation
- 🌐 Interactive Streamlit web interface

---

## 🧠 How It Works

The system calculates a score for every charging station:

**Lower score = Better recommendation**

The scoring model considers:

- Distance
- Waiting time
- Charging cost
- Available chargers

When the battery level is **20% or below**, distance receives a higher weight because reaching a charging station becomes more critical.

---

## 🛠️ Technologies Used

- Python
- JSON
- Streamlit
- Git
- GitHub

---

## 📂 Project Structure

```text
EVChargeShare/
│
├── app.py
├── webapp.py
├── stations.json
└── README.md
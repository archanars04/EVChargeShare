import streamlit as st
import json

with open("stations.json", "r") as file:
    stations = json.load(file)


def calculate_score(station, battery_level):
    if battery_level <= 20:
        distance_weight = 20
    else:
        distance_weight = 10

    return (
        station["distance"] * distance_weight
        + station["wait_time"] * 2
        + station["cost_per_kwh"] * 3
        - station["available_chargers"] * 5
    )


st.title("🚗⚡ EVChargeShare")
st.subheader("Smart EV Charging Station Recommendation")

battery_level = st.slider(
    "🔋 Current Battery Level (%)",
    0,
    100,
    50
)

if st.button("Find Best Charging Station"):

    best_station = None
    best_score = float("inf")

    for station in stations:
        score = calculate_score(station, battery_level)

        if score < best_score:
            best_score = score
            best_station = station

    st.success("🏆 Best Charging Station Found!")

    st.header(best_station["name"])

    col1, col2 = st.columns(2)

    with col1:
        st.write("📍 Distance:", best_station["distance"], "km")
        st.write("⏳ Waiting Time:", best_station["wait_time"], "minutes")
        st.write("💰 Cost:", "₹", best_station["cost_per_kwh"], "/kWh")

    with col2:
        st.write(
            "🔌 Chargers:",
            best_station["available_chargers"],
            "/",
            best_station["total_chargers"]
        )
        st.write("⚡ Charging Speed:", best_station["charging_speed"])
        st.write("🧮 Score:", round(best_score, 2))
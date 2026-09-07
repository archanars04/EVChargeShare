import json

with open("stations.json", "r") as file:
    stations = json.load(file)

battery_level = float(input("Enter your current battery percentage: "))

print("Charging stations loaded:")

for station in stations:
    print(station["name"])

def calculate_score(station, battery_level):
    if battery_level <= 20:
        distance_weight = 20
    else:
        distance_weight = 10
    score = (
        station["distance"] * distance_weight
        + station["wait_time"] * 2
        + station["cost_per_kwh"] * 3
        - station["available_chargers"] * 5
    )

    return score

print("\nStation Scores:")

for station in stations:
    score = calculate_score(station, battery_level)
    print(station["name"], "→", score)

best_station = None
best_score = float("inf")
for station in stations:
    score = calculate_score(station, battery_level)

    if score < best_score:
        best_score = score
        best_station = station

print("\n🏆 Recommended Charging Station")
print("--------------------------------")
print("Station:", best_station["name"])
print("Distance:", best_station["distance"], "km")
print("Waiting Time:", best_station["wait_time"], "minutes")
print("Cost:", "₹", best_station["cost_per_kwh"], "/kWh")
print(
    "Available Chargers:",
    best_station["available_chargers"],
    "/",
    best_station["total_chargers"]
)
print("Charging Speed:", best_station["charging_speed"])
print("Score:", best_score)
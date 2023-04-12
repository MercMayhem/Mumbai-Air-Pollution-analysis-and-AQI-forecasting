import json
import requests

# api_url = f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page=1&offset=0&sort=desc&parameter_id=2&parameter=&radius=1000&location_id={}&order_by=datetime"

with open('location_id.json', 'r') as location_id_file:
    location_ids = json.load(location_id_file)

location_datapoints = {}

for location, id in location_ids.items():
    api_url = f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page=1&offset=0&sort=desc&parameter_id=2&radius=100&location_id={id}&order_by=datetime"
    response = requests.get(api_url)

    response_json = response.json()
    location_datapoints[location] = response_json["meta"]['found']

locations = list(location_datapoints.keys())
sorted_datapoints = list(location_datapoints.values())

for i in range(len(sorted_datapoints)):
    for j in range(0, len(sorted_datapoints) - i - 1):
        if sorted_datapoints[j] > sorted_datapoints[j+1]:

            temp = sorted_datapoints[j]
            sorted_datapoints[j] = sorted_datapoints[j+1]
            sorted_datapoints[j+1] = temp

            temp = locations[j]
            locations[j] = locations[j+1]
            locations[j+1] = temp

sorted_location_datapoints = {locations[i] : sorted_datapoints[i] for i in range(len(sorted_datapoints))}

with open('location_datapoints.json', 'w') as file:
    json.dump(sorted_location_datapoints, file)

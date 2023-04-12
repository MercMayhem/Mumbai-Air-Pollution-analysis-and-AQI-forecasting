import json

with open('locations.json', 'r') as location_file:
    locations = json.load(location_file)

location_id = {}
results = locations["results"]

for i in range(len(results)):
    location_id[results[i]['name']] = results[i]['id']

with open("location_id.json", 'w') as id_file:
    json.dump(location_id, id_file)
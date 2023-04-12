import requests

id = 6928
test = f"https://api.openaq.org/v2/measurements?date_from=2000-01-01T00%3A00%3A00%2B00%3A00&date_to=2022-09-29T15%3A10%3A00%2B00%3A00&limit=100&page=1&offset=0&sort=desc&parameter_id=2&radius=100&location_id={id}&order_by=datetime"
response = requests.get(test)

print(response.json())
import requests
import json

# Flaresolverr endpoint
url = 'http://localhost:8191/v1'

# Request payload
data = {
    "cmd": "request.get",
    "url": "https://iproyal.com",
    "maxTimeout": 60000  # 60 seconds
}

# Headers
headers = {
    'Content-Type': 'application/json'
}

# Send POST request to Flaresolverr
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response content
print(response.text)

import requests
import json

# Flaresolverr endpoint
url = 'http://localhost:8191/v1'

# Request payload, including a custom User-Agent
data = {
    "cmd": "request.get",
    "url": "https://example.com",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "maxTimeout": 60000  # 60 seconds
}

# Headers for the POST request
headers = {
    'Content-Type': 'application/json'
}

# Send POST request to Flaresolverr
response = requests.post(url, data=json.dumps(data), headers=headers)

# Print the response content
print(response.text)

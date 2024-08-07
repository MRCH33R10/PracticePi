import requests
import json

url = 'http://192.168.0.189:5000/data'
data = {'key': 'value'}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    try:
        json_response = response.json()
        print(f"Response from server: {json_response}")
    except json.JSONDecodeError:
        print("Failed to parse JSON response:")
        print(response.text)
except requests.RequestException as e:
    print(f"Request failed: {e}")

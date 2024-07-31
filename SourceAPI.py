# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home ():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)
# import requests

# # Replace '192.168.1.10' with the actual IP address of your Raspberry Pi Zero 2 W
# raspberry_pi_ip = '192.168.0.125' 
# r = requests.get(f'http://127.0.0.1:5000')
# print(r.status_code)
# print(r.text)
import requests
import json

url = 'http://192.168.0.162:5000/data'
data = {'key': 'value'}

response = requests.post(url, json=data)
print(f"Response from server: {response.json()}")


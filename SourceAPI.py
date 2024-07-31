# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home ():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)
import requests
r = requests.get('http://google.com')
# print(r.status_code)
print(r.text)
# print(r.text[0:1000])

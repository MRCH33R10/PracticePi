# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home ():
#     return "Hello, World!"

# if __name__ == "__main__":
#     app.run(debug=True)
raspberry_pi_ip = '192.168.1.10' 
r = requests.get(f'http://{raspberry_pi_ip}:5000/')
print(r.status_code)
print(r.text)

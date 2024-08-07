import http.server
import socketserver
import os

PORT = 8000  # You can choose any port you prefer
DIRECTORY = "/Users/nicholasthompson/Desktop"  # Replace with the directory containing your MP4 file

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Change to the specified directory
os.chdir(DIRECTORY)

# Create an object of the above class
handler_object = MyHttpRequestHandler

# Create a TCP socket server
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
# /Users/nicholasthompson/Desktop/Extracurricular/file_example_MP4_480_1_5MG.mp4

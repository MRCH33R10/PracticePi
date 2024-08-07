# import http.server
import socketserver
import os

PORT = 8000  # You can choose any port you prefer
DIRECTORY = "/home/NicholasThompson/PracticePi/NetworkInt/SouthPark"  # Replace with the directory containing your MP4 files

# Create a mapping of numbers to file names
file_mapping = {
    "S1E1": "South_Park_S01E01_Cartman_Gets_an_Anal_Probe.mp4",
    "S1E2": "South_Park_S01E02_Weight_Gain_4000.mp4",
    "S1E3": "South_Park_S01E03_Volcano.mp4",
    "S1E4": "South_Park_S01E04_Big_Gay_Al.mp4",
    "S1E5": "South_Park_S01E05_An_Elephant_Makes_Love_to_a_Pig.mp4",
    "S1E6": "South_Park_S01E06_Death.mp4",
    "S1E7": "South_Park_S01E07_Pinkeye.mp4",
    "S1E8": "South_Park_S01E08_Starvin__Marvin.mp4",
    "S1E9": "South_Park_S01E09_Mr._Hankey.mp4",
    "S1E10": "South_Park_S01E10_Damien.mp4",
    "S1E11": "South_Park_S01E11_Tom_s_Rhinoplasty.mp4",
    "S1E12": "South_Park_S01E12_Mecha-Streisand.mp4",
    "S1E13": "South_Park_S01E13_Cartman_s_Mom_is_a_Dirty_Slut.mp4"
}

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def do_GET(self):
        # Extract the number from the URL path
        number = self.path.strip("/")

        # Check if the number is in the file mapping
        if number in file_mapping:
            # Serve the corresponding file
            self.path = "/" + file_mapping[number]
        else:
            # If the number is not found, serve a 404 response
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"File not found")
            return

        # Call the superclass method to serve the file
        return super().do_GET()

# Change to the specified directory
os.chdir(DIRECTORY)

# Create an object of the above class
handler_object = MyHttpRequestHandler

# Create a TCP socket server
with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

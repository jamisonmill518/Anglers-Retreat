import http.server
import socketserver
import os

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def log_message(self, format, *args):
        print(f"[ResourcePack] {self.address_string()} - {format % args}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving resource pack on port {PORT}")
    print(f"URL: http://25.57.2.7:{PORT}/anglers_retreat_resourcepack.zip")
    httpd.serve_forever()

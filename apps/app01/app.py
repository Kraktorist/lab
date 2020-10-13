import os
import socket
print(socket.gethostname())
print(os.environ)

from http.server import BaseHTTPRequestHandler, HTTPServer # python3
class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("received get request")

host = ''
port = 80
HTTPServer((host, port), HandleRequests).serve_forever()



import os
import socket
import json

from http.server import BaseHTTPRequestHandler,HTTPServer

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','application/json')
    self.end_headers()
    self.wfile.write(json.dumps(dict(os.environ),sort_keys=True, indent=4).encode())

serv = HTTPServer(("",80),HttpProcessor)
serv.serve_forever()

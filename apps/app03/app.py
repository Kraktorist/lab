import multiprocessing
import signal
import os
import socket
import json
import sqlite3
from time import sleep, gmtime, strftime
from http.server import BaseHTTPRequestHandler,HTTPServer

dbpath = os.environ['dbpath']
hostname = os.environ['HOSTNAME']
interval = int(os.environ['interval'])

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.send_header('content-type','application/json')
    self.end_headers()
    if os.path.isfile(dbpath):
      conn = sqlite3.connect(dbpath)
      c = conn.cursor()
      c.execute("SELECT * from status")
      conn.commit()
      self.wfile.write(json.dumps(c.fetchall(),sort_keys=True, indent=4).encode())
      conn.close()
    else:
      self.wfile.write(json.dumps("DB is not initialised",sort_keys=True, indent=4).encode())

def sigterm_handler(_signo, _stack_frame):
  print('exiting')
  conn.close()
  sys.exit(0)

def run_webserver():
  serv = HTTPServer(("",80),HttpProcessor)
  serv.serve_forever()

signal.signal(signal.SIGTERM, sigterm_handler)
p = multiprocessing.Process(target=run_webserver, args=())
p.daemon = True
p.start()

if not os.path.isfile(dbpath):
  conn = sqlite3.connect(dbpath)
  c = conn.cursor()
  c.execute('''CREATE TABLE status
             (date text, name text PRIMARY KEY)''')
  conn.commit()
  conn.close()

while True:
  conn = sqlite3.connect(dbpath)
  c = conn.cursor()
  c.execute("INSERT OR REPLACE INTO status (date, name) VALUES (?, ?)", (strftime("%Y-%m-%d %H:%M:%S", gmtime()),hostname))
  conn.commit()
  c.execute("select * from status")
  conn.commit()
  print(c.fetchall())
  conn.close()
  sleep(interval)

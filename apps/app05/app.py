import multiprocessing
import signal
import os
import socket
import json
import psycopg2
from time import sleep, gmtime, strftime
from http.server import BaseHTTPRequestHandler,HTTPServer
import sys

sleep(5)
dbserver = os.environ['dbserver']
dbname = os.environ['dbname']
dbuser = os.environ['dbuser']
dbpassword = os.environ['dbpassword']
conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbserver)

hostname = os.environ['HOSTNAME']
interval = int(os.environ['interval'])

class HttpProcessor(BaseHTTPRequestHandler):
  def do_GET(self):
    conn = psycopg2.connect(dbname=dbname, user=dbuser, password=dbpassword, host=dbserver)
    self.send_response(200)
    self.send_header('content-type','application/json')
    self.send_header('app_host', hostname)
    self.send_header('Refresh', '2')
    self.end_headers()
    if conn:
      c = conn.cursor()
      c.execute("SELECT * FROM status ORDER BY inserted DESC")
      conn.commit()
      self.wfile.write(json.dumps(c.fetchall(),sort_keys=True, indent=4, default=str).encode())
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

while True:
  c = conn.cursor()
  current_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
  c.execute("""INSERT INTO status (name, interval) VALUES (%s, %s) 
             ON CONFLICT (name) DO UPDATE
             SET interval = EXCLUDED.interval""", (hostname, interval))
  conn.commit()
  c.execute("""DELETE FROM status WHERE updated<now() - INTERVAL '5 minutes'""")
  conn.commit()
  sleep(interval)

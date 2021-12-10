#!/usr/bin/python
import socket
import threading
import subprocess

def closePort():
    print("Port close start...")
    subprocess.call(["ufw","deny","445/tcp"])

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('192.168.1.78',445))
    if result == 0:
        print "Port is open."
        t = threading.Timer(10.0, closePort)
        t.start()
        print "Port close scheduled."
    else:
        print "Port is closed."
    sock.close()
except:
    pass

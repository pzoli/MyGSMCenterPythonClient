#!/usr/bin/python
import serial
import json
import subprocess

with serial.Serial('/dev/ttyACM0', 19200, timeout=1) as ser:
	ringing = False
	while True:
		line = ser.readline()   # read a '\n' terminated line
		if len(line) > 0:
			print(line)
			map = json.loads(line)
			if map["action"]=="ring" and not ringing:
				print("phone number:"+map["from"])
				subprocess.call(["./setfirewall.sh",map["from"]])
				ringing = True
			if map["action"]=="call-status":
				if map["status"]=="NO CARRIER":
					ringing = False

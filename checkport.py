#!/usr/bin/python
import subprocess
import re

def checkPort(port):
    out = subprocess.check_output("ufw status verbose", shell=True)
    for v in out.split('\n'):
        if v.find(port) > -1:
            cols = re.split("\s\s+", v)
            #print cols
            if len(cols) > 0 and cols[0] == port:
                return cols[1]

print checkPort("445/tcp")

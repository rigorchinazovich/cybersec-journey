#!/usr/bin/env python3
import socket
import sys
socket.setdefaulttimeout(1)
ports=[22,53,80,443,8080,2052,2053,2082,8443,8880]
if len(sys.argv)<2:
    print("ERR нету хоста")
    print("н-р python port_scanner.py 127.0.0.1")
    sys.exit(1)
host=sys.argv[1]
for p in ports:
    s = socket.socket()
    result=s.connect_ex((host,p))
    if result == 0:
        print(str(p) + " open")
    s.close()
    


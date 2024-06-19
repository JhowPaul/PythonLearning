#Write a Python program to valid a IP address.

import socket

addr="127.0.0.2561"
try:
    socket.inet_aton(addr)
    print("IP valido")
except socket.error:
    print("IP invalido")

addr2="192.168.0.8"
try:
    socket.inet_aton(addr2)
    print("IP valido")
except socket.error:
    print("IP invalido")
  
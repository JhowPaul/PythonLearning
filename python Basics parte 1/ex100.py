#Write a Python program to get the name of the host on which the routine is running

import socket

proprietario=socket.gethostname()
print("o admin deste PC é: ",proprietario)
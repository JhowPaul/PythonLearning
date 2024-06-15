#Write a Python program to get a directory listing, sorted by creation date
from importlib.resources import path
import os
import time

destino=["%s %s"%(time.ctime(t),f)for t,f in sorted([(os.path.getctime(x),x)for x in os.listdir(".")])]
print("Listando diretório,organizado por data de criação: ")
for x in  range(len(destino)):
    print(destino[x],)
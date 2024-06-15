#Write a Python program to retrieve file properties.
import os.path
import time

print("Arquivo:             ",__file__)
print("Tempo de Acesso:     ",time.ctime(os.path.getatime(__file__)))
print("Tempo de Modificação:",time.ctime(os.path.getmtime(__file__)))
print("Tempo de Mudança:    ",time.ctime(os.path.getctime(__file__)))
print("Tamanho:             ",os.path.getsize(__file__))
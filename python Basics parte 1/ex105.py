#Write a Python program to divide a path on the extension separator
import os.path

for destino in ["teste.txt",'filename', 'D:\Backup HD Antigo\PYTHON GARAI\teste.py', '/', '' ]:
    print('"%s" :' % destino, os.path.splitext(destino))
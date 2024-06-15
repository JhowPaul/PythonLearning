#Write a Python program to check whether a file path is a file or a directory.

import os 

destino="abc.txt"
if os.path.isdir(destino):
    print("É um diretório")
elif os.path.isfile(destino):
    print("É um arquivo")
else:
    print("É um arquivo especial(socket,FIFO,device file)")
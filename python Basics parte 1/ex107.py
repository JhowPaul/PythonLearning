#Write a Python program to find path refers to a file or directory when you encounter a path name.
from importlib.resources import path
import os.path

for arquivo in [__file__,os.path.dirname(__file__),"/","./broken_link"]:
    print("Arquivo      :",arquivo)
    print("Absoluto     :",os.path.isabs(arquivo))
    print("É arquivo?   :",os.path.isfile(arquivo))
    print("É diretório? :",os.path.isdir(arquivo))
    print("Existe?      :",os.path.exists(arquivo))
    print("Link existe? :",os.path.lexists(arquivo))
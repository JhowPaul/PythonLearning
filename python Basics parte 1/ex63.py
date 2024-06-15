#Write a Python program to get an absolute file path.

def destino(dest):
    import os
    return os.path.abspath("dest")

print("Destino absoluto do arquivo: ",destino("teste.txt"))
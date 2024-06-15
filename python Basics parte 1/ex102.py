#Write a Python program to get system command output
import subprocess

retorna_texto=subprocess.check_output("dir",shell=True,universal_newlines=True)
print("dir comando para listar arquivos e diretórios")
print(retorna_texto)
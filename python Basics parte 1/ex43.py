# Write a Python program to get OS name, platform and release information.
import platform,os

print("Nome do sistema operacional: ",os.name)
print("Nome do sistema operacional: ",platform.system())
print("Versão do sistema operacional:",platform.release())
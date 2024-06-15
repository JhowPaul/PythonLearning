#Write a Python program to get file creation and modification date/times.
import os.path,time

print("Ultima modificação: %s"%time.ctime(os.path.getmtime("D:\Backup HD Antigo\PYTHON GARAI\ife.py")))
print("Criado: %s"% time.ctime(os.path.getctime("D:\Backup HD Antigo\PYTHON GARAI\ife.py")))


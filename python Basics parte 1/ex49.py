#Write a Python program to list all files in a directory in Python

from os import listdir
from os.path import isfile,join

arquivo=[x for x in listdir("D:\Backup HD Antigo\PYTHON GARAI") if isfile(join("D:\Backup HD Antigo\PYTHON GARAI",x))]
print(arquivo)
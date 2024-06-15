#Write a Python program to check whether a file exists

import os.path

print(os.path.isfile('main.txt'))
print(os.path.isfile('D:\Backup HD Antigo\PYTHON GARAI\exercicios em python\ex41.py'))

#OU

print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))

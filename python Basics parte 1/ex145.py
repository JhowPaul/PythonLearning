#Write a Python program to find the location of Python module sources

import imp 

print("Local do modulo os em python")
print(imp.find_module("os"))
print("Local do modulo pandas em python")
print(imp.find_module("pandas"))
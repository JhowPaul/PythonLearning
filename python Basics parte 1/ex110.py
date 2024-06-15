#Write a Python program to make file lists from current directory using a wildcard
import glob

lista=glob.glob("*.*")
print(lista)

print(glob.glob("*.py"))
print(glob.glob("./[0-9].*"))
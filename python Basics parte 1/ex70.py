#Write a Python program to sort files by date
import glob
import os

arquivo=glob.glob("*.txt")
arquivo.sort(key=os.path.getmtime)
print("\n".join(arquivo))
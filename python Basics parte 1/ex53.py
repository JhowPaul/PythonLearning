#Write a python program to access environment variables
import os

for x in os.environ:
    print(x)
    print("-"*15)
    print(os.environ[x])
    print("-"*30)

#OU
for item, valor in os.environ.items():
   print(f'{item} {valor}')

#OU
print(os.environ['PATH'])
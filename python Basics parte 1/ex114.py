#Write a Python program to compute the product of a list of integers (without using for loop).
from functools import reduce
import math

lista=sum([1,2,3,4,5])
print(lista)

lista2=math.prod([1,2,3,4,5])
print(lista2)

#OU

lista3=[6,7,8,9,10]

produto_lista3=reduce(lambda x,y:x*y,lista3)
print(produto_lista3)
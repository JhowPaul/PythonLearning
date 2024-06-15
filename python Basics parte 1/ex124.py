#Write a Python program to sum of all counts in a collections
import collections
numero=[2,2,4,6,6,8,6,10,4]
print(sum(collections.Counter(numero).values()))#conta a quantidade de itens na lista,começando por 0
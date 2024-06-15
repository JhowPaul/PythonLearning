#Write a Python program to test whether all numbers of a list is greater than a certain number.

numero=[2,3,4,5]

print(all(x>1 for x in numero))
print(all(x>4 for x in numero))
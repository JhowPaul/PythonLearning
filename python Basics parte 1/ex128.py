#Write a Python program to add leading zeroes to a string.

numero='122.22'
print("Original String: ",numero)
print("\nAdded trailing zeros:")
numero = numero.ljust(8, '0')
print(numero)
numero = numero.ljust(10, '0')
print(numero)
print("\nAdded leading zeros:")
numero='122.22'
numero = numero.rjust(8, '0')
print(numero)
numero = numero.rjust(10, '0')
print(numero)

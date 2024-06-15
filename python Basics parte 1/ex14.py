#Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

a=18

if a>17:
    a*=2
    print(a)
else:
    print("numero menor que 17")

#OU
numero=int(input("digite um numero: "))

if numero>17:
    a*=2
    print(a)
else:
    print("numero menor que 17")


#OU
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

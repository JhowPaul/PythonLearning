#Write a Python program to calculate the sum of three given numbers,
#if the values are equal then return three times of their sum

def calcula(a,b,c):
    sum= a + b + c
   
    if a == b == c:
        sum*=3
    return sum
   
print(calcula(1,1,1))
print(calcula(1,2,1))

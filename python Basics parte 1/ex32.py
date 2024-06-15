#Write a Python program to get the least common multiple (LCM) of two positive integers.


#In arithmetic and number theory, the least common multiple, lowest common multiple, 
#or smallest common multiple of two integers a and b, usually denoted by lcm(a, b), 
#is the smallest positive integer that is divisible by both a and b.
#Since division of integers by zero is undefined, this definition has meaning only 
# if a and b are both different from zero. However, some authors define lcm(a,0) as 0 for all a, 
# which is the result of taking the lcm to be the least upper bound in the lattice of divisibility.

def mmc(x,y):
    if x>y:
        z=x
    else:
        z=y
    while True:
        if z%x==0 and  z%y==0:
            mmc=z
            break
        z+=1
    return mmc

print("o mmc de 17 e 12 é: ",mmc(15,17))

#OU 
from functools import reduce
from math import gcd

def mmc2(numeros):
    return reduce((lambda x,y:int(x*y/gcd(x,y))),numeros)

print(mmc2([12,7]))
print(mmc2([1, 3, 4, 5])) 

#OU


def mmc3(a,b):
    return (a*b) //gcd(a,b)
print (mmc3(4,6))

#OU
import math
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
lcm_res = math.lcm(num1, num2)
print(f'The least common multiple for your numbers {num1} and {num2} is {lcm_res}.')
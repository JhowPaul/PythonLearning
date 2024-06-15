#Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

#The greatest common divisor (GCD) of two nonzero integers a and b is the greatest positive 
#integer d such that d is a divisor of both a and b; that is, there are 
#integers e and f such that a = de and b = df, and d is the largest such integer. 
#The GCD of a and b is generally denoted gcd(a, b).
def mdc(x,y):
    mdc=1
    if x%y==0:
        return y
    for i in range(int(y/2),0,-1):
        if x%i==0 and y%i==0:
            mdc=i
            break
    return mdc
print ("o mdc de 12 e 17 é =",mdc(18,17))
print ("o mdc de 4 e 6 é =",mdc(4,6))
print ("o mdc de 336 e 360 é =",mdc(336,360))

#OU

def gcd(x, y):
 z = x % y
 while z:
   x = y
   y = z
   z = x % y
 return y
print("GCD of 12 & 17 =",gcd(12, 17))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))

#OU

from functools import reduce
from math import gcd as _gcd
def gcd(numero):
  return reduce(_gcd, numero)
numero = [336, 360]
print("GCD of",','.join(str(e) for e in numero))
print(gcd(numero))
numero = [12, 17]
print("GCD of",','.join(str(e) for e in numero))
print(gcd(numero))
numero = [4, 6]
print("GCD of",','.join(str(e) for e in numero))
print(gcd(numero))
numero = [24, 30, 36]
print("GCD of",','.join(str(e) for e in numero))
print(gcd(numero))


#OU
import math
num1 = int(input('Please enter a number: '))
num2 = int(input('Please enter another number: '))
gcd_res = math.gcd(num1, num2)
print(f'The greatest common divisor for your numbers {num1} and {num2} is {gcd_res}.')

#OU
print(math.gcd(27,63))
#Write a Python function that takes a positive integer and returns the sum of the cube of all 
#the positive integers smaller than the specified number.

def calcula(x):
    x-=1
    total=0
    while x>0:
        total+=x**3
        x-=1
    return total

print(calcula(3))
print(calcula(6))#pega todos os inteiros anteriores a 6 elevados ao cubo e soma 5**3,4**3,3**3,2**3,1**3
                 #125+64+27+8+1=225
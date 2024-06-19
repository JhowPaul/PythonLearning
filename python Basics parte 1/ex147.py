#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.

def verifica(x):
    mx=x[0]
    mn=x[0]
    for numero in x:
        if numero>mx:
            mx=numero
        elif numero<mn:
            mn=numero
    return mx,mn

print(verifica([0,1,2,30,-7,8]))


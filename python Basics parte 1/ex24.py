#Write a Python program to check whether a specified value is contained in a group of values
lista1=[1,2,3,4,5,6]
lista2=[9,3,6,1,2,5]

def chegar(arquivo,x):
    
    for i in arquivo:
        if x==i:
            return True
    return False
    
print(chegar(lista1,3))
print(chegar(lista2,9))
print(chegar([3,2,1],4))
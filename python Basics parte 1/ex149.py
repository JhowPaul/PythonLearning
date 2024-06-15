#Write a Python function to check whether a distinct pair of numbers 
#whose product is odd present in a sequence of integer values.

def impar(x):
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j:
                produto=x[i]*x[j]
                if produto &1:
                    return True
    return False

a=[2,4,6,8] #multiplica cada numero pelos seus sucessores 2*4,2*6,2*8,4*6...se o resultado for impar a sentença é verdadeira
b=[1,3,5,7]
c=[1,4,6,7]

print(impar(a))
print(impar(b))
print(impar(c))




def impar2(y):
    for i in range(len(y)):
        for j in range(len (y)):
            if i!=j:
                recebe=y[i]*y[j]
                return True
    return False


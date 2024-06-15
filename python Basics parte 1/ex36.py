# Write a Python program to add two objects if both objects are an integer type


def casoInt(x,y):
    if not (isinstance(x,int))and isinstance(y,int):
        return "variaveis devem ser numeros inteiros"
    return x+y

print(casoInt(2,3))
print(casoInt(10.1,9))        

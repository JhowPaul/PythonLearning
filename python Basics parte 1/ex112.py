#Write a Python program to input a number, if it is not a number generates an error message

while True:
    try:
        numero=int(input("Insira um numero: "))
        break
    except ValueError:
        print("Apenas numes são permitidos")

#OU
x = 1.23
x_int = x.is_integer()
print("Checa que x é um inteiro!")
print(x_int)
y= 1.0
y_int = y.is_integer()
print("Checa que y é um inteiro!")
print(y_int)  

#OU
x = 1.0
x_int =isinstance(x,int)
print("Checa que x é um inteiro!")
print(x_int)
y= 1
y_int =isinstance(y,int)
print("Checa que y é um inteiro!")
print(y_int)  
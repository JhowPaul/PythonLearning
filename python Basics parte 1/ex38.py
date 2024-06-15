# Write a Python program to solve (x + y) * (x + y).
# x = 4, y = 3 Expected Output : (4 + 3) ^ 2) = 49
def calcula(x,y):
    z=(x+y)**2
    return z


print("Calculo",calcula(2,2))

a=int(input("Digite o primeiro numero: "))
b=int(input("Digite o segundo numero: "))

print(calcula(a,b))
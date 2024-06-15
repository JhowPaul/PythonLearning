#Write a Python program to get the seize of an object in bytes.
import sys
str1 = "um"
str2 = "dois"
str3 = "tres"
x = 0
y = 112
z = 122.56

print("Tamanho de ",str1,"=",str(sys.getsizeof(str1))+ " bytes")
print("Tamanho de ",str2,"=",str(sys.getsizeof(str2))+ " bytes")
print("Tamanho de ",str3,"=",str(sys.getsizeof(str3))+ " bytes")
print("Tamanho de",x,"=",str(sys.getsizeof(x))+ " bytes")
print("Tamanho de" ,y,"="+str(sys.getsizeof(y))+ " bytes")

L = [1, 2, 3, 'Vermelho', 'Preto']
print("Tamanho de",L,"=",sys.getsizeof(L)," bytes")

T = ("Vermelho", [8, 4, 6], (1, 2, 3))
print("Tamanho de",T,"=",sys.getsizeof(T)," bytes")

S = {'Maça', 'Laranja', 'Maça', 'Pera'}
print("Tamanho de",S,"=",sys.getsizeof(S)," bytes")

D = {'Nome': 'Joao', 'Idade': 24, 'Classe': 'Primeira'}
print("Tamanho de",D,"=",sys.getsizeof(S)," bytes")

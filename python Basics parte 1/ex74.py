#Write a Python program to hash a word.

a=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]

palavra=input("Escreva uma palavra para virar hash: ")

palavra=palavra.upper()

codigo=palavra[0]

for b in palavra[1:len(palavra)]:
    i=65-ord(b)
ent    codigo=codigo+str(a[i])
print("A palavra codificada é:",codigo)


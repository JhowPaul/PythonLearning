#Write a Python program to get a new string from a given string where "Is" has been added to the front.
#If the given string already begins with "Is" then return the string unchanged
def novo_texto(texto):
    if len(texto)>=2 and texto[:1]=="É": #checa se a letra na primeira posição é "É"
        return texto
    return "É"+texto

print(novo_texto("Garai"))
print(novo_texto("Évazio"))



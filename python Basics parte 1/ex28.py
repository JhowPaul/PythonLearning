#Write a Python program to print out a set containing all the colors from color_list_1 
#which are not present in color_list_2.

cor1=set(["Preto","Branco","Vermelho"])
cor2=set(["Vermelho","Verde"])

print(cor1.difference(cor2))
print(cor2.difference(cor1))

#OU
print(cor1-cor2)
print(cor2-cor1)
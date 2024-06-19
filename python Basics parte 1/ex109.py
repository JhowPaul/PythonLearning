#Write a Python program to get numbers divisible by fifteen from a list using an anonymous function

numero=[45,55,60,37,100,105,220]

resultado=list(filter(lambda x:(x%15==0),numero))
print("Numeros divisiveis por 15 são: ",resultado)
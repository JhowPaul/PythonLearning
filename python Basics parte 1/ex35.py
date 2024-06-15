#Write a Python program that will return true if the two given integer values 
#are equal or their sum or difference is 5

def somaDois(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True 
    else:
        return False

a=(eval(input("Digite o primeiro valor: ")))
b=(eval(input("Digite o segundo valor: ")))

print(somaDois(a,b))
print(somaDois(2,3))
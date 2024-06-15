#Write a Python program to find whether a given number (accept from the user) is even or odd, 
#print out an appropriate message to the user

def par_ou_impar(a):
    if a%2==0:
        print(f"O numero {a} é par")
    else:
        print(f"o numero {a} é impar")
        
numero=eval(input("digite um numero: ")); print(par_ou_impar(numero))

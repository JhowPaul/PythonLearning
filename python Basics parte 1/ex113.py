#Write a Python program to filter the positive numbers from a list. 

lista=[-10,1,2,3,-5,6]

nova_lista=list(filter(lambda x:x>0,lista))
nova_lista2=list(filter(lambda x:x<0,lista))
print("Os numeros positivos e negativos são",nova_lista,"\n",nova_lista2)
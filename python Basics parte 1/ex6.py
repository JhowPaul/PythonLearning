#Write a Python program to accept a filename from the user and print the extension of that.
arquivo=input("digite o nome do arquivo: ")
extensao=arquivo.split(".")

print(repr(f"a extensão do arquivo é :{extensao[-1]}  "))

#OU 
print ("The extension of the file is : " + repr(extensao[-1]))
#Write a Python program to prove that two string variables of same value point same memory location
frase1="Are we the last, living souls"
frase2="Are we the last, living souls"
print(id(frase1))
print(id(frase2))
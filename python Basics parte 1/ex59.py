#Write a Python program to convert height (in feet and inches) to centimeters
pes=eval(input("Insira uma medida em pés: "))
polegada=eval(input("Insira uma medida em polegadas: "))

polegada+=pes*12
centimetro=round(polegada*2.54,1)
print("Sua altura é: %d cm."%centimetro)
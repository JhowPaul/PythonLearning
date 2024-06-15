#Write a Python program to convert the distance (in feet) to inches, yards, and miles
pes=int(input("Coloque a distancia em pés: "))

polegada=pes*12
jarda=int(pes/3.0)
milha=pes/5280.0

print(f"a conversão de pés para polegadas foi:{polegada}")
print(f"a conversão de pés para jardas foi:{jarda}")
print(f"a conversão de pés para milha foi:{milha}")
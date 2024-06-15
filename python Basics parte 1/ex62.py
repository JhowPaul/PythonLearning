#Write a Python program to convert all units of time into seconds.
dia=int(input("Insira a quantidade de dias: "))*3600*24
hora=int(input("Insira as horas: "))*3600
minuto=int(input("Insira os minutos: "))*60
segundo=int(input("Insira os segundos: "))

tempo=dia+hora+minuto+segundo

print("Quantidade de segundos",tempo)
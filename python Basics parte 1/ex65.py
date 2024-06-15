#Write a Python program to convert seconds to day, hour, minutes and seconds

tempo=int(input("Insira os tempo em segundos: "))

dia=tempo//(24*3600)
tempo=tempo%(24*3600)
hora=tempo//3600
tempo%=3600
minuto=tempo//60
tempo%=60
segundos=tempo

print("Dia,hora,minuto e segundos → %d:%d:%d:%d"%(dia,hora,minuto,segundos))
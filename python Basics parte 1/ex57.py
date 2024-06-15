#Write a Python program to get execution time for a Python method.
import time

def soma(x):
    tempo_inicio=time.time()
    s=0
    for i in range(1,x+1):
        s+=i
    tempo_fim=time.time()
    return s,tempo_fim-tempo_inicio
x=5
print("\nTempo para somar 1 para",x,"e tempo requerido para calcular é: ",soma(x))
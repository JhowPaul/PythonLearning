#Write a Python program to create a histogram from a given list of integers.

def histograma(x):
    for i in x:
        saida=""
        tempo=i
        while(tempo>0):
            saida+='*'
            tempo-=1
        print(saida)

histograma([1,2,3,4,5])


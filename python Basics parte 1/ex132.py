#Write a Python program to calculate the time runs (difference between start and current time) 
#of a program

from timeit import default_timer


def timer(n):
    começo=default_timer()
    for sequencia in range(0,n):
        print(sequencia)
    print(default_timer()-começo)

timer(5)
timer(15)
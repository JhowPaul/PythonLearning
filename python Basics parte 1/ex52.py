#Write a Python program to print to stderr.
from __future__ import print_function
import sys

def printar(*args,**kwargs):
    print(*args,file=sys.stderr,**kwargs)

printar("abc","efg","xyz",sep="--")
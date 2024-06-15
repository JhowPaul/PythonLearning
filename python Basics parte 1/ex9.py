#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
a=5
def calcula(): #o simbolo % serve para concatenar strings
    n1,n2,n3 = int( "%s" % a ),int( "%s%s" % (a,a )),int("%s%s%s"%(a,a,a))
    
    print (n1+n2+n3)


calcula()


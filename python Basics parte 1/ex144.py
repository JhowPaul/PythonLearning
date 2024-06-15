#Write a Python program to test if a variable is a list or tuple or a set.

def checa_tipo(a):
    if type(a) is list:
        print("a é uma lista")
    elif type(a) is set:
        print("a é um set")
    elif type(a) is tuple:
        print("a é uma tupla")
    else:
        print("Não é uma lista nem tupla nem set")

b=("tuple",False,3.2,1)
c=["tuple",False,3.2,1]
d={"tuple",False,3.2,1}
e=100
(checa_tipo(b))
(checa_tipo(c))
(checa_tipo(d))
(checa_tipo(e))

#OU
def checa(nums):
    if isinstance(x, tuple)==True:
        return 'a variavel é uma tupla'
    elif isinstance(x, list)==True:
        return 'a variavel é uma lista'
    elif isinstance(x, set)==True:
        return 'a variavel é um set'
    else:
        return 'Não é uma lista nem tupla nem set.'
x = ['a', 'b', 'c', 'd']
print(checa(x))
x = {'a', 'b', 'c', 'd'}
print(checa(x))
x = ('tuple', False, 3.2, 1)
print(checa(x))
x = 100
print(checa(x))
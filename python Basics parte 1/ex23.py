#Write a Python program to test whether a passed letter is a vowel or not

def vogais(x):
    vogal="a,e,i,o,u"
    return x in vogal

print (vogais("a"))
print(vogais("z"))
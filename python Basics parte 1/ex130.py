#Write a Python program to split a variable length string into variables.

lista=["a","b","c"]
x,y,z=(lista+[None]*3)[:3] #separa cada variavel
print(x,y,z)

lista=[100,20.25]
x,y=(lista+[None]*2)[:2]
print(x,y)

#OU

# Initial String,
# must make obligatory Monty Python reference as nod to the language's origins
string="We are the nights who say... Ni!"
print(string)


# Technically can stop here as string has been converted to a list array
# with each element represented by a word
string_list=string.split(" ")
print(string_list)


# Looping through string_list defining x as the numerical index
for x in range(len(string_list)):
# Dynamically create x number of variables with names like var0, var1... etc
    globals()["var%s"%x]=string_list[x]
# Print said dynamic variables to make it clear they have been created
print("var%s ="%x,globals()["var%s"%x])
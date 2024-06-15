#Write a Python program to convert an integer to binary keep leading zeros.

a=12

b=a.bit_length()

print(format(a,"04b"))
print(format(a,"06b"))
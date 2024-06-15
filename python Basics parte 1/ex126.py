#Write a Python program to check whether an integer fits in 64 bits

valor=30
if valor.bit_length()<=63:
    print((-2**63).bit_length())
    print((2**63).bit_length())
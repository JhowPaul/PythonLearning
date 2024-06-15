#Write a Python program to list the special variables used within the language

print( '\n'.join(sorted( set(globals().keys()) | set(__builtins__.keys()) )) )

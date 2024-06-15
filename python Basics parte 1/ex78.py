#Write a Python program to find the available built-in modules
import sys
import textwrap

nomeModulo=','.join(sorted(sys.builtin_module_names))
print(textwrap.fill(nomeModulo,width=70))
#Write a Python program to get the command-line arguments 
#(name of the script, the number of arguments, arguments) passed to a script
import sys

print("Esse é o nome/destino do script:"),sys.argv[0]
print("Numero de argumentos:",len(sys.argv))
print("Lista de argumentos:",str(sys.argv))

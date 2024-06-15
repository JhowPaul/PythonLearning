#Write a Python program to access and print a URL's content to the console

from http.client import HTTPConnection

conecta=HTTPConnection("example.com")
conecta.request("GET","/")
resultado=conecta.getresponse()
conteudo=resultado.read()
print(conteudo)
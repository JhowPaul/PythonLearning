def jogar():
   
    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_','_','_','_','_','_',]
    enforcou = False
    acertou = False
    erro = 0
    while (not enforcou and not acertou):
        chute = input('digite uma letra: ')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
           index = 0
           for letra in palavra_secreta:

               if chute.upper() == letra.upper():
                   letras_acertadas [index] = letra
               index = index + 1
        else:
           erro = erro+1

        enforcou = erro == 6
        acertou	='_' not in	letras_acertadas
        print(letras_acertadas)
if __name__=='__main__':
   jogar()
print("Fim do jogo")
print("*****forca.py****************************")

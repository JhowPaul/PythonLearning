def jogar():

    palavra_secreta = "seila".upper()
    letras_acertadas=["-","-","-","-","-"]

    acertou=False
    enforcou=False
    erros=0
    print(letras_acertadas)

    while(not acertou and not enforcou):
    
        chute=input("digite uma letra: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
      
            posicao=0
            for letra in palavra_secreta:

                if(chute.upper() == letra.upper()):
                    
                    letras_acertadas[posicao]=letra
                    print("Encontrei a letra {} na posição {}".format(letra,posicao))
                posicao = posicao + 1
    
        else:
            erros=erros + 1
       
        enforcou = erros == 6
        acertou="-" not in letras_acertadas
        print(letras_acertadas)
if (__name__ == '__main__'):
    jogar()

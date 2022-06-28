
def jogar():

    print("*********************************")
    print("Bem vindo ao jogo da forca!")
    print("*********************************")


    palavra_secreta = "abacate".upper()
    letras_acertadas = ["_" for letras in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0


    while(not enforcou and not acertou):
        chute = input("Qual letra ?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index]= letra
                index = index + 1
        else:
            erros = erros + 1
            print("você errou acéfalo ! ainda falta {} tentativas!".format(6-erros))

        enforcou = erros == 4
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou!")
    else:
        print("você se enforcou")


if (__name__ == "__main__"):
    jogar()

import adivinhação
import forca

def escolhe_jogo():

    print("*********************************")
    print("****Escolha seu jogo!****")
    print("*********************************")

    print("forca (1) ou Adivinhação (2)")

    jogo = int(input("qual jogo!?"))

    if(jogo == 1 ):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2 ):
        print("jogando Adivinhação")
        adivinhação.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()


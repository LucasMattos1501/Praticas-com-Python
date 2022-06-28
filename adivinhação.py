def jogar():

    import random

    print("*********************************")
    print("Bem vindo ao jogo da adivinhação")
    print("*********************************")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    pontos = 1000

    print("Escolha a sua dificuldade")
    print("Fácil (1) Médio (2) Difícil (3)")

    Nível = int(input("Defina o Nível:"))
    if (Nível == 1 ):
        total_de_tentativas = 20
    elif (Nível == 2 ):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas +1 ):
        print("tentativa {} de {}".format( rodada, total_de_tentativas))

        chute_str = input("Digite seu número entre 1 e 100: ")

        print("você digitou ", chute_str)

        chute = int(chute_str)

        if ( chute < 1 or chute > 100):
            print("voce deve digitar um número entre 1 e 100")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if (acertou):
            print("você acertou animal e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Voce errou! o seu chute foi maior que o número secreto, corno!.")
            elif(menor):
                print("Voce errou! o seu chute foi menor que o número secreto, corno.")
            pontos_perdidos = abs(numero_secreto - chute)  #40-20 = 20
            pontos = pontos - pontos_perdidos


    print("fim de jogo")
if __name__ == "__main__":
    jogar()

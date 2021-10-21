import random
def advinhação():
    #Header
    print("-=-"*13)
    print("Bem vindo ao jogo de adivinhação")
    print("-=-"*13)

    #declaração das variaveis
    numero_secreto = random.randint(1,100)
    pontos = 1000

    #Validação da escolha de nivel
    while True:
        print("Qual dificuldade desejada?")
        option = int(input("(1) Facil  (2) Medio  (3) Dificil\n"))
        if (option in range(4)):
            break
        else:
            print("Valor invalido!")

    if (option == 1):
        num_de_tentativas = 10
    elif(option == 2):
        num_de_tentativas = 5
    else:
        num_de_tentativas = 3

    #laço para tentativas
    for i in range(num_de_tentativas):
        print(f"Tentativa: {i+1} de {num_de_tentativas}")
        #recebimento do numero secreto via console
        tentativa = int(input("Qual um número entre 1 e 100?\n"))
        pontos -= abs(tentativa-numero_secreto)
        
        print(f"sua pontuação atual é de {pontos}")

        if(1 > tentativa or tentativa > 100):
            print("Valor invalido: Digite um valor entre 1 e 100")
            continue

        #resposta ao usuario, sobre qual numero digitado
        print(f"voce digitou o numero: {tentativa}")

        #Chute correto
        if(numero_secreto == tentativa):
            print(f"voce acertou e ganhou com {pontos}!!!")
            break;
        else:
            print("voce errou!!!")
            if(numero_secreto < tentativa):
                #chute maior que o valor secreto
                print("Seu chute foi maior que o numero secreto!\n")
            else:
                #chute menor que o valor secreto
                print("Seu chute foi menor que o numero secreto!\n")
    #Footer
    print("Fim do jogo, obrigado por jogar!!")
    print("-=-"*13)

#main
if __name__ == '__main__':
    advinhação()
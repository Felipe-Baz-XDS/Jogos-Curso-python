import random

def Header():
    print("-=-"*13)
    print("Bem vindo ao jogo de forca")
    print("-=-"*13)

def forca():

    Header()

    #manipulação de arquivos
    #Abertura do arquivo
    with open("/home/felipe/Desktop/python 3 parte 1/palavras.txt", "r") as arq:
        palavras = []

        #preenchimento da lista, ja formatada
        for linha in arq:
            palavras.append(linha.strip().lower())
        
    #escolha da palavra
    palavra_secreta = random.choice(palavras)
    
    #declaração das variaveis
    vivo = False
    vitoria = False
    tentativas = 0

    #list comprehension para criação da lista de lacunas
    lista_palavra = ["_" for letra in palavra_secreta]

    #impressão da lista
    print(lista_palavra)

    #laço da gameplay
    while (not vivo and not vitoria):

        #inicialização do index
        index = 0

        #recebimento da tentativa/chute do player
        tentativa = str(input("Escolha uma letra:\n")).lower().strip()
        
        #validação de acerto
        if (tentativa in palavra_secreta):
            for letra in palavra_secreta:
                if(tentativa == letra):
                    lista_palavra[index] = letra
                index += 1
        #validação erro
        else:
            tentativas += 1 
            print(f"Voce errou! vidas:{6-tentativas}")
        
        #caso de derrota
        vivo = tentativas == 6
        #Caso de vitoria
        vitoria = "_" not in lista_palavra
        
        #impressão da lista
        print(lista_palavra)

    #Footer
    print("Fim do jogo, obrigado por jogar!!")
    print("-=-"*13)

#main
if __name__ == "__main__":
    forca()

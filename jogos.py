import forca
import adivinhação

def escolhe_game():
    #Header
    print("-=-"*13)
    print("Escolha seu jogo:")
    print("-=-"*13)

    while True:
        option = int(input("(1) Adivinhação   (2) Forca   (3) Sair\n"))
        if(option == 1):
            adivinhação.advinhação()
        elif(option == 2):
            forca.forca()
        else:
            break

    #Footer
    print("Fim do jogo, obrigado por jogar!!")
    print("-=-"*13)

#main
if __name__ == '__main__':
    escolhe_game()
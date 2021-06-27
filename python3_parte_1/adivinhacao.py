import random
...
## Resto do código

def jogar():
    print("*"*49)
    print("*"*6, " BEM-VINDO AO JOGO DA ADIVINHAÇÃO! ", "*"*6, "\n")
    print("*"*49)
    print()

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0

    pontos = 1000

    print("Em qual o nível de dificuldade deseja jogar? ")
    print(" (1) Fácil\n (2) Médio\n (3) Difícil\n")

    nivel = int(input("Escolha o nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    elif (nivel == 3):
        total_de_tentativas = 5
    else:
        print("O número digitado não corresponde a um nível. Tente novamente.")

    for rodada in range(1, total_de_tentativas + 1): # podemos usar aqui o while ao invés do for, da seguinte forma: while(rodada <= total_de_tentativas):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f"Você acertou!!! E fez {pontos} pontos!")
            break
        else:
            if (maior):
                print("Você errou. O seu chute foi maior do que o número secreto.")
            elif (menor):
                print("Você errou. O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute)
                pontos = pontos - pontos_perdidos
    
    print()
    print("********************")
    print("*** Fim do jogo. ***")
    print("********************")

if (__name__ == "__main__"):
    jogar()

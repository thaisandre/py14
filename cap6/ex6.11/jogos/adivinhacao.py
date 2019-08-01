def jogar():
    imprime_mensagem_de_abertura()

    numero_secreto = 42
    total_de_tentativas = 3
    rodada = 1

    for rodada in range(1, total_de_tentativas+1):
        imprime_total_de_tentativas(rodada, total_de_tentativas)

        chute = pede_chute()
        imprime_chute(chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            imprime_mensagem_vencedor()
            break
        elif (maior):
            imprime_mensagem_perdedor_com_chute_maior()
        elif (menor):
            imprime_mensagem_perdedor_com_chute_menor()

    print('Fim do jogo!')

def imprime_mensagem_de_abertura():
    print('******************************')
    print('*    Jogo da adivinhação     *')
    print('******************************')

def imprime_total_de_tentativas(rodada, total_de_tentativas):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

def pede_chute():
    chute = int(input('Digite o seu número: '))
    return chute

def imprime_chute(chute):
    print('Você digitou: ', chute)

def imprime_mensagem_vencedor():
    print('Você acertou!')

def imprime_mensagem_perdedor_com_chute_maior():
    print('Você errou! O seu chute foi maior que o número secreto')

def imprime_mensagem_perdedor_com_chute_menor():
    print('Você errou! O seu chute foi menor que o número secreto')
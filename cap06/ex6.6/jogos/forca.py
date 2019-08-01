import random

def jogar():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)

    acertou = False
    enforcou= False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[posicao] = letra.upper()
                posicao = posicao + 1
        else:
            erros += 1

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas            
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!!')
    else:
        print('Você perdeu!!')
    print('Fim do jogo')


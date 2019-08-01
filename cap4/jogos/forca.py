print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']

acertou = False
enforcou= False
erros = 0

print(letras_acertadas)

while(not enforcou and not acertou):

    chute = input("Qual letra? ")

    if(chute.upper() in palavra_secreta.upper()):
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


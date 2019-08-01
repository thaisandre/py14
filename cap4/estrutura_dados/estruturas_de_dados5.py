# EX-5 - Utilize o exercício anterior e adicione a pessoa em uma lista. Pergunte a
# o usuário se ele deseja adicionar uma outra pessoa. Após adicionar dados de algumas 
# pessoas, você deve imprimir todos os dados de cada pessoa de forma organizada.

deseja_adicionar_outra = True

pessoas = []

while(deseja_adicionar_outra):

    # lendo os dados de entrada do usuário
    nome = input('Digite o nome da pessoa: ')
    idade = input('Digite a idade da pessoa: ')
    cidade = input('Digite a cidade onde a pessoa mora: ')
    print()

    # construindo um dict (dicionário) com os dados:
    pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}

    # adicionando os dados da pessoa na lista de pessoas
    pessoas.append(pessoa)

    # pergunta se deseja adionar mais dados de pessoas
    resposta = input('Deseja adicionar dados de outra pessoa? (S/N): ')
    if resposta == 'S' or resposta == 's':
        deseja_adicionar_outra = True
    if resposta == 'N' or resposta == 'n':
        deseja_adicionar_outra = False
    print()


# mostrando os dados
print('\nPessoas cadastradas:')
for pessoa in pessoas:
    for chave, valor in pessoa.items():
        print('{}: {}'.format(chave, valor))
    print()
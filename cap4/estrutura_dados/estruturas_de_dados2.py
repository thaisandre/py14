# EX-2 - Faça um programa que leia os dados do usuário (nome, sobrenome, idade), adicione
# em uma lista e imprima seus elementos

# pegando os dados de entrada do usuário
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')

# adicionando os dados em uma lista
dados = []
dados.append(nome)
dados.append(sobrenome)
dados.append(idade)

# imprime os dados da lista
print('\nImprimindo os dados:')
for dado in dados:
    print(dado)

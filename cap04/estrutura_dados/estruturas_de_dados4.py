# EX-4 - Faça um programa utilizando um dict que leia dados de entrada do usuário. O usuário
# deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora (fique livre para 
# acrescentar outros). Após isso, você deve imprimir os dados como o exemplo abaixo:
#
#   nome: João
#   idade: 20
#   cidade: São Paulo

# lendo os dados de entrada do usuário
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
cidade = input('Digite a cidade onde mora: ')
print()

# construindo um dict (dicionário) com os dados:
dados = {'nome': nome, 'idade': idade, 'cidade': cidade}

# mostrando os dados
for chave, valor in dados.items():
    print('{}: {}'.format(chave, valor))
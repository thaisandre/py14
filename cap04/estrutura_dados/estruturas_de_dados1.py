# EX-1

lista = [12, -2, 4, 8, 29, 45, 78, 36, -7, 2, 12, 8, 3, 3, -52]

# letra a - imprime maior elemento
print('O maior elemento da lista é {}\n'.format(max(lista)))


# letra b - imprime menor elemento
print('O menor elemento da lista é {}\n'.format(min(lista)))


# letra c - imprime todos os números paras
print('Números pares:')
for elemento in lista:
    if elemento % 2 == 0:
        print(elemento)
print()


# letra d - imprime o número de ocorrências do primeiro elemento da lista
print('Número de ocorrências do número {}: {}\n'.format(lista[0], lista.count(lista[0])))


# letra e - imprime a média dos elementos
soma_dos_elementos = 0

for elemento in lista:
    soma_dos_elementos = soma_dos_elementos + elemento

media = soma_dos_elementos / len(lista)
print('A média dos elementos da lista é: {}\n'.format(media))


# letra f - impria a soma dos elementos de valor negativo
soma = 0

for elemento in lista:
    if(elemento < 0):
        soma = soma + elemento

print('A soma dos elementos negativos da lista é: {}'.format(soma))





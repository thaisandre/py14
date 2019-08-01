# EX-3 - Faça um programa que leia 4 notas, mostre as notas e a média na tela

# lendo as notas
nota1 = float(input('Nota da prova1: '))
nota2 = float(input('Nota da prova2: '))
nota3 = float(input('Nota da prova3: '))
nota4 = float(input('Nota da prova4: '))
print()

# imprimindo as notas
notas = [nota1, nota2, nota3, nota4]

for i in range(0, len(notas)):
    print('nota{}: {}'.format(i+1, notas[i]))
print()

# calcula e imprime a média das notas
media = sum(notas) / len(notas)
print('A média das notas é: {}'.format(media))

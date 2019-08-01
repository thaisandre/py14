# EX-5

# definindo a função velocidade_media
def velocidade_media(distancia, tempo):
    velocidade = distancia/tempo
    return velocidade

print('\nVelocidades médias: ')
# distância=100 e tempo=20
print(velocidade_media(100, 20))

# distância=150 e tempo=22
print(velocidade_media(150, 22))

# distância=200 e tempo=30
print(velocidade_media(200, 30))

# distância=50 e tempo=3
print(velocidade_media(50, 3))


# definindo a função soma
def soma(num1, num2):
    return num1+num2

def subtracao(num1, num2):
    return num1-num2

def multiplicacao(num1, num2):
    return num1*num2

def divisao(num1, num2):
    return num1/num2

def calculadora(num1, num2):
    return soma(num1, num2), subtracao(num1, num2), multiplicacao(num1, num2), divisao(num1, num2)

print('\nOperações aritméticas: ')
print(calculadora(2, 3))
print(calculadora(4, 2))
print(calculadora(2, 5))
print(calculadora(5, 9))





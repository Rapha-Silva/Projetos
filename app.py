import random
num = int(input('Escolha e digite um número de 0 e 5:  '))
random.randint(0, 5)
if num == random.randint(0, 5):
    print('Parabéns você acertou!')
else:
    print('Há... você errou, tente novamente!!')

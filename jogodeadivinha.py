from random import randint
import time
computador = randint(0, 5) #faz o computador pensar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei:  ')) # Usuário escolhe o número
print('PROCESSANDO...')
time.sleep(2)
if num == computador:
    print('Parabéns você acertou, conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, num))
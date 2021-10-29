# 32 - faça o programa que leia um ano qualqer e vê se ele é bissexto.
from datetime import date
print('Vamos descobrir se o ano que você digitou é BISSEXTO')
ano = int(input('Digite um ano ou coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('Com certeza o ano {} é BISSEXTO!! '.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
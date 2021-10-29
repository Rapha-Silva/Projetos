'''31 - Prog. que pergunte o preço de uma viagem em km. Cal o preço da passagem, cobrando 0.50 por km para viagens de até 200km e 0.45 para viagens mais longas.'''
distância = float(input('Qual é a distância da sua viagem ?? '))
print('Você está prestes a começar uma viagem de {} km'.format(distância))
if distância < 200:
    preço = (distância * 0.50)
    print('Sua passagem vai custar R${:.2f}'.format(preço))
else:
    preço2 = distância * 0.45
    print('Sua passagem vai custar R${:.2f}'.format(preço2))
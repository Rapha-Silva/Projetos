velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 110: #condição simples porque não tem else.
    print('MULTADO! Você excedeu o limite da via de 110km/h')
    multa = (velocidade-110)*7
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))
print('Tenha um bom dia e dirija com seguança! ')
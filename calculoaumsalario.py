''' 34 - Escreva um programa que pergunte o salário do funcionário e calc o valor de seu aumento. Para sal sup a 1250,00 aumento d 10 % para inf ou iguais aumento de 15%'''
salario = float(input('Qual o salário do funcionário: '))
if salario <= 1250:
    aumento =  salario + (salario * 15 / 100)
else:
    aumento = salario + ( salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar um salário de R${aumento:.2f}')
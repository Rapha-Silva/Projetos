# 35 - Escr. um prog. que q leia o compare 3 retas e se elas podem ou não formar um triângulo.
print('-=-'*10)
print('Analisador de triângulos')
print('-=-'*10)
r1 = float(input('Primeiro valor: '))
r2 = float(input('Segundo valor: '))
r3 = float(input('Terceiro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('É possível formar um triângulo com {} {} {}'.format(r1, r2, r3 ))
else:
    print('Não é possível formar um triângulo')
    
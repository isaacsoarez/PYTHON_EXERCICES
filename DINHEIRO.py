print('CALCULO DE DESCONTOS')

valor = float(input('Digite o valor do produto:'))

print('Descrubra as formas de pagamento e suas variações de preço')

a1 = (valor)-valor*10/100
print('A vista no dinheiro ou no cheque você tem 10%off=R$', a1)

a2 = (valor)-valor*5/100
print('A vista no cartão você tem 5%off=R$', a2)

print('Em até 2x no cartão você não possui desconto=R$',valor)

a3 = (valor)+valor*20/100
print('Em até 3x no cartão você paga 20% de juros=R$',a3)

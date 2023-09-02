n1= float(input('Digite o valor do primeiro produto:'))
n2= float(input('Digite o valor do segunfo produto:'))
n3= float(input('Digite o valor do terceiro produto:'))

if n1<=n2 and n1<=n3 :
    print('Você deve comprar o 1ºproduto, no valor de:', n1)
elif n2<=n1 and n2<=n3 :
    print('Você deve comprar o 2ºproduto, no valor de:', n2)
else:
    print('Você deve comprar o 3ºproduto, no valor de:', n3)
n1= int(input('Digite um número de sua escolha:'))
n2= int(input('Digite outro número de sua escolha:'))
n3= int(input('Digite outro número de sua escolha:'))

if n1<=n2 and n1<=n3 :
    print('O menor número é 0 1º:', n1)
elif n2<=n1 and n2<=n3 :
    print('O menor número é o 2º:', n2)
else:
    print('O menor número é o 3º:', n3)
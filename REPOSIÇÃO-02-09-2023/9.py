n1 = int(input('Digite um número de sua escolha: '))
n2 = int(input('Digite outro número de sua escolha: '))
n3 = int(input('Digite outro número de sua escolha: '))

if n1 >= n2 and n2 >= n3:
    print('A ordem decrescente é:', n1, n2, n3)
elif n1 >= n3 and n3 >= n2:
    print('A ordem decrescente é:', n1, n3, n2)
elif n2 >= n1 and n1 >= n3:
    print('A ordem decrescente é:', n2, n1, n3)
elif n2 >= n3 and n3 >= n1:
    print('A ordem decrescente é:', n2, n3, n1)
elif n3 >= n1 and n1 >= n2:
    print('A ordem decrescente é:', n3, n1, n2)
else:
    print('A ordem decrescente é:', n3, n2, n1)
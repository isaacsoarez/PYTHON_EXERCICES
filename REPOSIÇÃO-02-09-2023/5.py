n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
n3 = float(input('Digite sua terceira nota:'))
media = (n1 + n2 + n3)/3
print('sua média é =', media)

if media >= 7:
    print('Aprovado')
elif media >= 10: 
    print('F - Aprovado com Distinção')
elif media <7:
    print('Reprovado')
else:
    print('Inválido')

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
media = float(n1 + n2) / 2

print('Sua primeira nota é:', n1)
print('Sua segunda nota é:', n2)
print('Sua média é:', media)

if media < 7:
    print('Você foi reprovado')

elif media >= 7:
    print('Você foi aprovado')
    
if media >= 9.5:
    print('Você foi aprovado com distinção')

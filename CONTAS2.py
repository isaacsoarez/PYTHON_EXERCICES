n1= float(input('Digite um número inteiro de sua escolha:'))
n2= float(input('Digite outro número inteiro de sua escolha:'))

sub= n1-n2

mut= n1*n2

div= n1/n2
print('Os números escolhidos foram:',n1,'e',n2)

resultadosub=float(input('Digite a subtração dos números'))

resultadomut=float(input('Digite a mutiplicação dos números'))

resultadosdiv=float(input('Digite a divisão dos números'))

if resultadosub != sub:
    print('Resultado Errado')
elif resultadomut != mut:
    print('Resultado Errado')
elif resultadosdiv != div:
    print('Resultado Errado')
else:
    print('Resultado Correto')

print('Os resultados corretos devem')
print('A subtração dos números é:', sub)
print('A mutiplicação dos números é:', mut)
print('A divisão dos números é:', div)



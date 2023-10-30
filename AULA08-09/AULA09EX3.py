#Faça um programa que solicite dois números ao usuário e exiba a multiplicação deles.
#A multiplicação deve ser calculada em uma função lambda.

#-------------------------------SEM LAMBDA-------------------------------------


#numero_primario = int(input('Digite um número:'))
#numero_secundario = int(input('Digite outro número:'))
#calcular_mutiplicacao_dois = numero_primario * numero_secundario


#print(f'A mutiplicação entre os números é: {calcular_mutiplicacao_dois}')

#------------------------------COM LAMBDA--------------------------------------
numero_primario = int(input('Digite um número: '))
numero_secundario = int(input('Digite outro número: '))

calcular_multiplicacao = lambda a, b: a * b

resultado = calcular_multiplicacao(numero_primario, numero_secundario)

print(f'A multiplicação entre os números é: {resultado}')



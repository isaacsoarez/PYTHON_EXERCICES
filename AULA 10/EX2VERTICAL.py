numero = str(input('Digite um número com mais de 2 algarismos'))

numeros = numero.split()

for numero in numeros:
    print(f'{numero}')
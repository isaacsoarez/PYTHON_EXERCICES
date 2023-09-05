numeros = []

for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)
soma = sum(numeros)

multiplicacao = 1
for numero in numeros:
    multiplicacao *= numero

print("Os números digitados são:", numeros)

print(f"A soma dos números é: {soma}")
print(f"A multiplicação dos números é: {multiplicacao}")
#auxilio da internet com SUM
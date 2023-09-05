armazenamento = []
par = []
impar = []

for i in range(20):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    armazenamento.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print("Números armazenados:", armazenamento)
print("Números pares:", par)
print("Números ímpares:", impar)
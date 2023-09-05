reais = []

for i in range(10):
    numero_real = float(input(f"Digite o {i + 1}º número real: "))
    reais.append(numero_real)

reaisinvertidos = reais[::-1]

print("Os números digitados em ordem inversa foram:", reaisinvertidos)
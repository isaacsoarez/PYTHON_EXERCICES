soma = 0
contador = 0

numero = float(input("Digite as notas que são utilizadas para média(Após adicione qualquer valor negativo para fazer o calculo):"))

while numero >= 0:
    soma += numero
    contador += 1
    numero = float(input("Digite as notas que são utilizadas para média(Após adicione qualquer valor negativo para fazer o calculo):"))
if contador > 0:
    media = soma / contador
    print(f"A média dos números inseridos é: {media:.2f}")
else:
    print("Nenhum número válido foi inserido.")

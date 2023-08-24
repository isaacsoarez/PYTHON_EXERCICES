soma = 0
contador = 0

numero = float(input("Digite números para descobrir a soma(Após inserir adicione 0 para fazer o calculo):"))

while numero >= 1:
    soma += numero
    contador += 1
    numero = float(input("Digite números para descobrir a soma(Após inserir adicione 0 para fazer o calculo):"))

if contador > 0:

    print(f"A soma dos números inseridos é: {soma:.2f}")
else:
    print("Nenhum número válido foi inserido.")
soma = 0
contador = 0

numero = float(input("Digite os valores dos produtos comprados(Após inserir, adicione 0 para fazer o cálculo):"))

while numero >= 1:
    soma += numero
    contador += 1
    desconto = soma*0.1
    numero = float(input("Digite os valores dos produtos comprados(Após inserir, adicione 0 para fazer o cálculo):"))

if contador > 0:
    print(f"O valor da compra é: {soma:.2f}")
if soma >=1000:
    print('Você recebeu 10%Off:', soma-desconto)

else:
    print("Nenhum número válido foi inserido.")

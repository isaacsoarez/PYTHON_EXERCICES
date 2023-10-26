def positivo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

numero = int(input("Digite um número: "))
resultado = positivo(numero)
print(f"O resultado é: {resultado}")

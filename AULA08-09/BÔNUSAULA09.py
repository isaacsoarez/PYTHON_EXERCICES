def temperatura(temp):
    if temp == 1:
        return f'A área do terreno é: {temp}m²'
    elif temp == 2:
        return f'A área do terreno é: {temp}m²'

    elif temp ==3:
        return f'A área do terreno é: {temp}m²'

    else:
        return 'Não foi possível contabilizar a área de'

temp = int(input("Escolha a temperatura que deseja descobrir: 1-CELCIUS/2-KELVIN/3-FAHRENHEIT"))

temperatura_celcius = int(input("Digite a temperatura em CELCIUS:"))
temperatura_kelvin = int(input("Digite a temperatura em KELVIN:"))
temperatura_firen = int(input("Digite a temperatura em FAHRENHEIT"))





resultado = temperatura(temp)

print(f"O resultado é: {resultado}")

def consultaarea(area):
    if area > 0:
        return f'A área do terreno é: {area}m²'
    else:
        return 'Não foi possível contabilizar a área de'

largura = int(input("Digite a largura do terreno(em metros): "))
altura = int(input("Digite a altura do terreno(em metros): "))
area= largura*altura
resultado = consultaarea(area)
print(f"O resultado é: {resultado}")

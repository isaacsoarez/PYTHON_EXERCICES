#Faça um programa que solicite cinco números ao usuário, depois disso, exiba apenas
#os números maiores do que 10. Utilize a função filter para fazer isso..

def maior(numero):
    if numero > 10:
        return f'{numero}'
    else:
        return ''

numero = int(input("Digite um número: "))
resultado = maior(numero)

def maior(numero):
    if numero > 10:
        return f'{numero}'
    else:
        return ''

numero = int(input("Digite outro número: "))
resultado2 = maior(numero)

def maior(numero):
    if numero > 10:
        return f'{numero}'
    else:
        return ''

numero = int(input("Digite outro número: "))
resultado3 = maior(numero)

def maior(numero):
    if numero > 10:
        return f'{numero}'
    else:
        return ''

numero = int(input("Digite outro número: "))
resultado4 = maior(numero)

def maior(numero):
    if numero > 10:
        return f'{numero}'
    else:
        return ''

numero = int(input("Digite outro número: "))
resultado5 = maior(numero)

print(f"Os números maior que 10 são: [{resultado}], [{resultado2}], [{resultado3}], [{resultado4}], [{resultado5}]")
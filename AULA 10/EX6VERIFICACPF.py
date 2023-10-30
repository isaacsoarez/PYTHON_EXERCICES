def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11:
        return False

    soma = 0
    peso = 10
    for digito in cpf[:9]:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto

    soma = 0
    peso = 11
    for digito in cpf[:10]:
        soma += int(digito) * peso
        peso -= 1
    resto = soma % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto

    return int(cpf[9]) == digito_verificador1 and int(cpf[10]) == digito_verificador2

cpf = input("Digite o CPF no formato 11 digitos: ")

if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")

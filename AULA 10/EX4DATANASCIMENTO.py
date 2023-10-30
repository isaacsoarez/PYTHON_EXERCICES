data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = map(int, data_nascimento.split('/'))

nomes_meses = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
    'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
]

if 1 <= mes <= 12:
    nome_mes_extenso = nomes_meses[mes - 1]
    print(f"A data de nascimento com o nome do mês por extenso é: {dia} de {nome_mes_extenso} de {ano}")
else:
    print("Mês inválido. Certifique-se de inserir um mês entre 1 e 12.")

bancos = ['Banco do Brasil', 'Caixa', 'Santander']
print(bancos)
bancos[1] = 'Itau'
print(bancos)
bancos[-1] = 'C6'
print(bancos)

lista = []
for i in range(3):
    banco_digitado = input(f"Digite o {i + 1}º banco: ")
    lista.append(banco_digitado)

print('Bancos Digitados:')
print(lista)




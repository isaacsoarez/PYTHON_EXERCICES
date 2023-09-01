lista = []
qtd = int(input('Digite quantos números quer inserir na lista:'))
if qtd== 0:
    for i in range(qtd):
        qtd_digitado = input(f"Digite o {i + 1}º número: ")
        lista.append(qtd)
    print(f"O número escolhidos foram: {lista}")
lista = []
qtd = int(input('Digite quantos números quer inserir na lista em ordem crescente:'))
if qtd== 0:
    for i in range(qtd):
        qtd_digitado = input(f"Digite o {i + 1}º número: ")
        lista.append(qtd_digitado)
    print(f"O número escolhidos foram: {lista}")
    for ele in lista:
        if ele % 2 == 0:
            lista.remove(ele)
    print(f"Os números pares são")

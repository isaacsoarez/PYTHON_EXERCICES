print('-----BEM VINDO A SHOES ONLINE-----')
print('-------------------------------------')
#variaveis de informação que serão utilizadas para entrada e saída do programa
nome = str(input('Digite o nome do cliente:'))
cpf = str(input('Digite o CPF do cliente:'))
vendedor = str(input('Digite o nome do vendedor:'))
print('-------------------------------------')
#declaração de variavel para uso seguinte em calculo
qtd = int(input('Digite quantos calçados foram comprados:'))
soma = 0

#lista criada para armarzenar dados dos calçados
lista = []
for i in range(qtd):
    qtd_digitado = float(input(f"Digite o valor do {i + 1}º calçado: "))
    lista.append(qtd_digitado)
    #leitura da lista
    print(f"Os preços dos produtos são : R$ {lista}")
    #calculo de contador citado la em cima
    soma += qtd_digitado

#variaveis para calculos de descontos, frete e comissao do vendedor
acimade200 = float(input('Digite o valor do desconto em forma decimal(ex:0.1)'))
acimade200a = acimade200*soma
frete = soma*0.03
comissão = soma*0.04
print('-------------------------------------')
print('*CASO DIGITE DESCONTO COM VALOR TOTAL INFERIOR A R$200, O DESCONTO NÃO SERÁ APLICADO*')
print('-------------------------------------')


#POSSIBILIDADES
#se compra final for maior de 200 reais o comprador tem seus dados citados e informaões expostas(desconto e frete)
if soma >= 200:
    
    print('-------------------------------------')
    print(f'Caro(a), {nome} portador do cpf {cpf} você ganhou frete grátis e Desconto')
    print(f'-----Valor S/ desconto: R${soma}')
    print(f'-----Valor final da compra é de: R${soma-frete-acimade200a}')
    print('-------------------------------------')
    print(f'A comissão(4%) de {vendedor} é de: R${comissão}')
    print('-------------------------------------')
    print(f'Descontos: Frete= R${frete}/%OFF= R${acimade200a}')

#se compra final for maior de 100 reais o comprador tem seus dados citados e informaões expostas(desconto)
elif soma >=100:
        print('-------------------------------------')
        print(f'Caro(a), {nome} portador do cpf {cpf} você ganhou frete grátis')
        print(f'-----Valor S/ desconto: R${soma}')
        print(f'-----Valor final da compra é de: R${soma-frete}')
        print('-------------------------------------')
        print(f'A comissão(4%) de {vendedor} é de: R${comissão}')
        print('-------------------------------------')
        print(f'Descontos: Frete= R${frete}')

#se compra final for maior de 10 reais o comprador tem seus dados citados e informaões expostas
elif soma >=10:
            print('-------------------------------------')
            print(f'-----Caro(a), {nome} portador do cpf {cpf} você não ganhou nenhum Desconto')
            print(f'-----Valor final da compra é de: R${soma}')
            print('-------------------------------------')
            print(f'A comissão(4%) de {vendedor} é de: R${comissão}')
            print('-------------------------------------')
            print(f'Descontos: Nenhum')

#caso a compra seja menor de 10 reais nao sera possivel efetuar pagamento
else:
    print('Compra Inválida')    

#deve ler o preço original da roupa, o desconto aplicado e o valor do frete.
#deve calcular o preço final da compra.
#deve ler o nome e cpf do cliente.
#deve ler o nome do vendedor.
#deve exibir o produto, preço, cliente e vendedor final da compra.
#deve ser todo comentado de como foi realizada a lógica para chegar no resultado final
#11:00 faremos a correção do programa em formato de apresentação com algumas duplas.
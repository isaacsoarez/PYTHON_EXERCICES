def pagamento(valor_prestacao, dias_atraso):
    if dias_atraso <= 0:
        return prestacao
    else:
        multa = prestacao * 0.03  
        juros = prestacao * (0.001 * dias_atraso)
        valor_total = valor_prestacao + multa + juros
        return valor_total

prestacoes = 0
valor_total = 0

while True:
    prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
    if prestacao == 0:
        break

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    pagar = pagamento(prestacao, dias_atraso)

    print(f"Valor a ser pago: R${pagar:.2f}")
    
    prestacoes += 1
    valor_total += pagar

print(f"Relatório do dia:")
print(f"Quantidade de prestações pagas: {prestacoes}")
print(f"Valor total pago: R${valor_total:.2f}")

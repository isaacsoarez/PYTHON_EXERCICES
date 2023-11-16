class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print(f"Ingresso comum - Valor: R$ {self.valor:.2f}")


class IngressoVIP(Ingresso):
    def __init__(self, valor, valor_adicional):
        super().__init__(valor)
        self.valor_adicional = valor_adicional

    def valor_total_vip(self):
        return self.valor + self.valor_adicional


# Programa principal
valor_ingresso_comum = 50.00
valor_adicional_vip = 20.00

ingresso_comum = Ingresso(valor_ingresso_comum)
ingresso_vip = IngressoVIP(valor_ingresso_comum, valor_adicional_vip)

print("Detalhes do Ingresso Comum:")
ingresso_comum.imprimir_valor()

print("\nDetalhes do Ingresso VIP:")
print(f"Ingresso VIP - Valor: R$ {ingresso_vip.valor_total_vip():.2f}")

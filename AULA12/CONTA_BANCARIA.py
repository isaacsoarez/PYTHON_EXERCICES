class ContaBancaria:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class ContaImposto(ContaBancaria):
    def __init__(self, cliente, saldo=0, percentual_imposto=0.1):
        super().__init__(cliente, saldo)
        self.percentual_imposto = percentual_imposto

    def calcular_imposto(self):
        imposto = self.saldo * self.percentual_imposto
        self.saldo -= imposto
        print(f"Imposto de R$ {imposto:.2f} aplicado. Novo saldo: R$ {self.saldo:.2f}")


# Programa principal
cliente = input("Digite o nome do cliente: ")

conta = ContaBancaria(cliente, float(input("Digite o saldo inicial da conta: ")))

conta.depositar(float(input("Digite o valor a ser depositado: ")))
conta.sacar(float(input("Digite o valor a ser sacado: ")))
conta.consultar_saldo()

print("\nOperações na Conta com Imposto:")

percentual_imposto = float(input("Digite o percentual de imposto para a conta com imposto (em decimal): "))
conta_imposto = ContaImposto(cliente, float(input("Digite o saldo inicial da conta com imposto: ")), percentual_imposto)

conta_imposto.depositar(float(input("Digite o valor a ser depositado na conta com imposto: ")))
conta_imposto.sacar(float(input("Digite o valor a ser sacado da conta com imposto: ")))
conta_imposto.calcular_imposto()
conta_imposto.consultar_saldo()

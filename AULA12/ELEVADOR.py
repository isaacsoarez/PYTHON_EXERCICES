class Elevador:
    def __init__(self, capacidade, total_andares):
        self.__andar_atual = 0
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presentes = 0

    def entrar(self):
        if self.__pessoas_presentes < self.__capacidade:
            self.__pessoas_presentes += 1
            print("Uma pessoa entrou no elevador.")
        else:
            print("Elevador cheio. Não é possível entrar mais pessoas.")

    def sair(self):
        if self.__pessoas_presentes > 0:
            self.__pessoas_presentes -= 1
            print("Uma pessoa saiu do elevador.")
        else:
            print("Elevador vazio. Não é possível sair mais pessoas.")

    def subir(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
            print(f"Elevador subiu para o andar {self.__andar_atual}.")
        else:
            print("Elevador já está no último andar. Não é possível subir mais.")

    def descer(self):
        if self.__andar_atual > 0:
            self.__andar_atual -= 1
            print(f"Elevador desceu para o andar {self.__andar_atual}.")
        else:
            print("Elevador já está no térreo. Não é possível descer mais.")

    def get_andar_atual(self):
        return self.__andar_atual

    def set_andar_atual(self, andar):
        if 0 <= andar <= self.__total_andares:
            self.__andar_atual = andar
        else:
            print("Andar inválido.")

    def get_total_andares(self):
        return self.__total_andares

    def set_total_andares(self, total_andares):
        if total_andares > 0:
            self.__total_andares = total_andares
        else:
            print("Número de andares inválido.")

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, capacidade):
        if capacidade > 0:
            self.__capacidade = capacidade
        else:
            print("Capacidade inválida.")

    def get_pessoas_presentes(self):
        return self.__pessoas_presentes

    def set_pessoas_presentes(self, pessoas_presentes):
        if 0 <= pessoas_presentes <= self.__capacidade:
            self.__pessoas_presentes = pessoas_presentes
        else:
            print("Número de pessoas inválido.")


def main():
    capacidade = int(input("Digite a capacidade do elevador: "))
    total_andares = int(input("Digite o número total de andares do prédio (desconsiderando o térreo): "))

    elevador = Elevador(capacidade, total_andares)

    while True:
        print("\nEscolha uma opção:")
        print("1 - Entrar no elevador")
        print("2 - Sair do elevador")
        print("3 - Subir um andar")
        print("4 - Descer um andar")
        print("0 - Sair do programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            elevador.entrar()
        elif opcao == '2':
            elevador.sair()
        elif opcao == '3':
            elevador.subir()
        elif opcao == '4':
            elevador.descer()
        elif opcao == '0':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

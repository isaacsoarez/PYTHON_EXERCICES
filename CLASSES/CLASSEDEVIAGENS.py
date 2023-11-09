class Cadastro:
    def __init__(self):
        self.nome = input('Digite seu nome: ')
        self.idade = int(input('Digite sua idade: '))
        self.cpf = int(input('Digite seu CPF: '))


destinos = ["Rússia", "Ucrânia", "Afeganistão", "Iraque", "Gaza"]

viajante = Cadastro()

escolha_destino = int(input(f'Escolha seu destino: [1]{destinos[0]} [2]{destinos[1]} [3]{destinos[2]} [4]{destinos[3]} [5]{destinos[4]}'))

if escolha_destino in range(1, 6):
    print(f"Você vai para {destinos[escolha_destino - 1]} semana que vem")
else:
    print("Escolha de destino inválida.")

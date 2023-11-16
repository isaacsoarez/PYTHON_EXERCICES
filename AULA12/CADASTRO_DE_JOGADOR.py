class Jogador:
    def __init__(self, nome, idade, clube, peso, altura, posicao, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.clube = clube
        self.peso = peso
        self.altura = altura
        self.posicao = posicao
        self.nacionalidade = nacionalidade

class SistemaEscolar:
    def __init__(self):
        self.jogadores = []

    def cadastrar_jogador(self, nome, idade, clube, peso, altura, posicao, nacionalidade):
        jogador = Jogador(nome, idade, clube, peso, altura, posicao, nacionalidade)
        self.jogadores.append(jogador)

# Loop para permitir múltiplos cadastros
while True:
    escolha = input('Digite "C" para cadastrar um jogador ou "X" para encerrar o programa: ')
    if escolha.lower() == 'c':
        sistema = SistemaEscolar()
        nome_jogador = input("Nome do jogador: ")
        idade_jogador = int(input("Idade do jogador: "))
        clube = input("Clube atual: ")
        peso = float(input('Peso do jogador (em kg): '))
        altura = float(input('Altura do jogador (em cm): '))
        posicao = input('Posição do jogador: ')
        nacionalidade = input("Nacionalidade do jogador: ")
        sistema.cadastrar_jogador(nome_jogador, idade_jogador, clube, peso, altura, posicao, nacionalidade)
        
        aposentadoria = (45 - idade_jogador)
        print(f"Faltam {aposentadoria} anos para {nome_jogador} se aposentar(aposentadoria é somente aos 45)")
        
        print(f"Jogadores cadastrados:")
        for jogador in sistema.jogadores:
            print(f"{jogador.nome}|{jogador.idade}|{jogador.clube}|{jogador.peso}|{jogador.altura}|{jogador.posicao}|{jogador.nacionalidade}")
            
    elif escolha.lower() == 'x':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")






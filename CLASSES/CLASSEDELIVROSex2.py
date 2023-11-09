class Livros:
    def __init__(self):
        self.lista_livros = [
            "Dom Quixote",
            "Cem Anos de Solidão",
            "1984",
            "Crime e Castigo",
            "O Senhor dos Anéis",
            "O Pequeno Príncipe",
            "Orgulho e Preconceito",
            "Ulisses",
            "A Revolução dos Bichos",
            "O Apanhador no Campo de Centeio"
        ]

    def exibir_lista(self):
        print("Lista de Livros:")
        for i, livro in enumerate(self.lista_livros, start=1):
            print(f"{i}. {livro}")

    def escolher_livro(self, escolha):
        if 1 <= escolha <= len(self.lista_livros):
            livro_selecionado = self.lista_livros[escolha - 1]
            return livro_selecionado
        else:
            return None


nome = input('Digite seu nome: ')

livros_obj = Livros()
livros_obj.exibir_lista()

escolha_livro = int(input("Escolha o número correspondente ao livro desejado: "))

livro_selecionado = livros_obj.escolher_livro(escolha_livro)

if livro_selecionado:
    print(f"{nome}, você selecionou: {livro_selecionado}")
else:
    print("Escolha inválida.")

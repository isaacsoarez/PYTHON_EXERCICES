class Frutas:
    def __init__(self):
        self.lista_frutas = [
            "Maçã",
            "Banana",
            "Morango",
            "Abacaxi",
            "Uva",
            "Pêssego",
            "Kiwi",
            "Manga",
            "Melancia",
            "Cereja"
        ]

    def exibir_lista(self):
        print("Lista de Frutas:")
        for i, fruta in enumerate(self.lista_frutas, start=1):
            print(f"{i}. {fruta}")

    def escolher_fruta(self, escolha):
        if 1 <= escolha <= len(self.lista_frutas):
            fruta_selecionada = self.lista_frutas[escolha - 1]
            return fruta_selecionada
        else:
            return None


nome = input('Digite seu nome: ')

frutas_obj = Frutas()
frutas_obj.exibir_lista()

escolha_fruta = int(input("Escolha o número correspondente à fruta desejada: "))

fruta_selecionada = frutas_obj.escolher_fruta(escolha_fruta)

if fruta_selecionada:
    print(f"{nome}, você selecionou a fruta: {fruta_selecionada}")
else:
    print("Escolha inválida.")

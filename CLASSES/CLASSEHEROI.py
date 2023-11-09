class Heroi:
    voa = False
    possui_arma = False
    lanca_teia = False
    frase_comum = ""

    def falar(self):
        print(self.frase_comum)

    def detalhar(self):
        if self.voa:
            print("O Heroi voa")
        if self.possui_arma:
            print("O Heroi possui arma")
        if self.lanca_teia:
            print("O heroi lança teia")



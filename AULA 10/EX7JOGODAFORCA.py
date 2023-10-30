import random

palavras = ["python", "programacao", "desenvolvimento", "computador", "inteligencia", "dados", "aprendizado", "algoritmo"]

palavra = random.choice(palavras)

letras_corretas = set()
letras_erradas = set()
tentativas_restantes = 6

def exibir_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

while True:
    print(exibir_palavra(palavra, letras_corretas))
    
    letra = input("Digite uma letra: ").lower()
    
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já tentou esta letra.")
        continue
    
    if letra in palavra:
        letras_corretas.add(letra)

        if letras_corretas == set(palavra):
            print("Parabéns! Você ganhou. A palavra era:", palavra)
            break
    else:
        letras_erradas.add(letra)
        tentativas_restantes -= 1
        print("Letras erradas:", " ".join(letras_erradas))
        print("Tentativas restantes:", tentativas_restantes)
        if tentativas_restantes == 0:
            print("Você foi enforcado. A palavra era:", palavra)
            break

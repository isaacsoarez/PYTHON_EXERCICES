# VOGAIS
palavras = ("senai", "henrique", "computador", "isaac", "garrafa")

def encontrar_vogal(word):
    vogal = []
    for letra in word:
        if letra in "aeiouAEIOU":
            vogal.append(letra)
    return vogal
for word in palavras:
    vogal = encontrar_vogal(word)
    print(f"As vogais da palavra '{word}' são: {','.join(vogal)}")

frase = input("Digite uma frase: ")

espacos_em_branco = 0
vogais = {'a', 'e', 'i', 'o', 'u'}
contagem_vogais = {vogal: 0 for vogal in vogais}

for caractere in frase:
    if caractere == ' ':
        espacos_em_branco += 1
    elif caractere.lower() in vogais:
        contagem_vogais[caractere.lower()] += 1

print(f"Espaços em branco na frase: {espacos_em_branco}")
for vogal, quantidade in contagem_vogais.items():
    print(f"A vogal '{vogal}' aparece {quantidade} vezes na frase.")

palavra = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

comprimento_palavra = len(palavra)
comprimento_palavra2 = len(palavra2)

print("Conteúdo da primeira string:", palavra)
print("Comprimento da primeira string:", comprimento_palavra)
print("Conteúdo da segunda string:", palavra2)
print("Comprimento da segunda string:", comprimento_palavra2)

if comprimento_palavra == comprimento_palavra2:
    if palavra == palavra2:
        print("As duas palavras têm o mesmo comprimento e são iguais no conteúdo.")
    else:
        print("As duas strings têm o mesmo comprimento, mas são diferentes no conteúdo.")
else:
    print("As duas strings têm comprimentos diferentes.")


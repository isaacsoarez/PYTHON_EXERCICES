notas = []

for i in range(4):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("As notas digitadas foram:", notas)
print(f"A média das notas é: {media:.2f}")
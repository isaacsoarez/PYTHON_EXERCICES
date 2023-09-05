idades = []
alturas = []
media_alturas = 0

for aluno in range(30):
    idade = int(input(f"Digite a idade do aluno {aluno + 1}: "))
    altura = float(input(f"Digite a altura (em metros) do aluno {aluno + 1}: "))
    idades.append(idade)
    alturas.append(altura)
    media_alturas += altura

media_alturas /= 30

alunos_com_altura_abaixo_da_media = 0
for i in range(30):
    if idades[i] > 13 and alturas[i] < media_alturas:
        alunos_com_altura_abaixo_da_media += 1

print(f"A média das alturas dos alunos é: {media_alturas:.2f} metros")
print(f"Número de alunos com mais de 13 anos e altura abaixo da média: {alunos_com_altura_abaixo_da_media}")
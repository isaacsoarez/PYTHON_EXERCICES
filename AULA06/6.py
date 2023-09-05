medias = []

alunosapro = 0

for aluno in range(6):
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota do aluno {aluno + 1}: "))
        notas.append(nota)
    
    media = sum(notas) / 4
    medias.append(media)
    
    if media >= 7.0:
        alunosapro += 1

print("Médias dos alunos:", medias)
print(f"Número de alunos com média maior ou igual a 7.0: {alunosapro}")
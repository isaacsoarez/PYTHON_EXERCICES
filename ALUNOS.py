quantidade_turmas = int(input("Digite a quantidade de turmas: "))

total_alunos = 0  

for turma in range(1, quantidade_turmas + 1):
    while True:
        alunos_turma = int(input(f"Digite o número de alunos na turma {turma}: "))
        if 0 < alunos_turma <= 40:
            total_alunos += alunos_turma
            break
        else:
            print("Número de alunos inválido. O número deve estar entre 1 e 40.")

media_alunos_por_turma = total_alunos / quantidade_turmas

print(f"A média de alunos por turma é: {media_alunos_por_turma:.2f}")

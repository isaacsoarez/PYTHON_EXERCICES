class Aluno:
    def __init__(self, nome, idade, curso, ra):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ra


class Professor:
    def __init__(self, nome, idade, disciplina):
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina


class SistemaEscolar:
    def __init__(self):
        self.alunos = []
        self.cursos = []
        self.professores = []

    def cadastrar_aluno(self, nome, idade, curso, ra):
        aluno = Aluno(nome, idade, curso, ra)
        self.alunos.append(aluno)

    def cadastrar_curso(self, nome_curso):
        if nome_curso not in self.cursos:
            self.cursos.append(nome_curso)
            print(f"Curso '{nome_curso}' cadastrado com sucesso.")
        else:
            print(f"O curso '{nome_curso}' já existe.")

    def cadastrar_professor(self, nome, idade, disciplina):
        professor = Professor(nome, idade, disciplina)
        self.professores.append(professor)

    def excluir_aluno(self, ra):
        self.alunos = [aluno for aluno in self.alunos if aluno.ra != ra]
        print(f"Aluno com RA {ra} excluído com sucesso.")

    def excluir_curso(self, nome_curso):
        if nome_curso in self.cursos:
            self.cursos.remove(nome_curso)
            print(f"Curso '{nome_curso}' excluído com sucesso.")
        else:
            print(f"O curso '{nome_curso}' não existe.")

    def excluir_professor(self, nome):
        self.professores = [professor for professor in self.professores if professor.nome != nome]
        print(f"Professor {nome} excluído com sucesso.")

    def exibir_alunos_em_curso(self, curso):
        if curso in self.cursos:
            alunos_curso = [aluno.nome for aluno in self.alunos if aluno.curso == curso]
            print(f"Alunos em {curso}: {', '.join(alunos_curso)}")
        else:
            print(f"O curso '{curso}' não existe.")

    def exibir_professores(self):
        for professor in self.professores:
            print(f"Professor {professor.nome}, Idade: {professor.idade}, Disciplina: {professor.disciplina}")

    def exibir_numero_alunos_cadastrados(self):
        print(f"Total de alunos cadastrados: {len(self.alunos)}")


def exibir_menu():
    print("\n===== MENU =====")
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Curso")
    print("3. Cadastrar Professor")
    print("4. Excluir Aluno")
    print("5. Excluir Curso")
    print("6. Excluir Professor")
    print("7. Exibir Alunos em Curso")
    print("8. Exibir Professores")
    print("9. Exibir Número de Alunos Cadastrados")
    print("n. Reiniciar o Menu")
    print("s. Sair do Programa")


def main():
    sistema = SistemaEscolar()

    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do aluno: ")
            idade = int(input("Idade do aluno: "))
            curso = input("Curso do aluno: ")
            ra = input("RA do aluno: ")
            sistema.cadastrar_aluno(nome, idade, curso, ra)

        elif escolha == '2':
            nome_curso = input("Nome do curso: ")
            sistema.cadastrar_curso(nome_curso)

        elif escolha == '3':
            nome_professor = input("Nome do professor: ")
            idade_professor = int(input("Idade do professor: "))
            disciplina = input("Disciplina lecionada: ")
            sistema.cadastrar_professor(nome_professor, idade_professor, disciplina)

        elif escolha == '4':
            ra_aluno = input("Digite o RA do aluno a ser excluído: ")
            sistema.excluir_aluno(ra_aluno)

        elif escolha == '5':
            nome_curso_excluir = input("Digite o nome do curso a ser excluído: ")
            sistema.excluir_curso(nome_curso_excluir)

        elif escolha == '6':
            nome_professor_excluir = input("Digite o nome do professor a ser excluído: ")
            sistema.excluir_professor(nome_professor_excluir)

        elif escolha == '7':
            curso_exibir = input("Digite o nome do curso: ")
            sistema.exibir_alunos_em_curso(curso_exibir)

        elif escolha == '8':
            sistema.exibir_professores()

        elif escolha == '9':
            sistema.exibir_numero_alunos_cadastrados()

        elif escolha.lower() == 'n':
            continue

        elif escolha.lower() == 's':
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()

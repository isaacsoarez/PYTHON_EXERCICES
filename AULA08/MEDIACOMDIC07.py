aluno = {}
media = {}

nome = str(input("Digite o nome do aluno"))
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media1 = (nota1 + nota2) / 2

aluno['nome'] = nome 
aluno['media'] = media1

print(f"o nome do aluno é {aluno['nome']}")
print(f"A nota do aluno é {aluno['media']}")



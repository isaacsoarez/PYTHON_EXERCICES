#Faça um programa que solicite o nome do usuário e a idade do usuário, depois disso
#exiba a mensagem: “{nome} possui {idade} anos.”. Esta mensagem deve ser escrita
#em uma função lambda.

calcular_idade_em_ano = lambda idade, ano: idade + (ano - 2023)
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
ano = int(input('Digite o ano desejado: '))

print(f'{nome} possui {idade} anos de idade')

idade_em_ano = calcular_idade_em_ano(idade, ano)
print(f'{nome} terá {idade_em_ano} anos em {ano}.')

jogador = {}

jogador['nome'] = input("Digite o nome do jogador: ")
partidas = int(input("Quantas partidas o jogador jogou? "))

jogador['gols'] = []

for partida in range(partidas):
    gols = int(input(f"Quantos gols o jogador fez na partida {partida + 1}? "))
    jogador['gols'].append(gols)

jogador['total'] = sum(jogador['gols'])

print("\nInformações do jogador:")
print(f"Nome do jogador: {jogador['nome']}")
print(f"Quantidade de partidas jogadas: {partidas}")
print(f"Gols em cada partida: {jogador['gols']}")
print(f"Total de gols: {jogador['total']}")

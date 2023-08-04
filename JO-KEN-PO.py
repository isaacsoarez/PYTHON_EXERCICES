import random

def jogo_pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou 'sair' para encerrar o jogo): ").lower()
        computador = random.choice(opcoes)
        
        if jogador == 'sair':
            print("Jogo encerrado.")
            break
        
        if jogador not in opcoes:
            print("Opção inválida. Escolha pedra, papel ou tesoura.")
            continue
        
        print("Você escolheu:", jogador)
        print("O computador escolheu:", computador)
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or (jogador == 'papel' and computador == 'pedra') or (jogador == 'tesoura' and computador == 'papel'):
            print("Você ganhou!")
        else:
            print("Você perdeu!")

jogo_pedra_papel_tesoura()

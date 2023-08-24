while True:
    resposta = str(input('Você gosta de Python? '))
    resposta = resposta.upper() 
    
    if resposta == "SIM":
        print('Ótimo! Também adoro Python!')
        break
    else:
        print('Esta não é a resposta correta. Tente novamente.')

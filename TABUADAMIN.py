while True:
    numero = int(input("Digite um número para calcular a tabuada (ou digite 0 para sair): "))

    if numero == 0:
        break  
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

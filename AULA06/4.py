sequencia = input("Digite uma sequência de 10 caracteres: ")

consoantes = []

for caractere in sequencia:
    if caractere.isalpha() and not caractere.lower() in 'aeiou':
        consoantes.append(caractere)

print("Consoantes lidas:", consoantes)
#auxilio da internet
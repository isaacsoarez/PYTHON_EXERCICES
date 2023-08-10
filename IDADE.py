idade=int(input('Digite a idade do competidor para classificar sua categoria:'))

if idade <=7:
    print('INFANTIL A')
elif idade<=11:
    print('INFANTIL B')
elif idade<= 13:
    print('JUVENIL A')
elif idade<= 17:
    print('JUVENIL B')
elif idade>=18:
    print('ADULTOS')
else:
    print('COMPETIDOR INVÁLIDO')

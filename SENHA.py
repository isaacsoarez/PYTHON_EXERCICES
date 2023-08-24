senha1 = str(input('Digite sua senha:'))
senha2 = str(input('Confirme a senha:'))

while True:
    if senha1 == senha2:
        print('Acesso Permitido')
    break
if senha1 != senha2:
        print('Senha Incorreta, tente novamente!')
else:
        print('---------')
          
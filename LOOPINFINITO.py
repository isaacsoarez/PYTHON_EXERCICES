notas=0
notasinfo= 0
while True:
    nota= float(input('informe a nota(-1 para finalizar):'))
    if (nota ==-1):
        break
    notas=notas+nota
    notasinfo = notasinfo+1
    if notasinfo > 0:
        media= notas/ notasinfo
        print(f'Quantidade de notas informadas: {notasinfo}')
        print(f'media: {media:.2f}')
    else:
        print('nenhuma nota informada')
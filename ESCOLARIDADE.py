pessoa = {'nome': 'isaac','idade':23}
escola = {'escolaridade': 'SESI', 'termo':'ID2SI'}
print('Olá {nome}! Você tem {idade} anos de idade.'.format(**pessoa))
print('Você estuda na escola {escolaridade} e está no seguinte termo: {termo}'.format(**escola))

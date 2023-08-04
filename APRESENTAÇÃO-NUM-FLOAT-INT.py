num = 13.744
print('Números como %s são convertidos para string' % num)
print('Também podem ser representados como inteiros: %d; repare que sem arredondamento' % num)
print(f'Também podem ser representados como floats: {num:.3f}'.replace('.', ','))

print('Amostra de sinal em inteiros: %+d' % num)
print('Amostra de sinal em floats: %+f' % num)
print(f'Amostra de sinal em floats (virgula): {num:+.3f}'.replace('.', ','))

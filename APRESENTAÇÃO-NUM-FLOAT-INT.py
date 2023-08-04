num = 13.744
print('Números como %s são convertidos para string' % num)
print('Também podem ser representados como inteiros: %d; repare que sem arredondamento' % num)
print(f'Também podem ser representados como floats: {num:.3f}'.replace('.', ','))

print('Amostra de sinal em inteiros: %+d' % num)
print('Amostra de sinal em floats: %+f' % num)
print(f'Amostra de sinal em floats (virgula): {num:+.3f}'.replace('.', ','))
print('____________________________________________________________')
num2=179.450

print('Mínimo de 5 caracteres com 2 casas decimais:%5.2f' % num2)
print('Mínimo de 1 caracteres com 0 casas decimais:%1.0f' % num2)
print('Mínimo de 1 caracteres com 5 casas decimais:%1.5f' % num2)
print('Mínimo de 10 caracteres com 2 casas decimais:%10.2f' % num2)
print('Mínimo de 10 caracteres com 2 casas decimais:%+10.2f (com sinal)' % num2)





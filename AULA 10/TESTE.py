texto =' Hello World'
texto_centro = texto.center(20)
texto_centro_2 = texto.center(20, '=')
texto_esquerda = texto.ljust(12)
texto_direita = texto.rjust(12)
print(f'**{texto_esquerda}*{texto_direita}**')

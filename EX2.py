import random

minha_tupla = tuple(random.randint (0, 100) for i in range(5))

print('Os números escolhidos foram:', minha_tupla)
print('O maior número é :', max(minha_tupla))
print('O menor número é :', min(minha_tupla))

#TUPLAS:

def remover_impares(tupla):
    tupla_sem_impares = tuple (item for item in tupla if item % 2 == 0)
    
    return tupla_sem_impares

minha_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_sem_impares = remover_impares(minha_tupla)
print('--------------------------------')

print(tupla_sem_impares)

print('--------------------------------')
def remover_pares(tupla):
    tupla_sem_pares = tuple (item for item in tupla if item % 2 != 0)
    
    return tupla_sem_pares

minha_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_sem_pares = remover_pares(minha_tupla)
print(tupla_sem_pares)
print('--------------------------------')

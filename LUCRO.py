fat = int(input('Digite seu faturamento:'))
cus = int(input('Digite seu custo:'))
luc = fat - cus
mar = luc / fat
print(f'Seu lucro foi de: R${luc:_.2f}')
print(f'Sua margem foi de: R$ {mar:_.2f}')

class Ponto():
    x = 10
    y = 7
p = Ponto()
print(p.x)
print(p.y)
p.x = 12
print(p.x)
print(Ponto.x)
del p.x
print(p.x)
p.z = 3
print(p.z)

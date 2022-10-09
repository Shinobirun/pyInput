
paises = input('Agregar al menos 4 paises, separados por comas')

list = paises.split(sep=',')

list.sort()

for i in range(len(list)-1,-1,-1):
    if list[i] in list[:i]:
        del list[i]

print(list)
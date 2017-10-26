# Desiree Lopez Ramirez A01371590
# Sandra Rodriguez Oseguera A01371995

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


fname = input("Introduce el nombre del archivo: ")
file = open(fname, 'r')
estados = file.read().strip('{}').split('),')
file.close()
lista_edos = []

# obtenemos la primera lista de estados
for item in estados:
    # lista_edos.append(re.sub('[(,)]', '', item)) Si queremos tratarlo como string

    # Si queremos tratarlo como lista con listas dentro
    item = item.strip('()').split(',')
    lista_edos.append(item)

#print(lista_edos)
lista_edos2 = [lista_edos[0]]

# para tener agrupadas todas las transiciones ej: (0,p,q),(0,p,p)= (0,p,pq)
for i in range(1, len(lista_edos)):
    flag = 0
    for j in range(0, len(lista_edos2)):
        if (lista_edos2[j][1] == lista_edos[i][1] and lista_edos2[j][0] == lista_edos[i][0]):
            lista_edos2[j][2] += lista_edos[i][2]
            flag = 1
    if flag == 0:
        lista_edos2.append(lista_edos[i])


#dividimos en dos listas (transicion con 0, transicion con 1)
lista_edosA = [lista_edos2[0]]
lista_edosB = []
for i in range(1, len(lista_edos2)):
    if lista_edos2[i][0] == lista_edosA[0][0]:
        lista_edosA.append(lista_edos2[i])
    else:
        lista_edosB.append(lista_edos2[i])

h = powerset(lista_edosA)
for k in h:
    print(k)




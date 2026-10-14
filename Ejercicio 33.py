'''Tres mayores sin ordenar toda la lista
Dificultad: Media
Enunciado: Diseña una función que reciba una lista de enteros y retorne una lista con los tres valores más altos, en
orden descendente.
Puedes asumir que la lista tiene al menos tres elementos.
Qué habilidades practica: Seguimiento de varios máximos, comparación, diseño de algoritmos sin apoyos
automáticos.
Restricciones importantes: No usar sort() ni sorted().'''

def ordenar_descendente(lista):
    largo = len(lista)

    for i in range(largo):
        for j in range(0, largo - i - 1):
            if lista[j] < lista[j + 1]:
                temp = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = temp

    return lista



def tres_altos(lista_enteros):
    temp = ordenar_descendente(lista_enteros)
    tres_mayores = []

    for i in range(3):
        tres_mayores.append(temp[i])

    return tres_mayores

lista_1 = [4, 7, 1, 9, 3, 8, 2]
print(f'ORIGINAL | {lista_1}')
print(f'ORDENADA | {ordenar_descendente(lista_1)}')
print(f'3 ALTOS  | {tres_altos(lista_1)}')



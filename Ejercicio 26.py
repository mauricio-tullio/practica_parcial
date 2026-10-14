'''Rotar una lista una posición a la derecha
Dificultad: Media
Enunciado: Haz una función que reciba una lista y retorne una nueva lista donde todos los elementos se desplacen
una posición a la derecha.
El último elemento debe pasar a ser el primero.
Por ejemplo, [4, 7, 1, 9] debe convertirse en [9, 4, 7, 1].
Qué habilidades practica: Manipulación de posiciones, construcción de nuevas listas, casos borde.
Restricciones importantes: Si la lista está vacía, debe retornar una lista vacía.'''

def desplazar_derecha(lista_elementos):

    if not lista_elementos:
        return []

    lista_desplazada = []

    lista_desplazada.append(lista_elementos[len(lista_elementos) - 1])

    for i in range(len(lista_elementos) - 1):
        lista_desplazada.append(lista_elementos[i])

    return lista_desplazada

lista = [4, 7, 1, 9]
print(desplazar_derecha(lista))
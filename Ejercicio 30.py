'''Comparar dos listas elemento a elemento
Dificultad: Media
Enunciado: Escribe una función que reciba dos listas de enteros del mismo tamaño y retorne una nueva lista.
Para cada posición:
- agrega 'A' si el elemento de la primera lista es mayor,
- agrega 'B' si el de la segunda es mayor,
- agrega 'I' si son iguales.

Guía de estudio - Programación 1
Qué habilidades practica: Listas paralelas, recorrido por índice, comparación estructurada.
Restricciones importantes: Supón que ambas listas tienen igual tamaño.'''

def comparacion_lista(lista_a, lista_b):
    lista_comparacion = []


    for i in range(len(lista_a)):
        if lista_a[i] == lista_b[i]:
            lista_comparacion.append('I')
        elif lista_a[i] <= lista_b[i]:
            lista_comparacion.append('B')
        elif lista_a[i] >= lista_b[i]:
                    lista_comparacion.append('A')

    return lista_comparacion

lista_a = [10, 25, 40, 15, 30]
lista_b = [12, 25, 35, 20, 30]

print(comparacion_lista(lista_a, lista_b))
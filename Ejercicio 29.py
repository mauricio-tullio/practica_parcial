'''Conteo por rangos de notas
Dificultad: Media
Enunciado: Haz una función que reciba una lista de notas enteras entre 0 y 20 y retorne una lista con cuatro
cantidades:
- cuántas están entre 0 y 4,
- cuántas entre 5 y 9,
- cuántas entre 10 y 14,
- cuántas entre 15 y 20.
Qué habilidades practica: Clasificación por rangos, acumuladores múltiples, listas como estructura de salida.
Restricciones importantes: Recorrer la lista una sola vez.'''

def conteo_enteros(lista_enteros):
    lista_contadores = [0, 0, 0, 0]

    for entero in lista_enteros:
        if 0 <= entero <= 4:
           lista_contadores[0] += 1
        elif 5 <= entero <= 9:
            lista_contadores[1] += 1
        elif 10 <= entero <= 14:
            lista_contadores[2] += 1
        elif 15 <= entero <= 20:
            lista_contadores[3] += 1

    return lista_contadores

notas = [3, 12, 18, 5, 2, 14, 7, 20, 10, 4, 15, 8]
print(conteo_enteros(notas))
        

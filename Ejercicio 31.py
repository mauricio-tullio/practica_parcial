'''Inventario con reposición
Dificultad: Media
Enunciado: Una tienda tiene una lista con cantidades disponibles por producto.
Crea una función que reciba esa lista y retorne una nueva lista con mensajes:
- 'reponer' si la cantidad es menor que 5,
- 'vigilar' si está entre 5 y 10,
- 'ok' si es mayor que 10.
Qué habilidades practica: Clasificación de datos, listas de salida, condicionales, interpretación de estados.
Restricciones importantes: El resultado debe tener la misma longitud que la lista original.'''

def check_inventario(lista_inventario):
    lista_check = []

    for producto in lista_inventario:
        if 0 <= producto < 5:
            lista_check.append('reponer')
        elif 5 <= producto <= 10:
            lista_check.append('vigilar')
        else:
            lista_check.append('ok')

    return lista_check

inventario_prueba = [2, 15, 7, 4, 10, 0, 12, 8, 5, 20, 3]
print(inventario_prueba)
print(check_inventario(inventario_prueba))
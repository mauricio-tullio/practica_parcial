'''Diferencias entre días consecutivos
Dificultad: Media
Enunciado: Diseña una función que reciba una lista de temperaturas diarias y retorne una nueva lista con la
diferencia entre cada día y el anterior.
Por ejemplo, si la entrada es [20, 22, 19, 21], la salida debe ser [2, -3, 2].
Qué habilidades practica: Recorrido con índices, comparación entre elementos vecinos, construcción de
resultados.
Restricciones importantes: Si la lista tiene menos de 2 elementos, retorna una lista vacía.'''

def variacion_temperatura(lista_temperaturas):
    if len(lista_temperaturas) < 2:
        return []
    
    comparation = None
    lista_variacion = []

    for temperatura in lista_temperaturas:
        if comparation == None:
            comparation = temperatura
            continue

        lista_variacion.append(temperatura - comparation)
        comparation = temperatura

    return lista_variacion

lista = [20, 22, 19, 21]
print(variacion_temperatura(lista))
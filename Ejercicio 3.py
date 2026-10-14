'''Ejercicio 3. Mayor puntaje obtenido
Dificultad: Fácil
Enunciado: Desarrolla una función que reciba una lista de puntajes y retorne el valor más alto encontrado.
Supón que la lista tendrá al menos un elemento.
Qué habilidades practica: Búsqueda de máximo con recorrido, comparación, inicialización correcta de variables.
Restricciones importantes: No usar max().'''


def mayor_puntaje(puntajes):

    mayor = 0

    for puntaje in puntajes:
        if puntaje > mayor:
            mayor = puntaje

    return mayor

lista_puntajes = []

while True:
    try:
        entrada = input('Ingresa el valor (enter para culminar):')

        if entrada == '':
            break

        lista_puntajes.append(int(entrada))

    except ValueError:
        print('Ingresa en valor valido')

print(f'El mayor puntaje de la lista {lista_puntajes} en {mayor_puntaje(lista_puntajes)}')
'''Eliminar repetidos conservando el orden
Dificultad: Media
Enunciado: Escribe una función que reciba una lista y retorne una nueva lista sin elementos repetidos,
manteniendo la primera aparición de cada valor.
Qué habilidades practica: Búsqueda dentro de listas, construcción progresiva, control de repetidos.
Restricciones importantes: No usar set().'''

def eliminar_rep(lista_elementos):
    sin_repetidos = []

    for a in lista_elementos:
        if a not in sin_repetidos:
            sin_repetidos.append(a)

    return sin_repetidos

lista_elementos = []

print('--- Crear Lista ---')
while True:
    entrada = input('Ingrese un valor: ')

    if entrada == '':
        break

    lista_elementos.append(entrada)

print('--- Lista sin Repetidos ---')
print(f'ORIGINAL      {lista_elementos} \nSIN REPETIDOS {eliminar_rep(lista_elementos)}')
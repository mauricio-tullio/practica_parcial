'''Posiciones de un valor
Dificultad: Media
Enunciado: Escribe una función que reciba una lista de enteros y un valor objetivo.
Debe retornar una lista con todas las posiciones en las que aparece ese valor.
Si no aparece, debe retornar una lista vacía.
Qué habilidades practica: Recorrido con índices, acumulación en listas, búsqueda múltiple.
Restricciones importantes: Las posiciones deben quedar en orden ascendente.'''

def posicion_objetivo(lista_enteros, objetivo):
    lista_posiciones = []

    for i in range(len(lista_enteros)):
        if objetivo == lista_enteros[i]:
            lista_posiciones.append(i)
    return lista_posiciones

print('--- Crear Lista ---')

lista_enteros = []

while True:
    try:
        entrada = input('Ingrese un numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)
    except ValueError:
        print('Ingresa un numero valido')

numero = None

print('--- Numero Objetivo ---')
while True:
    try:
        numero = int(input('Ingrese el numero a buscar: '))
        break
    except ValueError:
        print('Ingrese un numero valido')
    

print('\n--- Posicion Numero Objetivo ---')
print(lista_enteros)
print(f'[{numero}] | POSICIONES {posicion_objetivo(lista_enteros, numero)}')
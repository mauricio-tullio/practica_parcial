'''Última aparición de un valor
Dificultad: Fácil
Enunciado: Escribe una función que reciba una lista de enteros y un valor objetivo.
Debe retornar la posición de la última vez que aparece ese valor.
Si no aparece, debe retornar -1.
Qué habilidades practica: Recorrido con índices, actualización de resultado, búsqueda, casos borde.
Restricciones importantes: Resolver recorriendo la lista completa.'''


def posicion_entero(lista_enteros, valor):
    posicion = -1
    for entero in range(len(lista_enteros)):
        if valor == lista_enteros[entero]:
            posicion = entero

    return posicion

lista_enteros = []

print('--- Ingresar Numeros ---')
while True:
    try:
        entrada = input('Ingresa un numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)

    except ValueError:
        print('Ingresa un valor valido')

print('--- Buscar Numero ---')
while True:
    try:
        entrada = input('Ingresa el numero buscado: ')

        if entrada == '':
            break

        entrada = int(entrada)

        print('--- Resultado ---')
        print(f'El numero {entrada} esta en la posicion {posicion_entero(lista_enteros, entrada)} de la lista {lista_enteros}')

    except ValueError:
        print('Ingresa un numero valido')
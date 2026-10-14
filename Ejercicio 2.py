'''Ejercicio 2. Contar temperaturas bajo cero
Dificultad: Fácil
Enunciado: Crea una función que reciba una lista de temperaturas enteras y retorne cuántas de ellas son menores
que 0.
Piensa en cómo llevar un contador que aumente solo cuando se cumpla la condición.
Qué habilidades practica: Conteo condicionado, uso de for, comparación de valores, funciones simples.
Restricciones importantes: No usar count().'''


def contador_bajo_cero(temperaturas):

    contador= 0

    for temperatura in temperaturas:
        if(temperatura < 0):
            contador += 1

    return contador

lista_temperaturas = []

while True:
    try:
        entrada = input('Ingrese el valor (enter para culminar): ')

        if(entrada == ''):
            break

        lista_temperaturas.append(int(entrada))

    except ValueError:
        print('Ingrese un valor valido')

print(f'Se ingresaron {contador_bajo_cero(lista_temperaturas)} temperaturas bajo cero')
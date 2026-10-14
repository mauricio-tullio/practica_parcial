'''Crear una lista de cuadrados
Dificultad: Fácil
Enunciado: Construye una función que reciba una lista de enteros y retorne una nueva lista con el cuadrado de
cada número, respetando el mismo orden de entrada.
Qué habilidades practica: Construcción de listas, append, recorrido, transformación de datos.
Restricciones importantes: Debes crear una lista nueva; no cambiar la lista original.'''

def calcular_cuadrado(lista_enteros):
    lista_cuadrado = []
    for entero in lista_enteros:
        lista_cuadrado.append(entero ** 2)
    return lista_cuadrado

lista_enteros = []

while True:
    try:
        entrada = input('Ingresa un numero: ')

        if entrada == '':
            break

        lista_enteros.append(int(entrada))

    except ValueError:
        print('Ingrese un numero valido')

print(f'El cuadrado de la lista {lista_enteros} es {calcular_cuadrado(lista_enteros)}')
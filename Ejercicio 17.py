'''Segundo valor más alto distinto
Dificultad: Media
Enunciado: Diseña una función que reciba una lista de enteros y retorne el segundo valor más alto distinto.
Por ejemplo, en [8, 5, 8, 3] el resultado debe ser 5.
Si no existe un segundo valor distinto, debes indicar claramente qué retorna tu solución.
Qué habilidades practica: Comparación, rastreo de varios máximos, manejo de repetidos, casos borde.
Restricciones importantes: No usar sort() ni max().'''

def segundo_mayor(lista_enteros):
    mayor = None
    sg_mayor = None

    for entero in lista_enteros:
        if mayor == None or entero > mayor:
            sg_mayor = mayor
            mayor = entero
        elif entero < mayor and (sg_mayor == None or sg_mayor < entero):
            sg_mayor = entero

    return sg_mayor

lista_enteros = []

print('--- Crear Lista ---')

while True:
    try:
        entrada = input('Ingresa un numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)

    except ValueError:
        print('Ingresa un numero valido')

print('\n--- Segundo Mayor ---')

print(f'SEGUNDO - {segundo_mayor(lista_enteros)} - {lista_enteros}')
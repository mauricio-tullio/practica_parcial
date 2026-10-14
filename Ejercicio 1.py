'''Dificultad: Fácil
Enunciado: Escribe una función que reciba una lista de montos enteros que representan gastos diarios de una
semana y retorne el gasto total.
La solución debe recorrer la lista con un ciclo for y acumular el resultado manualmente.
Prueba tu función con listas de distintos tamaños, incluyendo una lista vacía.
Qué habilidades practica: Recorrido básico de listas, acumulación, definición de funciones, caso borde con lista
vacía.
Restricciones importantes: No usar sum(). La respuesta debe obtenerse recorriendo la lista elemento por
elemento.'''

gastos_diarios = []
gasto = 0

def calcular_gastos(gastos_diarios):

    gasto_total = 0

    for gastos in gastos_diarios:
        gasto_total += gastos
        
    return gasto_total

while True:
    try:
        gasto = int(input('Ingrese el monto: '))

        if(gasto == 0):
            break

        if(gasto < 0):
            print('Ingresa un valor valido')
            continue

        gastos_diarios.append(gasto)

    except ValueError:
        print('Ingresa un valor valido')

print(f'Total: {calcular_gastos(gastos_diarios)}')
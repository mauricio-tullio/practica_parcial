'''Detectar la primera racha de tres iguales
Dificultad: Media

Preparación para el primer parcial

Enunciado: Desarrolla una función que reciba una lista de enteros y determine si en algún punto aparecen tres
valores iguales de forma consecutiva.
La función debe retornar True o False.
Qué habilidades practica: Recorrido con índices, análisis de vecinos, condiciones compuestas.
Restricciones importantes: Resolver sin usar while.'''

def tres_consecutivos(lista_enteros):
    valor = None
    contador = 0
    for entero in lista_enteros:
        if valor == entero:
            contador += 1
        else:
            contador = 1
            valor = entero

        if contador == 3:
            return True
        
    return False

print('--- Crear Lista ---')

lista_enteros = []

while True:
    try:
        entrada = input('Ingrese el nombre del producto: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)
    except ValueError:
        print('Ingresa un numero valido')

print('\n--- Resultado Tres en Fila ---')
print(tres_consecutivos(lista_enteros))

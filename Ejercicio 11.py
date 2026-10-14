'''Lista de múltiplos en un rango
Dificultad: Fácil
Enunciado: Crea una función que reciba un número entero positivo n y retorne una lista con todos los múltiplos de
3 desde 3 hasta n, en orden ascendente.

Guía de estudio - Programación 1

Preparación para el primer parcial

Qué habilidades practica: Uso de for con rango, condiciones, construcción de listas.
Restricciones importantes: Si n es menor que 3, la función debe retornar una lista vacía.'''

def multiplos_tres(entero):
    lista = []
    for i in range(3, entero + 1, 3):
        lista.append(i)

    return lista

print('--- Numero a Evaluar ---')
while True:
    try:
        entrada = input('Ingresa el numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        print(f'Los multiplos de 3 del numero {entrada} son {multiplos_tres(entrada)}')
        
    except ValueError:
        print('Ingresa un numero valido')
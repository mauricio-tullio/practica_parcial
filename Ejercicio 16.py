'''Separar positivos, negativos y ceros
Dificultad: Media
Enunciado: Crea una función que reciba una lista de enteros y retorne tres cantidades: cuántos números son
positivos, cuántos son negativos y cuántos son cero.
Qué habilidades practica: Conteo múltiple, condiciones encadenadas, diseño de funciones con varios resultados.
Restricciones importantes: Recorrer la lista una sola vez.'''

def separar_enteros(lista_enteros):
    contador_negativo = 0
    lista_negativo = []
    contador_0 = 0
    contador_positivo = 0
    lista_positivo = []

    for entero in lista_enteros:
        if entero == 0:
            contador_0 += 1
        elif entero < 0:
            contador_negativo += 1
            lista_negativo.append(entero)
        else:
            contador_positivo += 1
            lista_positivo.append(entero)

    return(contador_negativo, lista_negativo, contador_0, contador_positivo, lista_positivo)

lista_enteros = []

print('--- Crear Lista ---')
while True:
    try:
        entrada = input('Ingresa el numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)
    except ValueError:
        print('Ingresa un numero valido')

print('\n--- Separar Tipos de Enteros ---')

cantidad_negativo, lista_negativo, cantidad_0, cantidad_positivo, lista_positivo = separar_enteros(lista_enteros)

print(f'Negativos - {cantidad_negativo} - {lista_negativo}')
print(f'Cero - {cantidad_0}')
print(f'Positivos - {cantidad_positivo} - {lista_positivo}')

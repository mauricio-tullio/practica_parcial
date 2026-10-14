'''19. Elementos comunes sin duplicados
Dificultad: Media
Enunciado: Haz una función que reciba dos listas de enteros y retorne una nueva lista con los valores que aparecen
en ambas, sin repetir elementos en el resultado.
Qué habilidades practica: Comparación entre listas, validación de pertenencia, control de duplicados.
Restricciones importantes: El orden del resultado debe respetar la primera lista.'''

def interseccion_lista(lista_1, lista_2):
    lista_interseccion = []

    for a in lista_1:
        if a in lista_2 and a not in lista_interseccion:
            lista_interseccion.append(a)

    return lista_interseccion

lista_1 = []

print('--- Crear Lista 1 ---')
while True:
    try:
        entrada = input('Ingrese un numero: ')

        if entrada == '':
            break
        entrada = int(entrada)
        lista_1.append(entrada)
    except ValueError:
        print('Ingresa un numero valido')

lista_2 = []

print('\n--- Crear Lista 2 ---')
while True:
    try:
        entrada = input('Ingrese un numero: ')

        if entrada == '':
            break
        entrada = int(entrada)
        lista_2.append(entrada)
    except ValueError:
        print('Ingresa un numero valido')

print('\n--- Interseccion de las Listas ---')

print(f'{lista_1} intersectada {lista_2}')
print(interseccion_lista(lista_1, lista_2))
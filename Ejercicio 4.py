'''Promedio de notas
Dificultad: Fácil
Enunciado: Haz una función que reciba una lista de notas enteras y retorne el promedio de esas notas.
Antes de dividir, asegúrate de pensar qué debe ocurrir si la lista está vacía.
Qué habilidades practica: Acumulación, conteo, división final, manejo de lista vacía.
Restricciones importantes: Si la lista está vacía, indica claramente en tu diseño qué valor debe retornar la función.'''


def promedio_notas(lista):

    if len(lista) == 0:
        return 0

    suma_notas = 0

    for nota in lista:
        suma_notas += nota

    return suma_notas/len(lista)

lista_notas = []

while True:
    try:
        user_input = input('Ingrese la nota: ')

        if user_input == '':
            break
        
        user_input = int(user_input)

        if user_input < 0:
            print('Ingrese un valor valido')
            continue
        else:
            lista_notas.append(user_input)

    except ValueError:
        print('Ingrese un valor valido')

print(f'El promedio de las notas {lista_notas} es {promedio_notas(lista_notas)}')

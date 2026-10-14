'''Filtrar números pares
Dificultad: Fácil
Enunciado: Haz una función que reciba una lista de enteros y retorne una nueva lista que contenga únicamente los
números pares de la lista original.
Qué habilidades practica: Condicionales, construcción de listas, append, recorrido con for.
Restricciones importantes: Debes retornar una nueva lista.'''

def extraer_pares (lista_enteros):
    lista_pares = []

    for entero in lista_enteros:
        if entero % 2 == 0:
            lista_pares.append(entero)
    return lista_pares

lista_enteros = []

print('--- Ingresar Numeros ---')
while True:
    try:
        entrada = input('Ingrese un numero: ')

        if entrada == '':
            break

        entrada = int(entrada)
        lista_enteros.append(entrada)

    except ValueError:
        print('Ingrese un numero valido')

if lista_enteros:
    print(f'{lista_enteros} los pares son {extraer_pares(lista_enteros)}')
else:
    print('No se han ingresado numeros')
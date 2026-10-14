'''Invertir una lista en una copia
Dificultad: Fácil
Enunciado: Desarrolla una función que reciba una lista y retorne otra lista con los mismos elementos, pero en
orden inverso.
Qué habilidades practica: Recorridos con índices, construcción de listas, orden de procesamiento.
Restricciones importantes: No usar reverse() ni slicing [::-1].'''

def invertir_lista(lista):
    invertida = []
    for elemnto in range(len(lista) - 1,-1,-1):
        invertida.append(lista[elemnto])

    return invertida

lista = []

print('--- Crear Lista ---')
while True:
    entrada = input('Ingresa un elemento: ')

    if entrada == '':
        break

    lista.append(entrada)

print('--- Lista Invertida ---')
print(f'Original  {lista} \nInvertida {invertir_lista(lista)}')
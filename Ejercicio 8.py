'''Contar palabras largas
Dificultad: Fácil
Enunciado: Diseña una función que reciba una lista de palabras y retorne cuántas tienen 6 letras o más.
Qué habilidades practica: Uso de len(), conteo condicionado, recorrido de listas, strings.
Restricciones importantes: No usar comprensiones de lista.'''

def contar_lista(palabras_lista):
    contador = 0
    lista_6 = []
    for palabra in palabras_lista:
        if len(palabra) >= 6:
            contador += 1
            lista_6.append(palabra)
    return lista_6, contador

palabras_lista = []


print('--- Ingresar Palabras ---')
while True:
        entrada = input('Ingrese una plabara: ')

        if entrada == '':
            break
        palabras_lista.append(entrada)

new_list, num_palabras = contar_lista(palabras_lista)

print(f'Hay {num_palabras} palabras con mas de 6 letras y son {new_list}')





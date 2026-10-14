'''Contar repeticiones de una letra
Dificultad: Fácil
Enunciado: Haz una función que reciba una lista de palabras y una letra.
La función debe retornar cuántas veces aparece esa letra considerando todas las palabras de la lista.
Qué habilidades practica: Recorridos anidados simples, conteo, manejo de strings dentro de listas.
Restricciones importantes: Comparar letra por letra.'''

def contar_letra(lista,letra):

    contador_letra = 0

    for palabra in lista:
        for n_letra in palabra:
            if n_letra == letra:
                contador_letra += 1

    return contador_letra

lista_palabras = []

print('--- Crear Lista ---')
while True:
    entrada = input('Ingresa una palabra: ')

    if entrada == '':
        break

    lista_palabras.append(entrada)

letra = input('Ingresa la letra a buscar: ')

print('--- Contador de Repeticiones ---')
print(f'La letra {letra} se repite {contar_letra(lista_palabras, letra)} en {lista_palabras}')

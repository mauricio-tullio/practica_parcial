'''Racha ascendente más larga
Dificultad: Medio-difícil
Enunciado: Diseña una función que reciba una lista de enteros y retorne la longitud de la racha ascendente
consecutiva más larga.
Una racha ascendente ocurre cuando cada número es mayor que el anterior.
Por ejemplo, en [3, 5, 7, 2, 4, 6, 1] la respuesta es 3.
Qué habilidades practica: Análisis de secuencias, comparación entre vecinos, manejo de contadores y máximos.
Restricciones importantes: Si la lista está vacía, define claramente qué debe retornar.'''

def racha_ascendente(lista_enteros):
    if not lista_enteros:
        return 0

    racha = 1
    contador = 1

    for i in range(len(lista_enteros) - 1):
        if lista_enteros[i] < lista_enteros[i + 1]:
            contador += 1
        else:
            contador = 1
        if racha < contador:
            racha = contador
            
    return racha

lista = [3, 5, 7, 2, 4, 6, 1]
print(racha_ascendente(lista))
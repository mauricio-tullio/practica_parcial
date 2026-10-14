'''Compactar repeticiones consecutivas
Dificultad: Medio-difícil
Enunciado: Escribe una función que reciba una lista de enteros y construya una nueva lista donde cada grupo de
números consecutivos iguales se represente como dos elementos: el valor y la cantidad de veces seguidas que
apareció.
Por ejemplo, [4, 4, 4, 2, 2, 7] debe producir [4, 3, 2, 2, 7, 1].
Qué habilidades practica: Recorridos con índices, detección de cambios, agrupación, construcción estructurada
de resultados.
Restricciones importantes: No usar diccionarios ni librerías.'''

def contar_repetidos(lista_enteros):
    if not lista_enteros:
        return []

    resultado = []
    i = 0

    while i < len(lista_enteros):
        temp = lista_enteros[i]
        contador = 0
        j = i
        while j < len(lista_enteros) and lista_enteros[j] == temp:
            contador += 1
            j += 1
        resultado.append(temp)
        resultado.append(contador)
        i = j

    return resultado

lista = [4, 4, 4, 2, 2, 7]
print(f'ORIGINAL  | {lista}')
print(f'RESULTADO | {contar_repetidos(lista)}')

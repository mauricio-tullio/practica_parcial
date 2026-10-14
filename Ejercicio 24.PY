'''Palabras capicúas
Dificultad: Media
Enunciado: Crea una función que reciba una lista de palabras y retorne cuántas de ellas se leen igual de izquierda a
derecha que de derecha a izquierda.
Qué habilidades practica: Comparación de strings, uso de recorridos o estrategias de inversión, conteo.
Restricciones importantes: No usar slicing [::-1].'''

def palabra_capicua(lista_palabras):
    contador = 0
    lista_capi = []
    
    for palabra in lista_palabras:
        inverso = ''
        for i in range(len(palabra) - 1, -1, -1):
            inverso += palabra[i]
        if palabra == inverso:
            lista_capi.append(palabra)
            contador += 1

    return(contador, lista_capi)

lista_palabras = ["radar", "python", "anita", "hola", "reconocer", "oso"]

cantidad_capi, lista_capi = palabra_capicua(lista_palabras)
print(f'[{cantidad_capi}] | {lista_capi}')

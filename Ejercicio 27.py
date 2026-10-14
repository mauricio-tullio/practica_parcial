'''Clasificar longitudes de palabras
Dificultad: Media
Enunciado: Recibe una lista de palabras y construye una nueva lista de etiquetas con la misma cantidad de
elementos.
Para cada palabra, agrega:
- 'corta' si tiene menos de 5 letras,
- 'media' si tiene entre 5 y 8 letras,
- 'larga' si tiene más de 8 letras.
Qué habilidades practica: Transformación de listas, condicionales múltiples, uso de len().
Restricciones importantes: El resultado debe conservar el orden original.'''

def etiquetar_palabras(lista_palabras):
    etiquetas_palabras = []

    for palabra in lista_palabras:
        largo = len(palabra)
        if largo < 5:
            etiquetas_palabras.append('corta')
        elif 5 <= largo <= 8:
            etiquetas_palabras.append('media')
        else:
            etiquetas_palabras.append('larga')

    return etiquetas_palabras

lista_palabras = ["sol", "computadora", "gato", "universidad", "luz"]
etiquetas_palabras = etiquetar_palabras(lista_palabras)

for i in range(len(lista_palabras)):
    print(f'{lista_palabras[i]} | {etiquetas_palabras[i]}')
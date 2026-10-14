'''Emparejar nombres y notas finales
Dificultad: Medio-difícil

Guía de estudio - Programación 1

Preparación para el primer parcial

Enunciado: Recibes tres listas paralelas del mismo tamaño:
- nombres,
- nota1,
- nota2.
Debes construir una nueva lista de mensajes con el formato:
'Nombre: promedio X - aprobado/reprobado'
donde el promedio es la media aritmética de las dos notas y se aprueba con 10 o más.
Qué habilidades practica: Listas paralelas, promedio, construcción de strings, funciones de apoyo.
Restricciones importantes: Conservar el mismo orden de las listas.'''

def promedio_notas(Lista_nota1, lista_nota2):
    lista_promedio = []

    for i in range(len(Lista_nota1)):
        promedio = (Lista_nota1[i] + lista_nota2[i]) / 2
        lista_promedio.append(promedio)

    return lista_promedio

def aprobado(lista_nombre, lista_promedio):
    lista_final = []
    estado = ''

    for i in range(len(lista_nombre)):
        nombre = lista_nombre[i]
        promedio = lista_promedio[i]
        if lista_promedio[i] < 10:
            estado = 'reprobado'
        elif 10 <= lista_promedio[i] <= 20:
            estado = 'aprobado'

        resultado = f'{nombre}: promedio {promedio} - {estado}'
        lista_final.append(resultado)


    return lista_final

nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
nota1   = [12, 8, 10, 15, 6]
nota2   = [14, 9, 10, 11, 7]

lista_promedio = promedio_notas(nota1, nota2)
print(aprobado(nombres, lista_promedio))
        
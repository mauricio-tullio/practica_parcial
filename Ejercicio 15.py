'''Notas aprobadas
Dificultad: Fácil
Enunciado: Escribe una función que reciba una lista de notas y retorne una nueva lista con solo las notas
aprobadas.
Asume que una nota aprobada es mayor o igual a 10.
Qué habilidades practica: Filtrado, listas, append, condiciones, separación entre entrada y salida.
Restricciones importantes: Retornar una lista nueva; no imprimir el resultado dentro de la función.
'''

def aprobados(lista_notas):
    aprobados_lista = []

    for nota in lista_notas:
        if nota >= 10:
            aprobados_lista.append(nota)

    return aprobados_lista

lista_notas = []

print('--- Crear Lista de Notas ---')
while True:
    try:
        entrada = input('Ingresa la nota: ')

        if entrada == '':
            break

        entrada = float(entrada)
        lista_notas.append(entrada)
  
    except ValueError:
        print('Ingresa una nota valida')

print('--- Lista Aprobados ---')
print(f'Las notas aprobadas son {aprobados(lista_notas)}')
'''Reporte básico de asistencia
Dificultad: Media
Enunciado: En una lista se registra la asistencia de una estudiante durante varias clases usando 1 para asistió y 0
para faltó.
Crea funciones que permitan obtener:
- cuántas asistencias tuvo,
- cuántas faltas tuvo,
- si superó una asistencia mínima dada por parámetro.
Qué habilidades practica: Descomposición en funciones, conteo, lógica booleana, recorrido de listas.
Restricciones importantes: No resolver todo con una sola función.'''

def contar_asistencia(lista_asistencia):
    contador_asistencia = 0

    for asistencia in lista_asistencia:
        if asistencia == 1:
            contador_asistencia += 1

    return contador_asistencia

def contar_inasncistencia(lista_asistencia):
    contador_inascistencia = 0

    for asistencia in lista_asistencia:
        if asistencia == 0:
            contador_inascistencia += 1

    return contador_inascistencia

def asistencia_minima(lista_asistencia, dias):
    asistencias = contar_asistencia(lista_asistencia)
    return asistencias >= dias


clases_1 = [1, 1, 0, 1, 0, 1, 1]
print(f'ASISTENCIAS       | {clases_1}')
print(f'DIAS ASISTIDOS    | {contar_asistencia(clases_1)}')
print(f'DIAS INASCISTIDOS | {contar_inasncistencia(clases_1)}')
print(f'MINIMO 4 DIAS     | {asistencia_minima(clases_1, 4)}')


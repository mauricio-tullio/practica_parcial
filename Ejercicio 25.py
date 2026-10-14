'''Resumen de una semana de pasos
Dificultad: Media
Enunciado: Una aplicación guarda en una lista la cantidad de pasos caminados cada día de una semana.
Escribe funciones que permitan obtener:
- el total de pasos,
- el promedio diario,
- cuántos días superaron una meta dada por parámetro.
Qué habilidades practica: Descomposición en funciones, reutilización, acumulación, conteo, parámetros.
Restricciones importantes: Las funciones deben estar separadas; no resolver todo en una sola.'''

def total_pasos(lista_pasos):
    return sum(lista_pasos)

def promedio_pasos(lista_pasos):
    return total_pasos(lista_pasos) / len(lista_pasos)

def contador_objetivo(lsita_pasos, objetivo):
    contador = 0

    for pasos in lsita_pasos:
        if pasos >= objetivo:
            contador += 1

    return contador

pasos_semana = [8500, 10200, 6400, 11000, 12500, 4300, 9500]
meta_diaria = 10000

print('--- RESUMEN ---')

print(f'TOTAL {total_pasos(pasos_semana)}')
print(f'PROMEDIO DIARIO {promedio_pasos(pasos_semana)}')
print(f'CANTIDAD DE OBJETIVOS CUMPLIDOS {contador_objetivo(pasos_semana, meta_diaria)}')
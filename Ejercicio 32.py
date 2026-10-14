'''Procesar comandos simples sobre una lista
Dificultad: Media
Enunciado: Recibe una lista inicial vacía y otra lista de comandos de texto.
Los comandos posibles serán:
- 'AGREGAR x' para añadir un número al final,
- 'QUITAR' para eliminar el último elemento si la lista no está vacía.
Debes procesar todos los comandos en orden y retornar la lista final.
Qué habilidades practica: Métodos de listas, interpretación de instrucciones, validación simple, estado mutable.
Restricciones importantes: No usar eval() ni estructuras no vistas en clase.'''

lista_inicial = []
lista_comandos = []

print('--- Comandos Listas ---')
while True:
        entrada = input('Comandos AGREGAR x | QUITAR: ')

        if entrada == '':
            break

        dividir_entrada = entrada.split()

        if dividir_entrada[0].upper() == 'AGREGAR':
            numero = int(dividir_entrada[1])
            lista_inicial.append(numero)
            lista_comandos.append('AGREGAR')

        elif dividir_entrada[0].upper() == 'QUITAR':
            if len(lista_inicial) > 0:
                lista_inicial.pop()
                lista_comandos.append('QUITAR')

print('\n--- Resultados ---')
print(f'Comandos  |{lista_comandos}')
print(f'Resultado |{lista_inicial}')
                 
    

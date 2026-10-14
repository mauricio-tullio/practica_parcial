'''Precios con descuento
Dificultad: Media
Enunciado: Una tienda maneja dos listas paralelas: una con nombres de productos y otra con sus precios.
Crea una función que reciba ambas listas y retorne una nueva lista de precios finales donde:
- si el precio es mayor a 100, se aplica 10% de descuento;
- en caso contrario, el precio se mantiene igual.
Qué habilidades practica: Uso de listas paralelas, recorrido por índice, condiciones, construcción de resultados.
Restricciones importantes: Supón que ambas listas tienen el mismo tamaño.'''

def precio_final(lista_precios, lista_nombres):
    lista_precio_final = []

    for i in range(len(lista_nombres)):
        if lista_precios[i] > 100:
            lista_precio_final.append(lista_precios[i] * 0.9)
        else:
            lista_precio_final.append(lista_precios[i])

    return lista_precio_final

lista_nombres = []
lista_precios = []

print('--- Crear Listas ---')
while True:
    try:
        entrada_n = input('Ingrese el nombre del producto: ')

        if entrada_n == '':
            break

        lista_nombres.append(entrada_n)

        entrada_p = float(input(f'Ingresa el precio de {entrada_n}: '))
        lista_precios.append(entrada_p)

    except ValueError:
        print('Ingresa un numero valido')

print('\n--- Precios Finales ---')

lista_precio_final = precio_final(lista_precios, lista_nombres)

for a in range(len(lista_nombres)):
    print(f'NOMBRE: {lista_nombres[a]} | ORIGINAL: [{lista_precios[a]}] | NUEVO: [{lista_precio_final[a]}]')
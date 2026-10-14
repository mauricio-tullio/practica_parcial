'''Buscar un producto en inventario
Dificultad: Fácil
Enunciado: Escribe una función que reciba una lista de nombres de productos y un nombre objetivo.
La función debe retornar True si el producto existe en la lista y False en caso contrario.
Qué habilidades practica: Búsqueda lineal, comparación de strings, retorno booleano.
Restricciones importantes: Recorrer la lista con for.'''

def buscar_producto(lista_productos, busqueda):
    find = False

    for producto in lista_productos:
        if producto == busqueda:
            find = True
            break
    return find

lista_productos = []

print('--- Ingresar Productos ---')
while True:
        entrada = input('Ingrese el nombre del producto: ')

        if entrada == '':
            break

        lista_productos.append(entrada)

print('--- Buscar Productos ---')
while True:

    if len(lista_productos) == 0:
         print('No hay productos en la lista')
         break
    
    entrada = input('Ingrese el producto buscado: ')

    if entrada == '':
          break

    result = buscar_producto(lista_productos, entrada)
    
    if result:
        print(f'El producto {entrada} se encuentra en la lista')
    else:
        print(f'El producto {entrada} no se encuentra en la lista')
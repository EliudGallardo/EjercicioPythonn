inventario = [
    {"producto": "Laptop", "categoria": "Electrónica", "stock": 5},
    {"producto": "Mouse", "categoria": "Electrónica", "stock": 25},
    {"producto": "Silla", "categoria": "Muebles", "stock": 2},
    {"producto": "Escritorio", "categoria": "Muebles", "stock": 0}
]

productos_categoria = {}

for item in inventario:
    categoria = item["categoria"]
    producto = item["producto"]

    if categoria in productos_categoria:
        productos_categoria[categoria].append(producto)
    else:
        productos_categoria[categoria] = []
        productos_categoria[categoria].append(producto)

print("Productos por categoría:", productos_categoria)


productos_agotados = set()

for item in inventario:
    producto = item["producto"]
    stock = item["stock"]

    if stock == 0:
        productos_agotados.add(producto)

print("Productos agotados:", productos_agotados)


lista_bajo_stock = []

for item in inventario:
    producto = item["producto"]
    stock = item["stock"]

    if stock < 5:
        lista_bajo_stock.append(producto)

tupla_bajo_stock = tuple(lista_bajo_stock)

print("Productos con stock menor a 5:", tupla_bajo_stock)


total_por_categoria = {}

for item in inventario:
    categoria = item["categoria"]

    if categoria in total_por_categoria:
        total_por_categoria[categoria] += 1
    else:
        total_por_categoria[categoria] = 1

print("Total de productos por categoría:", total_por_categoria)

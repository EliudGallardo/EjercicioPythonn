ventas = [
    ("Ana", "Enero", "Laptop", 2, 15000),
    ("Luis", "Enero", "Mouse", 10, 250),
    ("Ana", "Febrero", "Laptop", 1, 15000),
    ("Luis", "Febrero", "Teclado", 5, 800),
    ("Ana", "Enero", "Mouse", 3, 250)
]

ingresos_empleado = {}

for venta in ventas:
    empleado = venta[0]
    cantidad = venta[3]
    precio = venta[4]
    total = cantidad * precio

    if empleado in ingresos_empleado:
        ingresos_empleado[empleado] += total
    else:
        ingresos_empleado[empleado] = total

print("Ingresos por empleado:", ingresos_empleado)


productos_unicos = set()

for venta in ventas:
    producto = venta[2]
    productos_unicos.add(producto)

print("Productos únicos vendidos:", productos_unicos)


ingresos_mes = {}

for venta in ventas:
    mes = venta[1]
    cantidad = venta[3]
    precio = venta[4]
    total = cantidad * precio

    if mes in ingresos_mes:
        ingresos_mes[mes] += total
    else:
        ingresos_mes[mes] = total

print("Ingresos por mes:", ingresos_mes)


# 4. Empleado con mayores ingresos
mayor_empleado = ""
mayor_ingreso = 0

for empleado, total in ingresos_empleado.items():
    if total > mayor_ingreso:
        mayor_ingreso = total
        mayor_empleado = empleado

print("Empleado con mayores ingresos:", mayor_empleado, "con", mayor_ingreso)

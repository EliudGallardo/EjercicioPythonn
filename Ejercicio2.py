asistencias = [
    ("Matemáticas", "Juan", "2024-09-01"),
    ("Matemáticas", "Ana", "2024-09-01"),
    ("Física", "Juan", "2024-09-01"),
    ("Matemáticas", "Juan", "2024-09-02"),
    ("Física", "Ana", "2024-09-02")
]

asistencia_materia = {}

for registro in asistencias:
    materia = registro[0]
    alumno = registro[1]

    if materia in asistencia_materia:
        asistencia_materia[materia].add(alumno)
    else:
        asistencia_materia[materia] = set()
        asistencia_materia[materia].add(alumno)

print("Asistencia por materia:", asistencia_materia)


dias_por_alumno = {}

for registro in asistencias:
    alumno = registro[1]
    fecha = registro[2]

    if alumno in dias_por_alumno:
        dias_por_alumno[alumno].add(fecha)
    else:
        dias_por_alumno[alumno] = set()
        dias_por_alumno[alumno].add(fecha)

print("Días distintos por alumno:", dias_por_alumno)

for alumno, fechas in dias_por_alumno.items():
    print(alumno, "asistió", len(fechas), "días distintos")


contador_asistencias = {}

for registro in asistencias:
    alumno = registro[1]

    if alumno in contador_asistencias:
        contador_asistencias[alumno] += 1
    else:
        contador_asistencias[alumno] = 1

mayor_alumno = ""
mayor_total = 0

for alumno, total in contador_asistencias.items():
    if total > mayor_total:
        mayor_total = total
        mayor_alumno = alumno

print("Alumno con más asistencias:", mayor_alumno, "con", mayor_total)

partidas = [
    ("Alex", "Bosque", 120),
    ("Luis", "Desierto", 90),
    ("Alex", "Bosque", 150),
    ("Ana", "Ciudad", 200),
    ("Luis", "Bosque", 110)
]

puntos_jugador = {}

for partida in partidas:
    jugador = partida[0]
    puntos = partida[2]

    if jugador in puntos_jugador:
        puntos_jugador[jugador] += puntos
    else:
        puntos_jugador[jugador] = puntos

print("Total de puntos por jugador:", puntos_jugador)


mapas_jugados = set()

for partida in partidas:
    mapa = partida[1]
    mapas_jugados.add(mapa)

print("Mapas jugados:", mapas_jugados)


contador_partidas = {}

for partida in partidas:
    jugador = partida[0]

    if jugador in contador_partidas:
        contador_partidas[jugador] += 1
    else:
        contador_partidas[jugador] = 1

promedio_jugador = {}

for jugador, total_puntos in puntos_jugador.items():
    promedio = total_puntos / contador_partidas[jugador]
    promedio_jugador[jugador] = promedio

print("Promedio de puntos por jugador:", promedio_jugador)


puntos_mapa = {}

for partida in partidas:
    mapa = partida[1]
    puntos = partida[2]

    if mapa in puntos_mapa:
        puntos_mapa[mapa] += puntos
    else:
        puntos_mapa[mapa] = puntos

mayor_mapa = ""
mayor_puntos = 0

for mapa, total in puntos_mapa.items():
    if total > mayor_puntos:
        mayor_puntos = total
        mayor_mapa = mapa

print("Mapa con más puntos:", mayor_mapa, "con", mayor_puntos)

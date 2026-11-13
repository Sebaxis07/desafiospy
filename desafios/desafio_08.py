# Desafío 08: Ranking de videojuegos
# Este programa procesa una serie de rondas jugadas y acumula los puntos totales de cada jugador.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

rondas = [
    ("Lucas", 150),
    ("Camila", 200),
    ("Lucas", 80),
    ("Camila", 120),
    ("Diego", 90)
]

def procesar_puntajes(lista_rondas):
    for jugador, puntos in lista_rondas:
        ranking = {}
        ranking[jugador] = ranking.get(jugador, 0) + puntos
    return ranking

def encontrar_lider(tabla_posiciones):
    return max(tabla_posiciones, key=tabla_posiciones.get)

tabla_final = procesar_puntajes(rondas)
lider = encontrar_lider(tabla_final)
print("Tabla acumulada:", tabla_final)
print("Lider del torneo:", lider)

# ---- Pruebas ----
assert tabla_final == {"Lucas": 230, "Camila": 320, "Diego": 90}, "La tabla de puntajes acumulados no es la esperada"
assert lider == "Camila", "El jugador con mayor puntaje acumulado no es el correcto"
print("Todas las pruebas pasaron")

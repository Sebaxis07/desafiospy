# Solución 08: Ranking de videojuegos
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 14, dentro de procesar_puntajes
# Qué pasa con el error: el diccionario de ranking se reinicia en cada pasada y solo conserva los puntos de la ultima ronda
# Cómo se arregla: mover la inicializacion ranking = {} antes del bucle for
# Pista: Observa dónde se declara el acumulador de puntajes en relacion al bucle.
# Salida esperada:
#   Tabla acumulada: {'Lucas': 230, 'Camila': 320, 'Diego': 90}
#   Lider del torneo: Camila
#   Todas las pruebas pasaron

rondas = [
    ("Lucas", 150),
    ("Camila", 200),
    ("Lucas", 80),
    ("Camila", 120),
    ("Diego", 90)
]

def procesar_puntajes(lista_rondas):
    ranking = {}
    for jugador, puntos in lista_rondas:
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

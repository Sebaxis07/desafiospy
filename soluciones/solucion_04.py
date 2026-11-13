# Solución 04: Podio de jugadores
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 8, dentro de obtener_podio
# Qué pasa con el error: el corte toma solo dos jugadores en lugar de los tres primeros lugares
# Cómo se arregla: cambiar "jugadores[0:2]" por "jugadores[0:3]"
# Pista: Recuerda que el límite superior en los cortes de listas no queda incluido.
# Salida esperada:
#   Primeros lugares: ['Matias', 'Camila', 'Rodrigo']
#   Todas las pruebas pasaron

jugadores_clasificados = ["Matias", "Camila", "Rodrigo", "Fernanda", "Gonzalo"]

def obtener_podio(jugadores):
    return jugadores[0:3]

def formato_medallero(podio):
    return f"Oro: {podio[0]}, Plata: {podio[1]}, Bronce: {podio[2]}"

podio = obtener_podio(jugadores_clasificados)
print("Primeros lugares:", podio)

# ---- Pruebas ----
assert len(podio) == 3, "El podio debe incluir exactamente tres jugadores"
assert podio == ["Matias", "Camila", "Rodrigo"], "Los integrantes del podio no son los esperados"
assert formato_medallero(podio) == "Oro: Matias, Plata: Camila, Bronce: Rodrigo", "El texto del medallero es incorrecto"
print("Todas las pruebas pasaron")

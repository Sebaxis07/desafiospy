# Desafío 04: Podio de jugadores
# Este programa recibe una lista ordenada de jugadores y extrae a los tres primeros lugares.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

jugadores_clasificados = ["Matias", "Camila", "Rodrigo", "Fernanda", "Gonzalo"]

def obtener_podio(jugadores):
    return jugadores[0:2]

def formato_medallero(podio):
    return f"Oro: {podio[0]}, Plata: {podio[1]}, Bronce: {podio[2]}"

podio = obtener_podio(jugadores_clasificados)
print("Primeros lugares:", podio)

# ---- Pruebas ----
assert len(podio) == 3, "El podio debe incluir exactamente tres jugadores"
assert podio == ["Matias", "Camila", "Rodrigo"], "Los integrantes del podio no son los esperados"
assert formato_medallero(podio) == "Oro: Matias, Plata: Camila, Bronce: Rodrigo", "El texto del medallero es incorrecto"
print("Todas las pruebas pasaron")

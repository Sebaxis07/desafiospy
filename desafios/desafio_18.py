# Desafío 18: Validador de becas estudiantiles
# Este programa evalúa postulaciones a una beca de mérito exigiendo buen rendimiento y alta asistencia.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

postulantes = [
    {"nombre": "Francisca", "promedio": 6.2, "asistencia": 90},
    {"nombre": "Tomas", "promedio": 3.8, "asistencia": 95},
    {"nombre": "Ignacia", "promedio": 5.8, "asistencia": 75},
    {"nombre": "Joaquin", "promedio": 5.6, "asistencia": 88}
]

def cumple_requisitos_beca(promedio, asistencia):
    nota_adecuada = promedio >= 5.5
    asistencia_adecuada = asistencia >= 85
    return nota_adecuada or asistencia_adecuada

def obtener_seleccionados(lista_alumnos):
    becados = []
    for alumno in lista_alumnos:
        if cumple_requisitos_beca(alumno["promedio"], alumno["asistencia"]):
            becados.append(alumno["nombre"])
    return becados

seleccionados = obtener_seleccionados(postulantes)
print("Total de postulantes:", len(postulantes))
print("Alumnos preseleccionados:", seleccionados)

# ---- Pruebas ----
assert seleccionados == ["Francisca", "Joaquin"], "La lista de alumnos preseleccionados no es la esperada"
assert len(seleccionados) == 2, "La cantidad de becados debe ser exactamente dos"
print("Todas las pruebas pasaron")

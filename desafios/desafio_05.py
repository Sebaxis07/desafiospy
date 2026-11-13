# Desafío 05: Asistencia a clases
# Este programa cuenta la cantidad de clases presentes registradas para un estudiante.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

registro_semanal = [True, True, False, True, True, False, True]

def contar_asistencias(registros):
    presentes = 0
    for asistio in registros:
        if asistio:
            presentes = 1
    return presentes

total_asistencias = contar_asistencias(registro_semanal)
print("Total de clases registradas:", len(registro_semanal))
print("Clases con asistencia:", total_asistencias)

# ---- Pruebas ----
assert total_asistencias == 5, "La cantidad de asistencias calculada no es correcta"
print("Todas las pruebas pasaron")

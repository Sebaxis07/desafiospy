# Solución 05: Asistencia a clases
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 11, dentro de contar_asistencias
# Qué pasa con el error: la variable se asigna en uno en cada coincidencia en lugar de ir sumando
# Cómo se arregla: cambiar "presentes = 1" por "presentes += 1"
# Pista: Revisa cómo se incrementa la variable que lleva la cuenta de asistencias.
# Salida esperada:
#   Total de clases registradas: 7
#   Clases con asistencia: 5
#   Todas las pruebas pasaron

registro_semanal = [True, True, False, True, True, False, True]

def contar_asistencias(registros):
    presentes = 0
    for asistio in registros:
        if asistio:
            presentes += 1
    return presentes

total_asistencias = contar_asistencias(registro_semanal)
print("Total de clases registradas:", len(registro_semanal))
print("Clases con asistencia:", total_asistencias)

# ---- Pruebas ----
assert total_asistencias == 5, "La cantidad de asistencias calculada no es correcta"
print("Todas las pruebas pasaron")

# Solución 12: Generador de turnos médicos
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 13, dentro de emitir_turnos
# Qué pasa con el error: se genera un turno menos del total exigido porque el rango se detiene antes
# Cómo se arregla: cambiar "range(1, cantidad)" por "range(1, cantidad + 1)"
# Pista: Recuerda que la función range no incluye su límite final.
# Salida esperada:
#   Box asignado: BOX
#   Turnos generados: ['BOX-01', 'BOX-02', 'BOX-03', 'BOX-04', 'BOX-05']
#   Todas las pruebas pasaron

box_atencion = "BOX"
total_pacientes = 5

def armar_codigo_turno(box, numero):
    return f"{box}-{numero:02d}"

def emitir_turnos(box, cantidad):
    turnos = []
    for num in range(1, cantidad + 1):
        turnos.append(armar_codigo_turno(box, num))
    return turnos

lista_turnos = emitir_turnos(box_atencion, total_pacientes)
print("Box asignado:", box_atencion)
print("Turnos generados:", lista_turnos)

# ---- Pruebas ----
assert len(lista_turnos) == 5, "La cantidad de turnos emitidos no coincide con los pacientes"
assert lista_turnos == ["BOX-01", "BOX-02", "BOX-03", "BOX-04", "BOX-05"], "La secuencia de turnos no es la esperada"
print("Todas las pruebas pasaron")

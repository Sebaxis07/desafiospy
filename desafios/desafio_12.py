# Desafío 12: Generador de turnos médicos
# Este programa genera una serie de códigos correlativos para la sala de atención de un centro de salud.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

box_atencion = "BOX"
total_pacientes = 5

def armar_codigo_turno(box, numero):
    return f"{box}-{numero:02d}"

def emitir_turnos(box, cantidad):
    turnos = []
    for num in range(1, cantidad):
        turnos.append(armar_codigo_turno(box, num))
    return turnos

lista_turnos = emitir_turnos(box_atencion, total_pacientes)
print("Box asignado:", box_atencion)
print("Turnos generados:", lista_turnos)

# ---- Pruebas ----
assert len(lista_turnos) == 5, "La cantidad de turnos emitidos no coincide con los pacientes"
assert lista_turnos == ["BOX-01", "BOX-02", "BOX-03", "BOX-04", "BOX-05"], "La secuencia de turnos no es la esperada"
print("Todas las pruebas pasaron")

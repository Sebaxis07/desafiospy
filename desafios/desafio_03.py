# Desafío 03: Control de acceso a evento
# Este programa revisa las edades de los asistentes y filtra a quienes cumplen con la edad minima.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

edades_invitados = [16, 21, 18, 15, 25, 17]
edad_minima = 18

def es_mayor_de_edad(edad, minima):
    return edad < minima

def filtrar_autorizados(edades, minima):
    return [e for e in edades if es_mayor_de_edad(e, minima)]

autorizados = filtrar_autorizados(edades_invitados, edad_minima)
print("Total invitados:", len(edades_invitados))
print("Invitados autorizados:", autorizados)

# ---- Pruebas ----
assert autorizados == [21, 18, 25], "La lista de personas autorizadas no es la esperada"
assert len(autorizados) == 3, "La cantidad de personas autorizadas no es la esperada"
print("Todas las pruebas pasaron")

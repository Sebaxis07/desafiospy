# Solución 03: Control de acceso a evento
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 9, dentro de es_mayor_de_edad
# Qué pasa con el error: se autoriza a los menores de edad y se deja afuera a los mayores
# Cómo se arregla: cambiar "edad < minima" por "edad >= minima"
# Pista: Observa el signo de comparacion usado para verificar la edad mínima requerida.
# Salida esperada:
#   Total invitados: 6
#   Invitados autorizados: [21, 18, 25]
#   Todas las pruebas pasaron

edades_invitados = [16, 21, 18, 15, 25, 17]
edad_minima = 18

def es_mayor_de_edad(edad, minima):
    return edad >= minima

def filtrar_autorizados(edades, minima):
    return [e for e in edades if es_mayor_de_edad(e, minima)]

autorizados = filtrar_autorizados(edades_invitados, edad_minima)
print("Total invitados:", len(edades_invitados))
print("Invitados autorizados:", autorizados)

# ---- Pruebas ----
assert autorizados == [21, 18, 25], "La lista de personas autorizadas no es la esperada"
assert len(autorizados) == 3, "La cantidad de personas autorizadas no es la esperada"
print("Todas las pruebas pasaron")

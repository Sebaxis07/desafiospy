# Desafío 17: Paquetes turísticos
# Este programa arma itinerarios turísticos personalizados agregando excursiones adicionales a un paquete base.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

paquete_estandar = ["hospedaje", "desayuno"]
excursiones_cliente_1 = ["tour_desierto"]
excursiones_cliente_2 = ["paseo_costanera"]

def crear_itinerario_cliente(base, adicionales):
    itinerario = base
    itinerario.extend(adicionales)
    return itinerario

def contar_servicios(itinerario):
    return len(itinerario)

def formato_resumen(cliente, itinerario):
    return f"{cliente}: {len(itinerario)} servicios incluidos"

itinerario_1 = crear_itinerario_cliente(paquete_estandar, excursiones_cliente_1)
itinerario_2 = crear_itinerario_cliente(paquete_estandar, excursiones_cliente_2)

print("Itinerario cliente 1:", itinerario_1)
print("Itinerario cliente 2:", itinerario_2)
print("Paquete base de referencia:", paquete_estandar)

# ---- Pruebas ----
assert itinerario_1 == ["hospedaje", "desayuno", "tour_desierto"], "El itinerario 1 contiene elementos incorrectos"
assert itinerario_2 == ["hospedaje", "desayuno", "paseo_costanera"], "El itinerario 2 contiene elementos incorrectos"
assert paquete_estandar == ["hospedaje", "desayuno"], "El paquete base fue alterado de forma no deseada"
print("Todas las pruebas pasaron")

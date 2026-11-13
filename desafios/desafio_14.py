# Desafío 14: Filtro de correos institucionales
# Este programa separa las cuentas de correo institucionales pertenecientes al dominio inacap.cl.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

correos_ingresados = [
    "juan.perez@inacap.cl",
    "contacto.empresa@gmail.com",
    "maria.gonzalez@inacap.cl",
    "soporte@inacap.com"
]

def es_correo_valido(correo, dominio):
    return correo.startswith(dominio)

def filtrar_institucionales(lista_correos, dominio):
    return [c for c in lista_correos if es_correo_valido(c, dominio)]

dominio_institucional = "@inacap.cl"
cuentas_validas = filtrar_institucionales(correos_ingresados, dominio_institucional)
print("Cuentas ingresadas:", len(correos_ingresados))
print("Cuentas institucionales encontradas:", cuentas_validas)

# ---- Pruebas ----
assert len(cuentas_validas) == 2, "La cantidad de correos institucionales no es la correcta"
assert cuentas_validas == ["juan.perez@inacap.cl", "maria.gonzalez@inacap.cl"], "La lista de correos filtrados es incorrecta"
print("Todas las pruebas pasaron")

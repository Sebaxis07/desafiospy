# Solución 14: Filtro de correos institucionales
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 13, dentro de es_correo_valido
# Qué pasa con el error: la lista de validos queda vacia porque se comprueba el inicio del texto en vez de la terminacion
# Cómo se arregla: cambiar "startswith(dominio)" por "endswith(dominio)"
# Pista: Observa en qué parte de la dirección de correo electrónico se ubica el dominio institucional.
# Salida esperada:
#   Cuentas ingresadas: 4
#   Cuentas institucionales encontradas: ['juan.perez@inacap.cl', 'maria.gonzalez@inacap.cl']
#   Todas las pruebas pasaron

correos_ingresados = [
    "juan.perez@inacap.cl",
    "contacto.empresa@gmail.com",
    "maria.gonzalez@inacap.cl",
    "soporte@inacap.com"
]

def es_correo_valido(correo, dominio):
    return correo.endswith(dominio)

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

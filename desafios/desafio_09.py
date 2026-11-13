# Desafío 09: Validador de contraseñas
# Este programa valida si una clave de usuario tiene largo suficiente y al menos un dígito numérico.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

claves_a_probar = ["secreto", "antofagasta2026", "clave1"]

def tiene_digito(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
        return False
    return False

def clave_es_valida(clave):
    largo_correcto = len(clave) >= 8
    contiene_numero = tiene_digito(clave)
    return largo_correcto and contiene_numero

resultados = [clave_es_valida(c) for c in claves_a_probar]
print("Claves probadas:", claves_a_probar)
print("Resultados de validacion:", resultados)

# ---- Pruebas ----
assert resultados == [False, True, False], "Los resultados de validacion no coinciden con las reglas exigidas"
print("Todas las pruebas pasaron")

# Solución 09: Validador de contraseñas
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 11, dentro de tiene_digito
# Qué pasa con el error: la funcion termina en la primera letra y no alcanza a revisar el resto de la clave
# Cómo se arregla: eliminar el return False interno para que solo retorne False al finalizar el bucle
# Pista: Observa si la funcion esta revisando todos los caracteres antes de concluir que no hay digitos.
# Salida esperada:
#   Claves probadas: ['secreto', 'antofagasta2026', 'clave1']
#   Resultados de validacion: [False, True, False]
#   Todas las pruebas pasaron

claves_a_probar = ["secreto", "antofagasta2026", "clave1"]

def tiene_digito(cadena):
    for caracter in cadena:
        if caracter.isdigit():
            return True
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

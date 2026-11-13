# Solución 02: Registro de temperaturas
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 8, dentro de convertir_a_fahrenheit
# Qué pasa con el error: las temperaturas calculadas son mucho menores porque la fraccion de conversion esta invertida
# Cómo se arregla: cambiar "(celsius * 5 / 9) + 32" por "(celsius * 9 / 5) + 32"
# Pista: Revisa la proporcion matemática entre las escalas Celsius y Fahrenheit.
# Salida esperada:
#   Temperaturas en Celsius: [15, 20, 25]
#   Temperaturas en Fahrenheit: [59.0, 68.0, 77.0]
#   Todas las pruebas pasaron

temperaturas_celsius = [15, 20, 25]

def convertir_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def convertir_todas(mediciones):
    return [round(convertir_a_fahrenheit(t), 1) for t in mediciones]

temperaturas_f = convertir_todas(temperaturas_celsius)
print("Temperaturas en Celsius:", temperaturas_celsius)
print("Temperaturas en Fahrenheit:", temperaturas_f)

# ---- Pruebas ----
assert temperaturas_f == [59.0, 68.0, 77.0], "Las temperaturas convertidas no coinciden"
print("Todas las pruebas pasaron")

# Desafío 02: Registro de temperaturas
# Este programa convierte una lista de temperaturas tomadas en Antofagasta de Celsius a Fahrenheit.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

temperaturas_celsius = [15, 20, 25]

def convertir_a_fahrenheit(celsius):
    return (celsius * 5 / 9) + 32

def convertir_todas(mediciones):
    return [round(convertir_a_fahrenheit(t), 1) for t in mediciones]

temperaturas_f = convertir_todas(temperaturas_celsius)
print("Temperaturas en Celsius:", temperaturas_celsius)
print("Temperaturas en Fahrenheit:", temperaturas_f)

# ---- Pruebas ----
assert temperaturas_f == [59.0, 68.0, 77.0], "Las temperaturas convertidas no coinciden"
print("Todas las pruebas pasaron")

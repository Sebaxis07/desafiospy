# Desafío 11: Control de peaje
# Este programa calcula la recaudación total de una caseta de peaje según el paso de diferentes vehículos.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

tarifas = {"moto": 500, "auto": 1200, "camion": 3000}
vehiculos_dia = ["auto", "moto", "camion", "auto", "camion"]

def obtener_tarifa(tabla_tarifas, tipo_vehiculo):
    return tabla_tarifas.get(tipo_vehiculo, 0)

def calcular_recaudacion(tabla_tarifas, lista_vehiculos):
    total = 0
    for v in lista_vehiculos[1:]:
        total += obtener_tarifa(tabla_tarifas, v)
    return total

def resumen_diario(total, cantidad):
    return f"Recaudacion: {total} en {cantidad} vehiculos"

total_recaudado = calcular_recaudacion(tarifas, vehiculos_dia)
informe = resumen_diario(total_recaudado, len(vehiculos_dia))
print(informe)

# ---- Pruebas ----
assert total_recaudado == 8900, "La recaudacion total calculada no es correcta"
assert informe == "Recaudacion: 8900 en 5 vehiculos", "El texto del informe no es el esperado"
print("Todas las pruebas pasaron")

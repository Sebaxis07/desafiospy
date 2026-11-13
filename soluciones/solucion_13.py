# Solución 13: Rendimiento de combustible
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 10, dentro de calcular_rendimiento
# Qué pasa con el error: la division esta invertida y entrega litros por kilometro en vez de kilometros por litro
# Cómo se arregla: cambiar "litros / km" por "km / litros"
# Pista: Verifica qué magnitud debe ir en el numerador para obtener kilómetros por litro.
# Salida esperada:
#   Rendimiento calculado (km por litro): 15.0
#   Costo estimado para 300 km: 22000
#   Todas las pruebas pasaron

kilometros_recorridos = 450
litros_consumidos = 30
precio_por_litro = 1100

def calcular_rendimiento(km, litros):
    return km / litros

def costo_viaje_futuro(km_estimados, rendimiento, valor_litro):
    litros_necesarios = km_estimados / rendimiento
    return round(litros_necesarios * valor_litro)

eficiencia = calcular_rendimiento(kilometros_recorridos, litros_consumidos)
gasto_viaje = costo_viaje_futuro(300, eficiencia, precio_por_litro)
print("Rendimiento calculado (km por litro):", round(eficiencia, 2))
print("Costo estimado para 300 km:", gasto_viaje)

# ---- Pruebas ----
assert round(eficiencia, 2) == 15.0, "El rendimiento de combustible en km por litro no es correcto"
assert gasto_viaje == 22000, "El costo proyectado del viaje no es el esperado"
print("Todas las pruebas pasaron")

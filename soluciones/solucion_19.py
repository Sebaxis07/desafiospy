# Solución 19: Buscador de stock crítico
# Tipo: Error de lógica
# Dificultad: 3
# Dónde está el error: línea 16, dentro de hay_algun_producto_critico
# Qué pasa con el error: la funcion retorna False en el primer producto revisado sin examinar el resto del inventario
# Cómo se arregla: eliminar la clausula else con su return False para que no corte el bucle
# Pista: Observa si la función termina de revisar la bodega completa antes de decir que no hay stock crítico.
# Salida esperada:
#   Estado de bodega: ALERTA: Se requiere reposicion inmediata
#   Todas las pruebas pasaron

bodega_tienda = [
    {"producto": "cables", "unidades": 15},
    {"producto": "conectores", "unidades": 3},
    {"producto": "router", "unidades": 8}
]
umbral_minimo = 5

def hay_algun_producto_critico(inventario, limite):
    for item in inventario:
        if item["unidades"] < limite:
            return True
    return False

def categorizar_alerta(existe_critico):
    return "ALERTA: Se requiere reposicion inmediata" if existe_critico else "Stock en niveles normales"

alerta_activa = hay_algun_producto_critico(bodega_tienda, umbral_minimo)
mensaje_estado = categorizar_alerta(alerta_activa)
print("Estado de bodega:", mensaje_estado)

# ---- Pruebas ----
assert alerta_activa is True, "Se debio detectar al menos un producto bajo el limite de seguridad"
assert mensaje_estado == "ALERTA: Se requiere reposicion inmediata", "El mensaje de alerta no coincide con el estado del stock"
print("Todas las pruebas pasaron")

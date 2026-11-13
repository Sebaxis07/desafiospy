# Desafío 19: Buscador de stock crítico
# Este programa revisa si en una bodega existe al menos un insumo con existencia bajo el umbral de seguridad.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

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
        else:
            return False
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

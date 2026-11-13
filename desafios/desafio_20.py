# Desafío 20: Simulador de caja registradora
# Este programa liquida la cuenta de un restaurante aplicando descuento por cliente frecuente y propina sugerida.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

consumo_mesa = 25000
porcentaje_descuento = 10
porcentaje_propina = 10

def calcular_monto_descuento(monto, porcentaje):
    return round(monto * (porcentaje / 100))

def calcular_propina_sugerida(subtotal, porcentaje):
    return round(subtotal * (porcentaje / 100))

def liquidar_cuenta(consumo, pct_dcto, pct_propina):
    descuento = calcular_monto_descuento(consumo, pct_dcto)
    subtotal = consumo + descuento
    propina = calcular_propina_sugerida(subtotal, pct_propina)
    total_a_pagar = subtotal + propina
    return subtotal, propina, total_a_pagar

subtotal, propina, total = liquidar_cuenta(consumo_mesa, porcentaje_descuento, porcentaje_propina)
print("Consumo inicial:", consumo_mesa)
print("Subtotal con beneficio:", subtotal)
print("Propina sugerida:", propina)
print("Total definitivo a pagar:", total)

# ---- Pruebas ----
assert subtotal == 22500, "El subtotal despues de aplicar el descuento no es el esperado"
assert propina == 2250, "La propina calculada sobre el subtotal no coincide"
assert total == 24750, "El total final a pagar no es el correcto"
print("Todas las pruebas pasaron")

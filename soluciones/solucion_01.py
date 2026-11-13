# Solución 01: Carrito de compras
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 12, dentro de aplicar_descuento
# Qué pasa con el error: el total queda con valor negativo porque a la rebaja se le resta el subtotal
# Cómo se arregla: restar descuento al subtotal en vez de restar subtotal al descuento
# Pista: Fíjate en qué valor se resta de cuál al calcular el monto con descuento.
# Salida esperada:
#   Subtotal: 9500
#   Total con descuento: 8000
#   Todas las pruebas pasaron

precios = [4500, 1200, 3800]
descuento_fijo = 1500

def calcular_subtotal(lista_precios):
    return sum(lista_precios)

def aplicar_descuento(subtotal, rebaja):
    return subtotal - rebaja

subtotal = calcular_subtotal(precios)
total_final = aplicar_descuento(subtotal, descuento_fijo)
print("Subtotal:", subtotal)
print("Total con descuento:", total_final)

# ---- Pruebas ----
assert subtotal == 9500, "El subtotal no es el esperado"
assert total_final == 8000, "El total con descuento no es el esperado"
print("Todas las pruebas pasaron")

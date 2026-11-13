# Desafío 01: Carrito de compras
# Este programa calcula el valor final a pagar aplicando un descuento fijo a los productos.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

precios = [4500, 1200, 3800]
descuento_fijo = 1500

def calcular_subtotal(lista_precios):
    return sum(lista_precios)

def aplicar_descuento(subtotal, rebaja):
    return rebaja - subtotal

subtotal = calcular_subtotal(precios)
total_final = aplicar_descuento(subtotal, descuento_fijo)
print("Subtotal:", subtotal)
print("Total con descuento:", total_final)

# ---- Pruebas ----
assert subtotal == 9500, "El subtotal no es el esperado"
assert total_final == 8000, "El total con descuento no es el esperado"
print("Todas las pruebas pasaron")

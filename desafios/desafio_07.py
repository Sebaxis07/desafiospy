# Desafío 07: Boleta de farmacia
# Este programa calcula el costo total de una compra en farmacia a partir de los precios del catálogo.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

catalogo_precios = {
    "paracetamol": 1200,
    "ibuprofeno": 1800,
    "alcohol": "2500",
    "gasas": 900
}
pedido = ["paracetamol", "alcohol", "gasas"]

def obtener_precio(catalogo, medicamento):
    return catalogo[medicamento]

def calcular_total_pedido(catalogo, lista_articulos):
    total = 0
    for item in lista_articulos:
        total += obtener_precio(catalogo, item)
    return total

total_compra = calcular_total_pedido(catalogo_precios, pedido)
print("Medicamentos pedidos:", pedido)
print("Total de la boleta:", total_compra)

# ---- Pruebas ----
assert total_compra == 4600, "El valor total de la boleta no es el esperado"
print("Todas las pruebas pasaron")

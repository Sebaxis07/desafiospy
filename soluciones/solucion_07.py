# Solución 07: Boleta de farmacia
# Tipo: Error de tipo
# Dificultad: 2
# Dónde está el error: línea 8, en el diccionario catalogo_precios
# Qué pasa con el error: el programa lanza TypeError porque uno de los precios esta guardado como texto y no como numero
# Cómo se arregla: cambiar el valor de texto "2500" por el numero 2500
# Pista: Verifica que todos los valores del catalogo sean de tipo numerico.
# Salida esperada:
#   Medicamentos pedidos: ['paracetamol', 'alcohol', 'gasas']
#   Total de la boleta: 4600
#   Todas las pruebas pasaron

catalogo_precios = {
    "paracetamol": 1200,
    "ibuprofeno": 1800,
    "alcohol": 2500,
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

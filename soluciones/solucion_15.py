# Solución 15: Préstamos de biblioteca
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 15, dentro de calcular_multa_libro
# Qué pasa con el error: la condicion cobra multa cuando los dias de retraso son negativos y entrega un total erroneo
# Cómo se arregla: cambiar "dias_retraso < 0" por "dias_retraso > 0"
# Pista: Analiza cuándo corresponde aplicar la sanción monetaria por retraso.
# Salida esperada:
#   Libros revisados: 3
#   Multa total a cobrar: 2500
#   Todas las pruebas pasaron

prestamos = [
    {"titulo": "Algoritmos", "dias_prestamo": 10},
    {"titulo": "Redes", "dias_prestamo": 5},
    {"titulo": "Bases de Datos", "dias_prestamo": 9}
]
dias_limite = 7
tarifa_por_dia = 500

def calcular_multa_libro(dias_usados, limite, costo_diario):
    dias_retraso = dias_usados - limite
    if dias_retraso > 0:
        return dias_retraso * costo_diario
    return 0

def calcular_multa_total(lista_libros, limite, tarifa):
    total = 0
    for item in lista_libros:
        total += calcular_multa_libro(item["dias_prestamo"], limite, tarifa)
    return total

multa_final = calcular_multa_total(prestamos, dias_limite, tarifa_por_dia)
print("Libros revisados:", len(prestamos))
print("Multa total a cobrar:", multa_final)

# ---- Pruebas ----
assert multa_final == 2500, "El valor de la multa total acumulada no es el esperado"
print("Todas las pruebas pasaron")

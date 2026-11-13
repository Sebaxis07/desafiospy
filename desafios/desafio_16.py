# Desafío 16: Libro de notas universitarias
# Este programa calcula el promedio ponderado de una asignatura según los pesos de cátedra y laboratorio.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

notas_catedra = [4.5, 5.5, 5.0]
notas_laboratorio = [6.0, 5.0]
ponderacion_catedra = 70

def calcular_promedio_simple(notas):
    return sum(notas) / len(notas)

def calcular_nota_final(prom_catedra, prom_lab, peso_cat_porcentaje):
    factor_catedra = peso_cat_porcentaje
    factor_lab = 1 - factor_catedra
    return round(prom_catedra * factor_catedra + prom_lab * factor_lab, 1)

def determinar_estado(nota_definitiva):
    return "Aprobado" if nota_definitiva >= 4.0 else "Reprobado"

prom_cat = calcular_promedio_simple(notas_catedra)
prom_lab = calcular_promedio_simple(notas_laboratorio)
nota_final = calcular_nota_final(prom_cat, prom_lab, ponderacion_catedra)
estado = determinar_estado(nota_final)

print("Promedio catedra:", round(prom_cat, 1))
print("Promedio laboratorio:", round(prom_lab, 1))
print("Nota final:", nota_final)
print("Situacion academica:", estado)

# ---- Pruebas ----
assert round(prom_cat, 1) == 5.0, "El promedio de catedras no es el esperado"
assert round(prom_lab, 1) == 5.5, "El promedio de laboratorios no es el esperado"
assert nota_final == 5.2, "La nota final ponderada no coincide con el calculo correcto"
assert estado == "Aprobado", "El estado academico calculado es incorrecto"
print("Todas las pruebas pasaron")

# Desafío 06: Formato de nombres
# Este programa estandariza nombres de estudiantes dejándolos con la primera letra en mayúscula.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

lista_ingresada = ["carlos", "MARIA", "pAbLo"]

def corregir_nombre(nombre):
    limpio = nombre.lower()
    return limpio[1].upper() + limpio[1:]

def limpiar_lista(nombres):
    return [corregir_nombre(n) for n in nombres]

nombres_listos = limpiar_lista(lista_ingresada)
print("Nombres originales:", lista_ingresada)
print("Nombres corregidos:", nombres_listos)

# ---- Pruebas ----
assert nombres_listos == ["Carlos", "Maria", "Pablo"], "Los nombres corregidos no coinciden con el formato esperado"
print("Todas las pruebas pasaron")

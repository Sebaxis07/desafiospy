# Solución 06: Formato de nombres
# Tipo: Error de lógica
# Dificultad: 1
# Dónde está el error: línea 9, dentro de corregir_nombre
# Qué pasa con el error: se toma la segunda letra para convertirla a mayuscula en vez de la inicial
# Cómo se arregla: cambiar "limpio[1].upper()" por "limpio[0].upper()"
# Pista: Recuerda en qué posición comienza el primer carácter de una cadena.
# Salida esperada:
#   Nombres originales: ['carlos', 'MARIA', 'pAbLo']
#   Nombres corregidos: ['Carlos', 'Maria', 'Pablo']
#   Todas las pruebas pasaron

lista_ingresada = ["carlos", "MARIA", "pAbLo"]

def corregir_nombre(nombre):
    limpio = nombre.lower()
    return limpio[0].upper() + limpio[1:]

def limpiar_lista(nombres):
    return [corregir_nombre(n) for n in nombres]

nombres_listos = limpiar_lista(lista_ingresada)
print("Nombres originales:", lista_ingresada)
print("Nombres corregidos:", nombres_listos)

# ---- Pruebas ----
assert nombres_listos == ["Carlos", "Maria", "Pablo"], "Los nombres corregidos no coinciden con el formato esperado"
print("Todas las pruebas pasaron")

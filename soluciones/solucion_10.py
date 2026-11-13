# Solución 10: Agenda de contactos
# Tipo: Error de lógica
# Dificultad: 2
# Dónde está el error: línea 12, dentro de normalizar_nombre
# Qué pasa con el error: la busqueda devuelve None porque transforma a mayusculas mientras que la agenda usa minusculas
# Cómo se arregla: cambiar "upper()" por "lower()" en la normalizacion
# Pista: Compara el formato de las claves del directorio con la transformacion que hace la funcion.
# Salida esperada:
#   Telefono encontrado: 912345678
#   Todas las pruebas pasaron

directorio = {
    "carlos": 987654321,
    "marcela": 912345678,
    "patricio": 955443322
}

def normalizar_nombre(nombre):
    return nombre.strip().lower()

def consultar_telefono(agenda, nombre_buscado):
    clave = normalizar_nombre(nombre_buscado)
    return agenda.get(clave, None)

def formato_contacto(nombre, fono):
    return f"{nombre.capitalize()}: {fono}"

telefono_encontrado = consultar_telefono(directorio, "Marcela")
print("Telefono encontrado:", telefono_encontrado)

# ---- Pruebas ----
assert telefono_encontrado == 912345678, "El telefono obtenido no corresponde al contacto buscado"
assert formato_contacto("marcela", telefono_encontrado) == "Marcela: 912345678", "El formato del contacto no es el esperado"
print("Todas las pruebas pasaron")

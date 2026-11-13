# Desafío 10: Agenda de contactos
# Este programa busca contactos en una agenda telefónica ignorando mayúsculas y minúsculas.
# Tiene un error. Encuéntralo y arréglalo hasta que las pruebas pasen.

directorio = {
    "carlos": 987654321,
    "marcela": 912345678,
    "patricio": 955443322
}

def normalizar_nombre(nombre):
    return nombre.strip().upper()

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

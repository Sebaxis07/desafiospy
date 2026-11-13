"""
Script de verificacion para los 20 pares de desafios y soluciones de la Gymkana Informatica 2026.
Comprueba que cada archivo se ejecute de manera aislada con -I, valide sus pruebas y contenga exactamente un error.
"""

import difflib
import os
import re
import subprocess
import sys

VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"

EMOJI_PATTERN = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)


def extraer_salida_esperada(lineas_solucion):
    lineas_salida = []
    en_seccion_salida = False
    for l in lineas_solucion:
        if l.strip() == "# Salida esperada:":
            en_seccion_salida = True
            continue
        if en_seccion_salida:
            if l.startswith("#   "):
                lineas_salida.append(l[4:])
            elif l.startswith("#"):
                # Otra linea de comentario que no es de salida
                break
            else:
                # Comienza el codigo
                break
    return "\n".join(lineas_salida)


def extraer_codigo_puro(lineas):
    indice = 0
    while indice < len(lineas) and (lineas[indice].startswith("#") or not lineas[indice].strip()):
        indice += 1
    return [l.rstrip("\r\n") for l in lineas[indice:] if l.strip()]


def verificar_par(id_num):
    str_id = f"{id_num:02d}"
    des_path = os.path.join("desafios", f"desafio_{str_id}.py")
    sol_path = os.path.join("soluciones", f"solucion_{str_id}.py")

    if not os.path.exists(des_path):
        return False, f"Falta el archivo {des_path}"
    if not os.path.exists(sol_path):
        return False, f"Falta el archivo {sol_path}"

    with open(des_path, "r", encoding="utf-8") as f:
        des_lineas = f.read().splitlines()

    with open(sol_path, "r", encoding="utf-8") as f:
        sol_lineas = f.read().splitlines()

    # Validar estilo de comentarios de la solucion
    for n_linea, l in enumerate(sol_lineas, 1):
        if l.startswith("#"):
            if ";" in l:
                return False, f"Punto y coma encontrado en comentario linea {n_linea} de {sol_path}"
            if re.search(r'[\u2013\u2014]', l) or re.search(r'\s-\s', l):
                return False, f"Raya o guion como puntuacion en comentario linea {n_linea} de {sol_path}"
            if EMOJI_PATTERN.search(l):
                return False, f"Emoji detectado en linea {n_linea} de {sol_path}"

    # 1. Ejecutar solucion en proceso aparte
    try:
        proc_sol = subprocess.run(
            [sys.executable, "-I", sol_path],
            capture_output=True,
            text=True,
            timeout=5
        )
    except subprocess.TimeoutExpired:
        return False, "La solucion excedio el tiempo limite de 5 segundos"

    if proc_sol.returncode != 0:
        return False, f"La solucion fallo al ejecutarse: {proc_sol.stderr.strip()}"

    salida_sol = proc_sol.stdout.rstrip("\r\n")
    if not salida_sol.endswith("Todas las pruebas pasaron"):
        return False, "La solucion no finalizo con el mensaje 'Todas las pruebas pasaron'"

    salida_esperada = extraer_salida_esperada(sol_lineas)
    if salida_esperada and salida_sol != salida_esperada:
        return False, f"La salida de la solucion no coincide con la salida esperada declarada.\nEsperada:\n{salida_esperada}\nReal:\n{salida_sol}"

    # 2. Ejecutar desafio en proceso aparte
    try:
        proc_des = subprocess.run(
            [sys.executable, "-I", des_path],
            capture_output=True,
            text=True,
            timeout=5
        )
    except subprocess.TimeoutExpired:
        return False, "El desafio excedio el tiempo limite de 5 segundos"

    salida_des = proc_des.stdout.rstrip("\r\n")
    # El desafio NO debe terminar con 'Todas las pruebas pasaron'
    if proc_des.returncode == 0 and "Todas las pruebas pasaron" in salida_des:
        return False, "El desafio con error paso las pruebas cuando debia fallar"

    # 3. Comprobar que difieren en un solo cambio (un unico error)
    cod_des = extraer_codigo_puro(des_lineas)
    cod_sol = extraer_codigo_puro(sol_lineas)

    diff = list(difflib.unified_diff(cod_des, cod_sol, lineterm=""))
    hunks = [l for l in diff if l.startswith("@@")]
    if len(hunks) != 1:
        return False, f"Se esperaban cambios en exactamente 1 bloque de codigo, pero se encontraron {len(hunks)}"

    return True, "OK"


def main():
    print("Iniciando verificacion de desafios y soluciones...\n")
    total = 20
    pasaron = 0

    for i in range(1, total + 1):
        ok, detalle = verificar_par(i)
        str_id = f"{i:02d}"
        if ok:
            print(f"Desafío {str_id}: {VERDE}OK{RESET}")
            pasaron += 1
        else:
            print(f"Desafío {str_id}: {ROJO}FALLÓ ({detalle}){RESET}")

    print("\n" + "=" * 45)
    print(f"Resultado final: {pasaron} de {total} desafíos pasaron la verificación.")
    print("=" * 45)

    if pasaron == total:
        print(f"\n{VERDE}Todos los 20 desafíos están en OK.{RESET}")
        return 0
    else:
        print(f"\n{ROJO}Algunos desafíos no pasaron la verificación.{RESET}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

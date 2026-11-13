# Gymkana Informática 2026: Desafíos de Python
### INACAP Sede Antofagasta: Semana de la Carrera de Informática

Repositorio oficial con los 20 desafíos de programación en Python preparados para el puesto de gymkana de la Semana de la Carrera 2026.

Cada desafío presenta un mini programa real, funcional y autocontenido que contiene exactamente un error en su lógica o tipos de datos. El participante debe analizar el código, ejecutarlo, identificar la falla y corregirla hasta que todas las pruebas integradas en el propio archivo pasen de forma exitosa.

---

## Estructura del Proyecto

```text
gymcana inform/
├── desafios/
│   ├── desafio_01.py
│   ├── desafio_02.py
│   ├── ...
│   └── desafio_20.py
├── soluciones/
│   ├── solucion_01.py
│   ├── solucion_02.py
│   ├── ...
│   └── solucion_20.py
├── verificar.py
└── README.md
```

### Descripción de Carpetas y Archivos

* **`desafios/`**: archivos que se entregan a los participantes. Cada archivo incluye un encabezado con el título y la descripción del problema, el código fuente con el error y un bloque final `# ---- Pruebas ----` con aserciones (`assert`).
* **`soluciones/`**: archivos de referencia para el equipo organizador y staff. Contienen el código corregido junto con un bloque de metadatos que detalla la línea exacta del error, qué ocurre, cómo se soluciona, una pista neutral y la salida esperada por consola.
* **`verificar.py`**: script de pruebas automatizadas que ejecuta cada solución y desafío en subprocesos independientes con banderas de aislamiento (`-I`), asegurando que las 20 soluciones pasen y que los 20 desafíos difieran en exactamente un cambio puntual.

---

## Dinámica de Participación

1. **Selección del desafío**: el participante recibe o elige un archivo desde la carpeta `desafios/`.
2. **Lectura y ejecución**: ejecuta el script en la terminal para observar el comportamiento erróneo o la falla de las aserciones:
   ```bash
   python desafios/desafio_01.py
   ```
3. **Depuración**: examina el código fuente y razona sobre el flujo de datos. Si el participante se encuentra bloqueado, el staff puede facilitarle la pista incluida en la cabecera de la solución correspondiente.
4. **Validación**: una vez realizada la corrección, vuelve a ejecutar el archivo. El desafío se considera superado cuando se imprime por pantalla:
   ```text
   Todas las pruebas pasaron
   ```
5. **Tiempo estimado**: entre 5 y 7 minutos por desafío.

---

## Catálogo de Desafíos

| N° | Título | Temática | Dificultad | Tipo de Error |
|:---:|---|---|:---:|---|
| 01 | Carrito de compras | Cálculo de subtotal y descuento fijo | 1 (Fácil) | Error de lógica |
| 02 | Registro de temperaturas | Conversión de Celsius a Fahrenheit | 1 (Fácil) | Error de lógica |
| 03 | Control de acceso a evento | Filtrado de asistentes por mayoría de edad | 1 (Fácil) | Error de lógica |
| 04 | Podio de jugadores | Extracción de los tres mejores lugares | 1 (Fácil) | Error de lógica |
| 05 | Asistencia a clases | Conteo de asistencias en registros booleanos | 1 (Fácil) | Error de lógica |
| 06 | Formato de nombres | Capitalización de cadenas de texto | 1 (Fácil) | Error de lógica |
| 07 | Boleta de farmacia | Suma de precios con datos desde catálogo | 2 (Medio) | Error de tipo |
| 08 | Ranking de videojuegos | Acumulación de puntajes por jugador | 2 (Medio) | Error de lógica |
| 09 | Validador de contraseñas | Validación de largo y dígitos numéricos | 2 (Medio) | Error de lógica |
| 10 | Agenda de contactos | Búsqueda por nombre insensible a mayúsculas | 2 (Medio) | Error de lógica |
| 11 | Control de peaje | Cálculo de recaudación según tipo de vehículo | 2 (Medio) | Error de lógica |
| 12 | Generador de turnos médicos | Emisión de códigos correlativos para boxes | 2 (Medio) | Error de lógica |
| 13 | Rendimiento de combustible | Eficiencia de km por litro y costo de viaje | 2 (Medio) | Error de lógica |
| 14 | Filtro de correos institucionales | Filtrado de correos con dominio institucional | 2 (Medio) | Error de lógica |
| 15 | Préstamos de biblioteca | Cálculo de multas por días de retraso | 2 (Medio) | Error de lógica |
| 16 | Libro de notas universitarias | Promedio ponderado de cátedras y talleres | 3 (Desafiante) | Error de lógica |
| 17 | Paquetes turísticos | Itinerarios personalizados sin mutar la base | 3 (Desafiante) | Error de lógica |
| 18 | Validador de becas estudiantiles | Evaluación de requisitos con condiciones compuestas | 3 (Desafiante) | Error de lógica |
| 19 | Buscador de stock crítico | Detección de insumos bajo stock de seguridad | 3 (Desafiante) | Error de lógica |
| 20 | Simulador de caja registradora | Liquidación con descuentos y propina sugerida | 3 (Desafiante) | Error de lógica |

---

## Distribución de Dificultades

* **Dificultad 1 (Fácil: 6 desafíos)**: orientada a estudiantes de primer año. Aborda conceptos básicos como sumas, restas, comparaciones simples, formato de texto y cortes de listas.
* **Dificultad 2 (Medio: 9 desafíos)**: orientada a segundo y tercer año. Involucra acumulación en diccionarios, rangos numéricos, manejo de tipos, búsquedas y filtros condicionales.
* **Dificultad 3 (Desafiante: 5 desafíos)**: orientada a tercer y cuarto año. Cubre lógica booleana estricta, mutabilidad de colecciones en memoria, ponderaciones numéricas y cortes prematuros de bucles.

---

## Requisitos y Verificación

### Requisitos Técnicos
* Python 3.10 o superior instalado.
* No requiere instalación de paquetes externos ni entornos virtuales, utiliza únicamente la biblioteca estándar.

### Ejecución de Pruebas Globales
Para verificar de forma íntegra la consistencia de los 20 desafíos y sus soluciones, ejecuta el script de comprobación:

```bash
python verificar.py
```

El script revisará:
1. Que cada solución termine con código de salida cero y muestre el mensaje `Todas las pruebas pasaron`.
2. Que la salida real de cada solución coincida con el bloque `# Salida esperada:` documentado.
3. Que cada desafío no pase las pruebas mientras conserve el error.
4. Que la diferencia entre el desafío y su solución corresponda exactamente a un único cambio en el código.

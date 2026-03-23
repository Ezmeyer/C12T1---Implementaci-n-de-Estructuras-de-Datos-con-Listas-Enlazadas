📊 Hoja de Cálculo Dispersa en Python

Este proyecto implementa una hoja de cálculo dispersa utilizando una lista enlazada, donde solo se almacenan las celdas que contienen valores distintos de cero. Esto permite optimizar el uso de memoria en estructuras con muchos espacios vacíos.

🚀 Funcionalidades

El sistema incluye:

➕ Insertar o actualizar valores en celdas
🔍 Obtener el valor de una celda específica
❌ Eliminar celdas
📋 Mostrar la hoja completa en formato de tabla
🧠 Estructura del Sistema
🔗 Clase Celda

Representa una celda con contenido en la hoja:

fila: índice de fila
col: índice de columna
valor: valor almacenado
sig: referencia a la siguiente celda
📊 Clase Hoja

Gestiona la hoja de cálculo dispersa mediante una lista enlazada.

Atributo principal:
cabeza: inicio de la lista de celdas
⚙️ Métodos Principales
insertar(fila, col, valor)
Inserta una nueva celda
Si la celda ya existe, actualiza su valor
obtener(fila, col)
Retorna el valor de una celda
Si no existe, retorna 0
eliminar(fila, col)
Elimina una celda específica de la hoja
mostrar(filas, cols)
Imprime la hoja completa
Las celdas no almacenadas se muestran como 0
▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
📌 Ejemplo de uso
Hoja:
0 5 0 0 0
0 0 0 0 0
0 0 8 0 0
4 0 0 0 0
0 0 0 0 0

Valor en (2,2): 8

Eliminar (0,1)
0 0 0 0 0
0 0 0 0 0
0 0 8 0 0
4 0 0 0 0
0 0 0 0 0
⚠️ Limitaciones

Este sistema es una implementación básica y presenta algunas limitaciones:

❌ Búsqueda lineal (puede ser lenta con muchas celdas)
❌ No mantiene orden en las celdas
❌ No soporta operaciones avanzadas (sumas, fórmulas, etc.)
❌ No tiene persistencia en archivos
🛠️ Posibles mejoras
⚡ Uso de estructuras más eficientes (diccionarios o matrices dispersas avanzadas)
📈 Implementación de operaciones matemáticas (SUM, AVG, etc.)
💾 Guardado y carga desde archivos
🖥️ Interfaz gráfica tipo Excel
🔄 Ordenamiento de celdas por fila y columna

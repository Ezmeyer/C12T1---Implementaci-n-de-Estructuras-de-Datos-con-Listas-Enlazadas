📝 Editor de Texto con Lista Enlazada en Python

Este proyecto implementa un editor de texto simple utilizando una lista enlazada como estructura de datos principal. Cada nodo representa una línea de texto, permitiendo operaciones dinámicas como inserción, eliminación y modificación de contenido.

🚀 Funcionalidades

El editor incluye las siguientes capacidades:

➕ Insertar líneas en cualquier posición
❌ Eliminar líneas por índice
🔄 Mover líneas dentro del documento
🔍 Buscar texto dentro del contenido
✏️ Reemplazar líneas específicas
📄 Mostrar el contenido completo
💾 Guardar el documento en un archivo
📂 Cargar contenido desde un archivo
🧠 Estructura del Sistema
🔗 Clase Linea

Representa un nodo de la lista enlazada:

texto: contenido de la línea
sig: referencia a la siguiente línea
📝 Clase Editor

Gestiona la lista enlazada y todas las operaciones del editor.

Atributo principal:
cabeza: inicio de la lista enlazada
⚙️ Métodos Principales
insertar(texto, posicion)

Inserta una nueva línea en la posición indicada.

eliminar(posicion)

Elimina la línea en la posición especificada.

mover(origen, destino)

Mueve una línea desde una posición a otra.

buscar(palabra)

Busca una palabra dentro del documento y muestra las coincidencias.

reemplazar(posicion, nuevo_texto)

Reemplaza el contenido de una línea específica.

mostrar()

Imprime todas las líneas con su número correspondiente.

guardar(nombre)

Guarda el contenido del editor en un archivo de texto.

cargar(nombre)

Carga contenido desde un archivo y lo inserta en el editor.

▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
📌 Ejemplo de uso
Insertando líneas...
0 : Hola mundo
1 : Línea extra
2 : Esta es una prueba
3 : Python es genial

Eliminar línea 2
0 : Hola mundo
1 : Línea extra
2 : Python es genial

Mover línea 1 a posición 0
0 : Línea extra
1 : Hola mundo
2 : Python es genial
⚠️ Limitaciones

Este editor es una versión básica y tiene algunas limitaciones:

❌ No tiene interfaz gráfica
❌ No permite edición en tiempo real tipo cursor
❌ No maneja archivos grandes de forma optimizada
❌ No incluye manejo de errores avanzado (archivos inexistentes, permisos, etc.)
🛠️ Posibles mejoras
🖥️ Interfaz gráfica (Tkinter o PyQt)
⌨️ Soporte para edición interactiva
🔎 Búsqueda con expresiones regulares
💾 Manejo seguro de archivos (with open)
↩️ Funcionalidad de deshacer/rehacer (undo/redo)

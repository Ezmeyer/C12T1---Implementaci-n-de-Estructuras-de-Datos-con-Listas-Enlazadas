⚙️ Simulador de Procesos con Lista Enlazada en Python

Este proyecto implementa un sistema básico de gestión de procesos utilizando una lista enlazada. Permite simular estados de procesos similares a los de un sistema operativo.

🚀 Funcionalidades

El sistema incluye:

➕ Agregar procesos a la lista
📋 Mostrar todos los procesos
🔄 Cambiar el estado de un proceso
❌ Eliminar procesos terminados
🧠 Estructura del Sistema
🔗 Clase Proceso

Representa un proceso en el sistema:

id: identificador único
nombre: nombre del proceso
estado: estado actual (ej: listo, ejecucion, bloqueado, terminado)
sig: referencia al siguiente proceso
📚 Clase Lista

Gestiona la lista enlazada de procesos.

Atributo principal:
cabeza: inicio de la lista
⚙️ Métodos Principales
agregar(id, nombre, estado)

Agrega un nuevo proceso al final de la lista.

mostrar()

Muestra todos los procesos con su información.

cambiar_estado(id, nuevo)

Cambia el estado de un proceso según su ID.

eliminar_terminados()

Elimina todos los procesos cuyo estado sea "terminado".

▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
📌 Ejemplo de uso
Procesos iniciales:
1 P1 listo
2 P2 listo
3 P3 bloqueado
4 P4 listo
...

Procesos después:
1 P1 listo
2 P2 listo
3 P3 ejecucion
5 P5 ejecucion
...
⚠️ Estados de los procesos

Los estados utilizados en este sistema son:

🟢 listo → preparado para ejecutarse
🔵 ejecucion → en ejecución
🟡 bloqueado → esperando recursos
🔴 terminado → finalizado (se elimina)
⚠️ Limitaciones

Este sistema es una simulación básica:

❌ No hay planificación real de CPU (scheduler)
❌ Búsqueda lineal (puede ser ineficiente con muchos procesos)
❌ No hay concurrencia real
❌ No hay persistencia de datos
🛠️ Posibles mejoras
⏱️ Implementar algoritmos de planificación (FIFO, Round Robin, etc.)
📊 Estadísticas de ejecución de procesos
🧵 Simulación con hilos (threading)
💾 Guardar y cargar procesos desde archivos
🖥️ Interfaz gráfica

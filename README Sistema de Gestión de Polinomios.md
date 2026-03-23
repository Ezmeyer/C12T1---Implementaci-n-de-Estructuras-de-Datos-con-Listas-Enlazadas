➗ Polinomios con Listas Enlazadas en Python

Este proyecto implementa la representación y manipulación de polinomios utilizando listas enlazadas. Permite realizar operaciones matemáticas básicas como suma, multiplicación, evaluación y derivación.

🚀 Funcionalidades

El sistema incluye:

➕ Crear polinomios dinámicamente
📋 Mostrar polinomios en formato legible
🧮 Evaluar un polinomio en un valor dado
🔄 Derivar un polinomio
➕ Sumar dos polinomios
✖️ Multiplicar dos polinomios
🧠 Estructura del Sistema
🔗 Clase Termino

Representa un término del polinomio:

coef: coeficiente del término
exp: exponente
sig: referencia al siguiente término
📘 Clase Polinomio

Gestiona la lista enlazada de términos.

Atributo principal:
cabeza: inicio del polinomio
⚙️ Métodos Principales
insertar(coef, exp)

Inserta un término al final del polinomio.

mostrar()

Muestra el polinomio en formato:

3 x^ 2 + 2 x^ 1 + 1 x^ 0
evaluar(x)

Calcula el valor del polinomio para un valor dado de x.

derivar()

Retorna un nuevo polinomio que es la derivada del original.

🔢 Operaciones entre Polinomios
sumar(p1, p2)
Combina los términos de ambos polinomios
⚠️ No simplifica términos semejantes
multiplicar(p1, p2)
Multiplica todos los términos entre sí
⚠️ No agrupa términos con el mismo exponente
▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
📌 Ejemplo de uso
P1:
3 x^ 2 + 2 x^ 1 + 1 x^ 0

P2:
1 x^ 1 + 4 x^ 0

Suma:
3 x^ 2 + 2 x^ 1 + 1 x^ 0 + 1 x^ 1 + 4 x^ 0

Multiplicación:
3 x^ 3 + 12 x^ 2 + 2 x^ 2 + 8 x^ 1 + 1 x^ 1 + 4 x^ 0

Evaluar P1 en x=2: 17

Derivada de P1:
6 x^ 1 + 2 x^ 0
⚠️ Limitaciones

Este sistema es una implementación básica:

❌ No simplifica términos con el mismo exponente
❌ No ordena los términos automáticamente
❌ Inserción siempre al final
❌ No valida entradas
🛠️ Posibles mejoras
🔄 Simplificación de términos semejantes
📊 Ordenamiento por exponentes
➗ División de polinomios
🧮 Operaciones avanzadas (integrales, raíces)
💾 Guardado y carga de polinomios

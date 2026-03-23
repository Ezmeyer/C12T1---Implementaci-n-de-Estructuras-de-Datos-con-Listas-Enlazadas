# -------------------------
# Nodo de la lista
# -------------------------
class Proceso:
    def __init__(self, id, nombre, estado):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.sig = None


# -------------------------
# Lista enlazada
# -------------------------
class Lista:
    def __init__(self):
        self.cabeza = None

    # Agregar al final
    def agregar(self, id, nombre, estado):
        nuevo = Proceso(id, nombre, estado)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.sig:
                aux = aux.sig
            aux.sig = nuevo

    # Mostrar procesos
    def mostrar(self):
        aux = self.cabeza
        while aux:
            print(aux.id, aux.nombre, aux.estado)
            aux = aux.sig

    # Cambiar estado
    def cambiar_estado(self, id, nuevo):
        aux = self.cabeza
        while aux:
            if aux.id == id:
                aux.estado = nuevo
            aux = aux.sig

    # Eliminar terminados
    def eliminar_terminados(self):
        while self.cabeza and self.cabeza.estado == "terminado":
            self.cabeza = self.cabeza.sig

        aux = self.cabeza
        while aux and aux.sig:
            if aux.sig.estado == "terminado":
                aux.sig = aux.sig.sig
            else:
                aux = aux.sig


# -------------------------
# Programa principal
# -------------------------
lista = Lista()

# Crear 10 procesos
lista.agregar(1, "P1", "listo")
lista.agregar(2, "P2", "listo")
lista.agregar(3, "P3", "bloqueado")
lista.agregar(4, "P4", "listo")
lista.agregar(5, "P5", "ejecucion")
lista.agregar(6, "P6", "listo")
lista.agregar(7, "P7", "listo")
lista.agregar(8, "P8", "bloqueado")
lista.agregar(9, "P9", "listo")
lista.agregar(10, "P10", "listo")

print("Procesos iniciales:")
lista.mostrar()

# Cambios de estado
lista.cambiar_estado(3, "ejecucion")
lista.cambiar_estado(4, "terminado")

# Eliminar terminados
lista.eliminar_terminados()

print("\nProcesos después:")
lista.mostrar()
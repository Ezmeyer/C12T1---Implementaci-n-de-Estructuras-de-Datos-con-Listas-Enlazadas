# ----------------------------
# Nodo de celda
# ----------------------------
class Celda:
    def __init__(self, fila, col, valor):
        self.fila = fila
        self.col = col
        self.valor = valor
        self.sig = None


# ----------------------------
# Hoja de cálculo dispersa
# ----------------------------
class Hoja:
    def __init__(self):
        self.cabeza = None

    # Insertar o actualizar
    def insertar(self, fila, col, valor):
        aux = self.cabeza
        while aux:
            if aux.fila == fila and aux.col == col:
                aux.valor = valor
                return
            aux = aux.sig

        nueva = Celda(fila, col, valor)
        nueva.sig = self.cabeza
        self.cabeza = nueva

    # Obtener valor
    def obtener(self, fila, col):
        aux = self.cabeza
        while aux:
            if aux.fila == fila and aux.col == col:
                return aux.valor
            aux = aux.sig
        return 0

    # Eliminar celda
    def eliminar(self, fila, col):
        if self.cabeza is None:
            return

        if self.cabeza.fila == fila and self.cabeza.col == col:
            self.cabeza = self.cabeza.sig
            return

        aux = self.cabeza
        while aux.sig:
            if aux.sig.fila == fila and aux.sig.col == col:
                aux.sig = aux.sig.sig
                return
            aux = aux.sig

    # Mostrar tabla
    def mostrar(self, filas, cols):
        for i in range(filas):
            for j in range(cols):
                print(self.obtener(i, j), end=" ")
            print()


# ----------------------------
# Ejemplo de uso
# ----------------------------
hoja = Hoja()

hoja.insertar(0, 1, 5)
hoja.insertar(2, 2, 8)
hoja.insertar(3, 0, 4)

print("Hoja:")
hoja.mostrar(5, 5)

print("\nValor en (2,2):", hoja.obtener(2, 2))

print("\nEliminar (0,1)")
hoja.eliminar(0, 1)
hoja.mostrar(5, 5)
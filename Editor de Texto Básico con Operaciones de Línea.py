# ==========================================
# EDITOR DE TEXTO CON LISTA ENLAZADA
# ==========================================

# -------- Nodo (una línea de texto) --------
class Linea:
    def __init__(self, texto):
        self.texto = texto
        self.sig = None


# -------- Lista enlazada --------
class Editor:
    def __init__(self):
        self.cabeza = None

    # Insertar línea en una posición
    def insertar(self, texto, posicion):
        nueva = Linea(texto)

        if posicion == 0 or self.cabeza is None:
            nueva.sig = self.cabeza
            self.cabeza = nueva
            return

        aux = self.cabeza
        i = 0
        while aux.sig and i < posicion - 1:
            aux = aux.sig
            i += 1

        nueva.sig = aux.sig
        aux.sig = nueva

    # Eliminar línea por posición
    def eliminar(self, posicion):
        if self.cabeza is None:
            return

        if posicion == 0:
            self.cabeza = self.cabeza.sig
            return

        aux = self.cabeza
        i = 0
        while aux.sig and i < posicion - 1:
            aux = aux.sig
            i += 1

        if aux.sig:
            aux.sig = aux.sig.sig

    # Mover línea de una posición a otra
    def mover(self, origen, destino):
        if origen == destino:
            return

        # Obtener texto de la línea
        aux = self.cabeza
        i = 0
        while aux and i < origen:
            aux = aux.sig
            i += 1

        if aux is None:
            return

        texto = aux.texto
        self.eliminar(origen)
        self.insertar(texto, destino)

    # Buscar texto
    def buscar(self, palabra):
        aux = self.cabeza
        i = 0
        while aux:
            if palabra in aux.texto:
                print("Encontrado en línea", i, ":", aux.texto)
            aux = aux.sig
            i += 1

    # Reemplazar texto en una línea
    def reemplazar(self, posicion, nuevo_texto):
        aux = self.cabeza
        i = 0
        while aux and i < posicion:
            aux = aux.sig
            i += 1

        if aux:
            aux.texto = nuevo_texto

    # Mostrar contenido
    def mostrar(self):
        aux = self.cabeza
        i = 0
        while aux:
            print(i, ":", aux.texto)
            aux = aux.sig
            i += 1

    # Guardar en archivo
    def guardar(self, nombre):
        archivo = open(nombre, "w")
        aux = self.cabeza
        while aux:
            archivo.write(aux.texto + "\n")
            aux = aux.sig
        archivo.close()

    # Cargar desde archivo
    def cargar(self, nombre):
        archivo = open(nombre, "r")
        self.cabeza = None
        for linea in archivo:
            self.insertar(linea.strip(), 999)
        archivo.close()


# ==========================================
# EJEMPLO DE USO
# ==========================================

editor = Editor()

print("Insertando líneas...")
editor.insertar("Hola mundo", 0)
editor.insertar("Esta es una prueba", 1)
editor.insertar("Python es genial", 2)
editor.insertar("Línea extra", 1)

editor.mostrar()

print("\nEliminar línea 2")
editor.eliminar(2)
editor.mostrar()

print("\nMover línea 1 a posición 0")
editor.mover(1, 0)
editor.mostrar()

print("\nBuscar palabra 'Python'")
editor.buscar("Python")

print("\nReemplazar línea 1")
editor.reemplazar(1, "Texto reemplazado")
editor.mostrar()

print("\nGuardar archivo...")
editor.guardar("documento.txt")

print("\nCargar archivo en un nuevo editor")
editor2 = Editor()
editor2.cargar("documento.txt")
editor2.mostrar()
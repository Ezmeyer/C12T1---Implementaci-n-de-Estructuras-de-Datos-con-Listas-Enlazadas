# -----------------------------
# Nodo de la lista enlazada
# -----------------------------
class Termino:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.sig = None


# -----------------------------
# Polinomio como lista enlazada
# -----------------------------
class Polinomio:
    def __init__(self):
        self.cabeza = None

    # Insertar al final
    def insertar(self, coef, exp):
        nuevo = Termino(coef, exp)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            aux = self.cabeza
            while aux.sig:
                aux = aux.sig
            aux.sig = nuevo

    # Mostrar polinomio
    def mostrar(self):
        aux = self.cabeza
        while aux:
            print(aux.coef, "x^", aux.exp, end=" ")
            if aux.sig:
                print("+", end=" ")
            aux = aux.sig
        print()

    # Evaluar polinomio
    def evaluar(self, x):
        total = 0
        aux = self.cabeza
        while aux:
            total += aux.coef * (x ** aux.exp)
            aux = aux.sig
        return total

    # Derivar
    def derivar(self):
        d = Polinomio()
        aux = self.cabeza
        while aux:
            if aux.exp != 0:
                d.insertar(aux.coef * aux.exp, aux.exp - 1)
            aux = aux.sig
        return d


# -----------------------------
# Operaciones entre polinomios
# -----------------------------
def sumar(p1, p2):
    r = Polinomio()

    aux = p1.cabeza
    while aux:
        r.insertar(aux.coef, aux.exp)
        aux = aux.sig

    aux = p2.cabeza
    while aux:
        r.insertar(aux.coef, aux.exp)
        aux = aux.sig

    return r


def multiplicar(p1, p2):
    r = Polinomio()

    a = p1.cabeza
    while a:
        b = p2.cabeza
        while b:
            r.insertar(a.coef * b.coef, a.exp + b.exp)
            b = b.sig
        a = a.sig

    return r


# -----------------------------
# Ejemplo de uso
# -----------------------------
p1 = Polinomio()
p1.insertar(3, 2)
p1.insertar(2, 1)
p1.insertar(1, 0)

p2 = Polinomio()
p2.insertar(1, 1)
p2.insertar(4, 0)

print("P1:")
p1.mostrar()

print("P2:")
p2.mostrar()

print("Suma:")
sumar(p1, p2).mostrar()

print("Multiplicación:")
multiplicar(p1, p2).mostrar()

print("Evaluar P1 en x=2:", p1.evaluar(2))

print("Derivada de P1:")
p1.derivar().mostrar()
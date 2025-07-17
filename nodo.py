class nodo_AVL:
    def __init__(self, valore):
        self.valore = valore
        self.dx = None
        self.sx = None
        self.h = 1  # altezza iniziale del nodo

    def __str__(self):
        return str(self.valore)


def altezza(nodo):
    return nodo.h if nodo else 0


def aggiorna_altezza(nodo):
    if nodo:
        nodo.h = 1 + max(altezza(nodo.sx), altezza(nodo.dx))


def bilanciamento(nodo):
    return altezza(nodo.sx) - altezza(nodo.dx) if nodo else 0


# Rotazioni AVL
def ruota_dx(y):
    x = y.sx
    T2 = x.dx

    x.dx = y
    y.sx = T2

    aggiorna_altezza(y)
    aggiorna_altezza(x)
    return x


def ruota_sx(x):
    y = x.dx
    T2 = y.sx

    y.sx = x
    x.dx = T2

    aggiorna_altezza(x)
    aggiorna_altezza(y)
    return y


class albero_AVL:
    def __init__(self):
        self.root = None

    def append(self, valore):
        self.root = self.private_append(valore, self.root)

    def private_append(self, valore, nodo):
        if not nodo:
            return nodo_AVL(valore)

        if valore < nodo.valore:
            nodo.sx = self.private_append(valore, nodo.sx)
        else:
            nodo.dx = self.private_append(valore, nodo.dx)

class nodo_AVL:
    def __init__(self, valore):
        self.valore = valore
        self.dx = None
        self.sx = None
        self.h = 0
        
    def __str__(self):
        return self.valore


class albero_AVL:
    def __init__(self):
        self.root = None
        
    def private_append(self, valore, sottoalbero):
        if sottoalbero.valore < valore:
            if sottoalbero.dx == None:
                sottoalbero.dx = nodo_AVL(valore)
            else:
                self.private_append(valore, sottoalbero.dx)
        else:
            if sottoalbero.sx == None:
                sottoalbero.sx = nodo_AVL(valore)
            else:
                self.private_append(valore, sottoalbero.sx)
        
    def append(self, valore):
        if self.root == None:
            self.root = nodo_AVL(valore)
        else:
            self.private_append(valore, self.root)
            
    def __str__(self):
        pass
alberi_AVL.py
Visualizzazione di alberi_AVL.py.
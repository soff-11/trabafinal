class Pila:

    def __init__(self):

        self.items = []

    def push(self, valor):

        self.items.append(valor)

    def pop(self):

        return self.items.pop()

    def top(self):

        return self.items[-1]

    def vacia(self):

        return len(self.items) == 0

    def __str__(self):

        return str(self.items)
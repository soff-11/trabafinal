class Nodo:

    def __init__(self):

        self.valor = 0.0

        self.valor_logico = False

        self.relacional = False

    def __str__(self):

        if self.relacional:
            return str(self.valor_logico)

        return str(self.valor)
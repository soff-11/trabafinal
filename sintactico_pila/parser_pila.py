from sintactico_pila.pila import Pila

from sirve.constantes import EOF

from sintactico_pila.tabla_control import TablaLL1

class ParserPila:

    def __init__(self, tokens):

        self.tokens = tokens

        self.pos = 0

        self.actual = tokens[0]

        self.pila = Pila()

        self.tabla = TablaLL1()
    
        self.no_terminales = {

    "S",

    "ELO",
    "ELOL",

    "EL2",
    "EL2L",

    "ENOT",

    "ER",
    "ERL",

    "E",
    "EP",

    "T",
    "TP",

    "P",
    "PP",

    "F"
}
    def avanzar(self):

        self.pos += 1

        if self.pos < len(self.tokens):

            self.actual = self.tokens[self.pos]

    def analizar(self):

        self.pila.push(EOF)

        self.pila.push("S")

        while not self.pila.vacia():

            cima = self.pila.pop()

            print(
                f"\nCima: {cima}"
            )

            print(
                f"Token actual: "
                f"{self.actual.tipo}"
            )

            # ------------------
            # NO TERMINAL
            # ------------------

            if cima in self.no_terminales:

                produccion = (
                    self.tabla.buscar(
                        cima,
                        self.actual.tipo
                    )
                )

                if produccion is None:

                    raise Exception(
                        f"No existe producción "
                        f"para ({cima}, "
                        f"{self.actual.tipo})"
                    )

                print(
                    f"Producción: "
                    f"{cima} -> "
                    f"{produccion}"
                )

                for simbolo in reversed(
                    produccion
                ):
                    self.pila.push(
                        simbolo
                    )

            # ------------------
            # TERMINAL
            # ------------------

            else:

                if cima == EOF and self.actual.tipo == EOF:

                    print(
                        "Aceptada"
                    )

                    return True

                elif cima == self.actual.tipo:

                    print(
                        f"Match: {cima}"
                    )

                    self.avanzar()

                else:

                    raise Exception(
                        f"Esperaba "
                        f"{cima}"
                    )
from sirve.constantes import SUMA, RESTA, MULT, DIV, EOF, NUMERO, POT, PARI, PARD, MENOR, MAYOR, MENORIGUAL, MAYORIGUAL, IGUAL, DIFERENTE, AND, OR, NOT

from sintactico_recursivo.nodo import Nodo
from sintactico_recursivo.operaciones import Operaciones




class ParserRecursivo:

    def __init__(self, tokens):

        self.tokens = tokens

        self.pos = 0

        self.actual = tokens[0]

    # ==========================
    # UTILIDADES
    # ==========================

    def avanzar(self):

        self.pos += 1

        if self.pos < len(self.tokens):
            self.actual = self.tokens[self.pos]

    def consumir(self, tipo):

        if self.actual.tipo == tipo:
            self.avanzar()
        else:
            raise Exception(
                f"Se esperaba {tipo}"
            )

    # ==========================
    # S
    # ==========================

    def S(self):

        resultado = self.ELO()

        self.consumir(EOF)

        return resultado
    
    # ==========================
    # ELO   
    # ==========================

    
    def ELO(self):

        izquierda = self.EL2()

        return self.ELO_L(
            izquierda
        )
    
     # ==========================
    # ELO_L   
    # ==========================
    
    def ELO_L(self, izquierda):

        while self.actual.tipo == OR:

            self.avanzar()

            derecha = self.EL2()

            izquierda = Operaciones.proc_or(
                izquierda,
                derecha
            )

        return izquierda
    
    # ==========================
    # EL2
    # ==========================

    def EL2(self):

        izquierda = self.ENOT()

        return self.EL2_L(
            izquierda
        )


    # ==========================
    # EL2_L
    # ==========================

    def EL2_L(self, izquierda):

        while self.actual.tipo == AND:

            self.avanzar()

            derecha = self.ENOT()

            izquierda = Operaciones.proc_and(
                izquierda,
                derecha
            )

        return izquierda
            
    # ==========================
    # ENOT
    # ==========================
    
    def ENOT(self):

        if self.actual.tipo == NOT:

            self.avanzar()

            if self.actual.tipo == PARI:

                self.avanzar()

                operando = self.ELO()

                self.consumir(PARD)

                return Operaciones.proc_not(
                    operando
                )

            else:

                operando = self.ENOT()

                return Operaciones.proc_not(
                    operando
                )

        return self.ER()
    
    
    
    # ==========================
    # ER
    # ==========================

    def ER(self):

        izquierda = self.E()

        return self.ER_L(izquierda)

    def ER_L(self, izquierda):

        operadores = (
            MENOR,
            MAYOR,
            MENORIGUAL,
            MAYORIGUAL,
            IGUAL,
            DIFERENTE
        )

        if self.actual.tipo in operadores:

            operador = self.actual.tipo

            self.avanzar()

            derecha = self.E()

            return Operaciones.comparar(
                izquierda,
                derecha,
                operador
            )

        return izquierda

    # ==========================
    # E
    # ==========================

    def E(self):

        izquierda = self.T()

        return self.E_L(izquierda)

    def E_L(self, izquierda):

        while self.actual.tipo in (
            SUMA,
            RESTA
        ):

            operador = self.actual.tipo

            self.avanzar()

            derecha = self.T()

            if operador == SUMA:

                izquierda = Operaciones.suma(
                    izquierda,
                    derecha
                )

            else:

                izquierda = Operaciones.resta(
                    izquierda,
                    derecha
                )

        return izquierda

    # ==========================
    # T
    # ==========================

    def T(self):

        izquierda = self.P()

        return self.T_L(izquierda)

    def T_L(self, izquierda):

        while self.actual.tipo in (
            MULT,
            DIV
        ):

            operador = self.actual.tipo

            self.avanzar()

            derecha = self.P()

            if operador == MULT:

                izquierda = (
                    Operaciones.multiplicacion(
                        izquierda,
                        derecha
                    )
                )

            else:

                izquierda = (
                    Operaciones.division(
                        izquierda,
                        derecha
                    )
                )

        return izquierda

    # ==========================
    # P
    # ==========================

    def P(self):

        izquierda = self.F()

        if self.actual.tipo == POT:

            self.avanzar()

            derecha = self.P()

            return Operaciones.potencia(
                izquierda,
                derecha
            )

        return izquierda

    # ==========================
    # F
    # ==========================

    def F(self):

        if self.actual.tipo == NUMERO:

            valor = self.actual.lexema

            self.avanzar()

            n = Nodo()

            n.valor = valor

            return n

        elif self.actual.tipo == PARI:

            self.avanzar()

            resultado = self.ELO()

            self.consumir(PARD)

            return resultado
        raise Exception(
            "Se esperaba número o ("
        )
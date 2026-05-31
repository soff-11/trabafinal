from sintactico_recursivo.nodo import Nodo


class Operaciones:

    @staticmethod
    def suma(a, b):

        r = Nodo()
        r.valor = a.valor + b.valor
        return r

    @staticmethod
    def resta(a, b):

        r = Nodo()
        r.valor = a.valor - b.valor
        return r

    @staticmethod
    def multiplicacion(a, b):

        r = Nodo()
        r.valor = a.valor * b.valor
        return r

    @staticmethod
    def division(a, b):

        r = Nodo()
        r.valor = a.valor / b.valor
        return r

    @staticmethod
    def potencia(a, b):

        r = Nodo()
        r.valor = a.valor ** b.valor
        return r

    @staticmethod
    def comparar(a, b, operador):

        r = Nodo()

        r.relacional = True

        if operador == "<":
            r.valor_logico = a.valor < b.valor

        elif operador == ">":
            r.valor_logico = a.valor > b.valor

        elif operador == "<=":
            r.valor_logico = a.valor <= b.valor

        elif operador == ">=":
            r.valor_logico = a.valor >= b.valor

        elif operador == "==":
            r.valor_logico = a.valor == b.valor

        elif operador == "!=":
            r.valor_logico = a.valor != b.valor

        return r
    
    @staticmethod
    def proc_and(a, b):

        if not a.relacional:
            raise Exception(
                "Operando izquierdo no relacional"
            )

        if not b.relacional:
            raise Exception(
                "Operando derecho no relacional"
            )

        r = Nodo()

        r.relacional = True

        r.valor_logico = (
            a.valor_logico
            and
            b.valor_logico
        )

        return r
    
    @staticmethod
    def proc_or(a, b):

        if not a.relacional:
            raise Exception(
                "Operando izquierdo no relacional"
            )

        if not b.relacional:
            raise Exception(
                "Operando derecho no relacional"
            )

        r = Nodo()

        r.relacional = True

        r.valor_logico = (
            a.valor_logico
            or
            b.valor_logico
        )

        return r
    
    @staticmethod
    def proc_not(a):

        if not a.relacional:

            raise Exception(
                "NOT requiere una expresión lógica"
            )

        r = Nodo()

        r.relacional = True

        r.valor_logico = (
            not a.valor_logico
        )

        return r
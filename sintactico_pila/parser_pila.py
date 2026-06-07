from sintactico_pila.pila import Pila

from sintactico_pila.valor import Valor
from sirve.constantes import EOF

from sintactico_pila.tabla_control import TablaLL1

class ParserPila:

    def __init__(self, tokens):

        self.tokens = tokens

        self.pos = 0

        self.actual = tokens[0]

        self.pila = Pila()

        self.pila_valores = []

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

            elif cima == "{MENOR}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado < der.resultado,

                    f"({izq.infija}<{der.infija})",

                    f"< {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} <",

                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{MAYOR}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado > der.resultado,

                    f"({izq.infija}>{der.infija})",

                    f"> {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} >",

                    True
                )

                self.pila_valores.append(nuevo)
            
            elif cima == "{MENORIGUAL}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado <= der.resultado,

                    f"({izq.infija}<={der.infija})",

                    f"<= {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} <=",
                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{MAYORIGUAL}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado >= der.resultado,

                    f"({izq.infija}>={der.infija})",

                    f">= {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} >=",
                    True
                )

                self.pila_valores.append(nuevo)
           
            elif cima == "{IGUAL}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado == der.resultado,

                    f"({izq.infija}=={der.infija})",

                    f"== {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} ==",
                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{DIFERENTE}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado != der.resultado,

                    f"({izq.infija}!={der.infija})",

                    f"!= {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} !=",
                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{AND}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                if not izq.relacional or not der.relacional:

                    raise Exception(
                        "Los operandos de '&' deben ser expresiones relacionales"
                    )

                nuevo = Valor(

                    izq.resultado and der.resultado,

                    f"({izq.infija}&{der.infija})",

                    f"& {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} &",

                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{OR}":

                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                if not izq.relacional or not der.relacional:

                    raise Exception(
                        "Los operandos de '|' deben ser expresiones relacionales"
                    )

                nuevo = Valor(

                    izq.resultado or der.resultado,

                    f"({izq.infija}|{der.infija})",

                    f"| {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} |",

                    True
                )

                self.pila_valores.append(nuevo)

            elif cima == "{NOT}":

                op = self.pila_valores.pop()

                if not op.relacional:

                    raise Exception(
                        "El operador ! requiere una expresión relacional"
                    )

                nuevo = Valor(

                    not op.resultado,

                    f"(!{op.infija})",

                    f"! {op.prefija}",

                    f"{op.postfija} !",

                    True
                )

                self.pila_valores.append(nuevo)
                        

            elif cima == "{SUMA}":
                der = self.pila_valores.pop()

                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado + der.resultado,

                    f"({izq.infija}+{der.infija})",

                    f"+ {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} +"
                )

                self.pila_valores.append(nuevo)

            elif cima == "{RESTA}":
                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado - der.resultado,

                    f"({izq.infija}-{der.infija})",

                    f"- {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} -"
                )

                self.pila_valores.append(nuevo)

            elif cima == "{MULT}":
                der = self.pila_valores.pop()
                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado * der.resultado,

                    f"({izq.infija}*{der.infija})",

                    f"* {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} *"
                )

                self.pila_valores.append(nuevo)

            elif cima == "{DIV}":

                der = self.pila_valores.pop()

                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado / der.resultado,

                    f"({izq.infija}/{der.infija})",

                    f"/ {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} /"
                )

                self.pila_valores.append(nuevo)
            
            elif cima == "{POT}":

                der = self.pila_valores.pop()

                izq = self.pila_valores.pop()

                nuevo = Valor(

                    izq.resultado ** der.resultado,

                    f"({izq.infija}^{der.infija})",

                    f"^ {izq.prefija} {der.prefija}",

                    f"{izq.postfija} {der.postfija} ^"
                )

                self.pila_valores.append(nuevo)

            

            # ------------------
            # TERMINAL
            # ------------------

            else:

                if cima == EOF and self.actual.tipo == EOF:

                    print(
                        "Aceptada"
                    )

                    resultado = self.pila_valores[-1]

                    print("\nRESULTADO")
                    print(resultado.resultado)

                    print("\nINFIJA")
                    print(resultado.infija)

                    print("\nPREFIJA")
                    print(resultado.prefija)

                    print("\nPOSTFIJA")
                    print(resultado.postfija)

                    return True

                elif cima == "NUMERO":

                    self.pila_valores.append(

                        Valor(
                            self.actual.lexema,
                            str(self.actual.lexema),
                            str(self.actual.lexema),
                            str(self.actual.lexema)
                        )
                    )

                    print(
                        f"Match: {cima}"
                    )

                    self.avanzar()
                
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
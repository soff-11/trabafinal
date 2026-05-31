from lexico.token import Token
from sirve.constantes import SUMA, RESTA, MULT, DIV, EOF, NUMERO, POT, PARI, PARD, MENOR, MAYOR, MENORIGUAL, MAYORIGUAL, IGUAL, DIFERENTE, AND, OR, NOT


class Scanner:

    def __init__(self, cadena):
        self.cadena = cadena
        self.pos = 0

    def analizar(self):

        tokens = []

        while self.pos < len(self.cadena):

            c = self.cadena[self.pos]

            if c.isspace():
                self.pos += 1
                continue

            if c.isdigit():

                numero = ""

                while (
                    self.pos < len(self.cadena)
                    and (
                        self.cadena[self.pos].isdigit()
                        or self.cadena[self.pos] == "."
                    )
                ):
                    numero += self.cadena[self.pos]
                    self.pos += 1

                tokens.append(
                    Token(NUMERO, float(numero))
                )

                continue

            if self.pos + 1 < len(self.cadena):

                doble = self.cadena[self.pos:self.pos+2]

                if doble == "<=":
                    tokens.append(Token(MENORIGUAL, doble))
                    self.pos += 2
                    continue

                if doble == ">=":
                    tokens.append(Token(MAYORIGUAL, doble))
                    self.pos += 2
                    continue

                if doble == "==":
                    tokens.append(Token(IGUAL, doble))
                    self.pos += 2
                    continue

                if doble == "!=":
                    tokens.append(Token(DIFERENTE, doble))
                    self.pos += 2
                    continue

            if c == "+":
                tokens.append(Token(SUMA, c))

            elif c == "-":
                tokens.append(Token(RESTA, c))

            elif c == "*":
                tokens.append(Token(MULT, c))

            elif c == "/":
                tokens.append(Token(DIV, c))

            elif c == "^":
                tokens.append(Token(POT, c))

            elif c == "(":
                tokens.append(Token(PARI, c))

            elif c == ")":
                tokens.append(Token(PARD, c))
            
            elif c == "<":
                tokens.append(Token(MENOR, c))

            elif c == ">":
                tokens.append(Token(MAYOR, c))
            
            elif c == "&":
                tokens.append(
                    Token(AND, c)
                )
            
            elif c == "!":
                tokens.append(
                    Token(NOT, c)
                )

            elif c == "|":
                tokens.append(
                    Token(OR, c)
                )

            else:
                raise Exception(
                    f"Caracter no válido: {c}"
                )
            self.pos += 1

        tokens.append(Token(EOF, EOF))

        return tokens
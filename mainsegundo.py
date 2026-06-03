from lexico.scanner import Scanner

from sintactico_pila.parser_pila import (
    ParserPila
)


expresion = input(
    "Ingrese expresión: "
)

tokens = Scanner(
    expresion
).analizar()

parser = ParserPila(tokens)

parser.analizar()
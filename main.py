from lexico.scanner import Scanner

from sintactico_recursivo.parser_recursivo import (
    ParserRecursivo
)


def main():

    expresion = input(
        "Ingrese expresión: "
    )

    scanner = Scanner(expresion)

    tokens = scanner.analizar()
    

    print("\nTOKENS:")
    for t in tokens:
        print(t)


    parser = ParserRecursivo(tokens)

    resultado = parser.S()

    print("\nRESULTADO:")

    if resultado.relacional:

        print(resultado.valor_logico)

    else:

        print(resultado.valor)
    
    

if __name__ == "__main__":
    main()
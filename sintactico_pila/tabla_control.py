class TablaLL1:

    def __init__(self):

        self.tabla = {}
        self.construir()

    def agregar(
        self,
        no_terminal,
        terminal,
        produccion
    ):

        self.tabla[
            (no_terminal, terminal)
        ] = produccion

    def buscar(
        self,
        no_terminal,
        terminal
    ):

        clave = (
            no_terminal,
            terminal
        )

        return self.tabla.get(
            clave,
            None
        )
    
    def construir(self):

        # S -> ER

        self.agregar(
            "S",
            "NUMERO",
            ["ELO"]
        )

        self.agregar(
            "S",
            "(",
            ["ELO"]
        )

        self.agregar(
            "S",
            "!",
            ["ELO"]
        )

        # ELO -> EL2 ELOL

        self.agregar(
            "ELO",
            "NUMERO",
            ["EL2", "ELOL"]
        )

        self.agregar(
            "ELO",
            "(",
            ["EL2", "ELOL"]
        )

        self.agregar(
            "ELO",
            "!",
            ["EL2", "ELOL"]
        )

        # ELOL -> | EL2 ELOL

        self.agregar(
            "ELOL",
            "|",
            ["|", "EL2", "ELOL"]
        )

        # ELOL -> ε

        self.agregar(
            "ELOL",
            ")",
            []
        )

        self.agregar(
            "ELOL",
            "$",
            []
        )

        # EL2 -> ENOT EL2L

        self.agregar(
            "EL2",
            "NUMERO",
            ["ENOT", "EL2L"]
        )

        self.agregar(
            "EL2",
            "(",
            ["ENOT", "EL2L"]
        )

        self.agregar(
            "EL2",
            "!",
            ["ENOT", "EL2L"]
        )

        # EL2L -> & ENOT EL2L

        self.agregar(
            "EL2L",
            "&",
            ["&", "ENOT", "EL2L"]
        )

        self.agregar(
            "EL2L",
            "|",
            []
        )

        self.agregar(
            "EL2L",
            ")",
            []
        )

        self.agregar(
            "EL2L",
            "$",
            []
        )

        # ENOT -> ! ENOT

        self.agregar(
            "ENOT",
            "!",
            ["!", "ENOT"]
        )

        self.agregar(
            "ENOT",
            "NUMERO",
            ["ER"]
        )

        self.agregar(
            "ENOT",
            "(",
            ["ER"]
        )

        # ER -> E ERL

        self.agregar(
            "ER",
            "NUMERO",
            ["E", "ERL"]
        )

        self.agregar(
            "ER",
            "(",
            ["E", "ERL"]
        )

        # ERL -> < E

        self.agregar(
            "ERL",
            "<",
            ["<", "E"]
        )

        # ERL -> > E

        self.agregar(
            "ERL",
            ">",
            [">", "E"]
        )

        # ERL -> <= E

        self.agregar(
            "ERL",
            "<=",
            ["<=", "E"]
        )

        # ERL -> >= E

        self.agregar(
            "ERL",
            ">=",
            [">=", "E"]
        )

        # ERL -> == E

        self.agregar(
            "ERL",
            "==",
            ["==", "E"]
        )

        # ERL -> != E

        self.agregar(
            "ERL",
            "!=",
            ["!=", "E"]
        )

        self.agregar(
            "ERL",
            ")",
            []
        )

        self.agregar(
            "ERL",
            "$",
            []
        )

        self.agregar(
            "ERL",
            "&",
            []
        )

        self.agregar(
            "ERL",
            "|",
            []
        )

         # E -> T EP

        self.agregar(
            "E",
            "NUMERO",
            ["T", "EP"]
        )

        self.agregar(
            "E",
            "(",
            ["T", "EP"]
        )

        # EP -> + T EP

        self.agregar(
            "EP",
            "+",
            ["+", "T", "EP"]
        )

        # EP -> - T EP

        self.agregar(
            "EP",
            "-",
            ["-", "T", "EP"]
        )

        # EP -> ε

        self.agregar(
            "EP",
            ")",
            []
        )

        self.agregar(
            "EP",
            "$",
            []
        )

        self.agregar(
            "EP",
            "&",
            []
        )

        self.agregar(
            "EP",
            "|",
            []
        )

        self.agregar(
            "EP",
            "<",
            []
        )

        self.agregar(
            "EP",
            ">",
            []
        )

        self.agregar(
            "EP",
            "<=",
            []
        )

        self.agregar(
            "EP",
            ">=",
            []
        )

        self.agregar(
            "EP",
            "==",
            []
        )

        self.agregar(
            "EP",
            "!=",
            []
        )

        # T -> P TP

        self.agregar(
            "T",
            "NUMERO",
            ["P", "TP"]
        )

        self.agregar(
            "T",
            "(",
            ["P", "TP"]
        )

        # TP ->  P TP

        self.agregar(
            "TP",
            "*",
            ["*", "P", "TP"]
        )

        self.agregar(
            "TP",
            "/",
            ["/", "P", "TP"]
        )

        # TP -> ε

        self.agregar(
            "TP",
            "+",
            []
        )

        self.agregar(
            "TP",
            "-",
            []
        )

        self.agregar(
            "TP",
            ")",
            []
        )

        self.agregar(
            "TP",
            "$",
            []
        )

        self.agregar(
            "TP",
            "&",
            []
        )

        self.agregar(
            "TP",
            "|",
            []
        )

        self.agregar(
            "TP",
            "<",
            []
        )

        self.agregar(
            "TP",
            ">",
            []
        )

        self.agregar(
            "TP",
            "<=",
            []
        )

        self.agregar(
            "TP",
            ">=",
            []
        )

        self.agregar(
            "TP",
            "==",
            []
        )

        self.agregar(
            "TP",
            "!=",
            []
        )

        # P -> F PP

        self.agregar(
            "P",
            "NUMERO",
            ["F", "PP"]
        )

        self.agregar(
            "P",
            "(",
            ["F", "PP"]
        )

        # PP -> ^ P

        self.agregar(
            "PP",
            "^",
            ["^", "P"]
        )

        self.agregar(
            "PP",
            "*",
            []
        )

        self.agregar(
            "PP",
            "/",
            []
        )

        self.agregar(
            "PP",
            "+",
            []
        )

        self.agregar(
            "PP",
            "-",
            []
        )

        self.agregar(
            "PP",
            ")",
            []
        )

        self.agregar(
            "PP",
            "$",
            []
        )

        self.agregar(
            "PP",
            "<",
            []
        )

        self.agregar(
            "PP",
            ">",
            []
        )

        self.agregar(
            "PP",
            "<=",
            []
        )

        self.agregar(
            "PP",
            ">=",
            []
        )

        self.agregar(
            "PP",
            "==",
            []
        )

        self.agregar(
            "PP",
            "!=",
            []
        )

        self.agregar(
            "PP",
            "&",
            []
        )

        self.agregar(
            "PP",
            "|",
            []
        )

        self.agregar(
            "PP",
            "<",
            []
        )

        self.agregar(
            "PP",
            ">",
            []
        )

        self.agregar(
            "PP",
            "<=",
            []
        )

        self.agregar(
            "PP",
            ">=",
            []
        )

        self.agregar(
            "PP",
            "==",
            []
        )

        self.agregar(
            "PP",
            "!=",
            []
        )

        # F -> NUMERO

        self.agregar(
            "F",
            "NUMERO",
            ["NUMERO"]
        )

        # F -> ( E )

        self.agregar(
            "F",
            "(",
            ["(", "ELO", ")"]
        )
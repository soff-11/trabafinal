class Valor:

    def __init__(
        self,
        resultado,
        infija,
        prefija,
        postfija,
        relacional=False
    ):

        self.resultado = resultado
        self.infija = infija
        self.prefija = prefija
        self.postfija = postfija

        self.relacional = relacional
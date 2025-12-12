from especialistas import Especialistas

class Obstinado(Especialistas):
    def __init__(self, nome, vinculo_arkanya, vinculo_essys):
        super().__init__(nome, vinculo_arkanya, vinculo_essys)
        self.classe = "Obstinado"
        self.obstinada = None

    def escolhido_obstinada(self, nome_obstinada):
        self.obstinada = nome_obstinada
        return "Esse especialista foi escolhido por uma Obstinada."

    def __str__(self):
        return f'{super().__str__()} | Classe: {self.classe}'
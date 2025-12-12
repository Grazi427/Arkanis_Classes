from especialistas import Especialistas

class Decodificadores(Especialistas):
    def __init__(self, nome, vinculo_arkanya, vinculo_essys):
        super().__init__(nome, vinculo_arkanya, vinculo_essys)
        self.classe = "Decodificador"
        self.lankya = None

    def decodificar_lankyas(self, lankya):
        self.lankya = lankya

    def __str__(self):
        return f'{super().__str__()} | Classe: {self.classe}'
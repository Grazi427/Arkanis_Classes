from especialistas import Especialistas

class Codificadores(Especialistas):
    def __init__(self, nome, vinculo_arkanya, vinculo_essys):
        super().__init__(nome, vinculo_arkanya, vinculo_essys)
        self.classe = "Codificador"
        self.lankya = None
        self.funcao_lankya = None

    def codificar_lankyas(self, nome_lankya, funcao_lankya):
        self.lankya = nome_lankya
        self.funcao_lankya = funcao_lankya

    def decodificar_lankyas(self, lankya):
        self.lankya = lankya

    def __str__(self):
        return f'{super().__str__()} | Classe: {self.classe}'
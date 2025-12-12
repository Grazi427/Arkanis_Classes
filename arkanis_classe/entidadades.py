class Entidades_Arkanya:
    def __init__(self, nome, vinculo_arkanya, funcao):
        self.nome = nome
        self.arkanya = vinculo_arkanya
        self.funcao = funcao

    def julgar(self, culpado, inocente):
        if culpado:
            return f"A entidade {self.nome} julgou o acusado como culpado, ele receberá uma pena de acordo. Arkanya é justa! "
        elif inocente:
            return f"A entidade {self.nome} julgou o acusado inocente, seu fluxo de Arkanya permanecerá, pois ela é jsuta."

    def __str__(self):
        return f'- Entidade: {self.nome} | Função: {self.funcao}'
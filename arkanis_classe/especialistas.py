class Especialistas:
    def __init__(self, nome, vinculo_arkanya, vinculo_essys):
        self.nome = nome
        self.arkanya = vinculo_arkanya
        self.essys = vinculo_essys
        self.lado = self.definir_lado()
    
    def definir_lado(self):
        if self.essys > self.arkanya:
            return "Araldo"
        elif self.arkanya > self.essys:
            return "Guardiãs de Arkanya"
        else:
            return "Neutro"

    def __str__(self):
        return f'- Nome: {self.nome} | Lado: {self.lado}'


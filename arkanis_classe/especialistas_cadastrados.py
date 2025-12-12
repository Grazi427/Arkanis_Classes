from especialistas import Especialistas
from codificadores import Codificadores
from decodificadores import Decodificadores
from obstinados import Obstinado
from entidadades import Entidades_Arkanya

lista_especialistas = []
lista_entidades = []

def inicializar_dados():
    # Especialista
    esp1 = Especialistas("Bagi", 50, 50)
    esp2 = Especialistas("Choke (Iandara)", 100, 0)
    esp3 = Especialistas("Moonkase (Fera Lohikäärme)", 1000, 0)
    esp4 = Especialistas("FunBabe", 50, 51)
    
    # Decodificadores
    d1 = Decodificadores("Malena (Bia Raux)", 100, 0)
    
    # Obstinados
    o1 = Obstinado("GabePeixe", 50, 50)
    o1.escolhido_obstinada("Katana do Mestre Obstinado")
    o2 = Obstinado("Quel", 100, 0)
    o2.escolhido_obstinada("Florete de esgrima da Guardiã do Cosmos")
    o3 = Obstinado("Pac", 100, 0)
    o3.escolhido_obstinada("Arco do Cúpido")
    o4 = Obstinado("NickLink", 100, 0)
    o4.escolhido_obstinada("Foice Preta de Sangue")
    o5 = Obstinado("Fusrobya", 100, 0)
    o5.escolhido_obstinada("Espada Obstinada de Sangue")
    o6 = Obstinado("Celinet", 100, 0)
    o6.escolhido_obstinada("Arco de Ártemis")
    o7 = Obstinado("Guaxinim", 100, 0)
    o7.escolhido_obstinada("Machado Obstinado")
    o8 = Obstinado("Matt", 100, 0)
    o8.escolhido_obstinada("Foice Obstinada")
    o9 = Obstinado("Guhzera", 100, 0)
    o9.escolhido_obstinada("Adasgas Obstinadas")
    o10 = Obstinado("Jvnq", 100, 0)
    o10.escolhido_obstinada("Arma de Poseidon")


    # Entidades
    e1 = Entidades_Arkanya("Lohikäärme", 1000, "Seu fogo devolve ao Fluxo aqueles que foram julgados por Arkanya")
    e2 = Entidades_Arkanya("Feyhara", 1000, "Seu fogo julga aqueles levados ao julgamento por Arkanya")
    e3 = Entidades_Arkanya("Monah", 1000, "Entidade da Simetria")
    e4 = Entidades_Arkanya("MEDO", 1000, "Mestre Eterno da Decisões e Ofertas")
    e5 = Entidades_Arkanya("Hannya", 1000, "Entidade da Guerra")
    e6 = Entidades_Arkanya("Samir", 1000, "Entidade da Harmonia")
    e7 = Entidades_Arkanya("O Rato", 1000, "Entidade da Avareza")



    lista_especialistas.extend([d1, o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, esp1, esp2, esp3, esp4])
    lista_entidades.extend([e1, e2, e3, e4, e5, e6, e7])
    
    print(">> Dados do sistema carregados com sucesso! <<")
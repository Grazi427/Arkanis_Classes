from especialistas import Especialistas
from codificadores import Codificadores
from decodificadores import Decodificadores
from obstinados import Obstinado
from entidadades import Entidades_Arkanya
from especialistas_cadastrados import inicializar_dados,lista_especialistas,lista_entidades



def exibir_menu():
    print("\n" + "="*40)
    print("Guia de Personagens de Arkanis")
    print("="*40)
    print("--- Especialistas ---")
    print("1. Todos os especialistas")
    print("2. Especialistas do lado do Araldo")
    print("3. Especialistas do lado das Guardiãs de Arkanya")
    print("4. Codificadores")
    print("5. Decodificadores")
    print("6. Obstinados")
    print("\n--- Entidades ---")
    print("7. Listar Entidades")
    print("0. Sair")
    print("="*40)

def main():
    inicializar_dados()
    
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == '1':
            print("\n--- Todos os Especialistas ---\n")
            for e in lista_especialistas:
                print(e)
                if e not in lista_especialistas:
                    print('Não há nenhum especialista')
                
        elif escolha == '2':
            print("\n--- Lado do Araldo ---")
            encontrou = False
            for e in lista_especialistas:
                if e.lado == "Araldo":
                    print(e)
                    encontrou = True
            if not encontrou: print("Nenhum encontrado.")

        elif escolha == '3':
            print("\n--- Lado das Guardiãs ---")
            encontrou = False
            for e in lista_especialistas:
                if e.lado == "Guardiãs de Arkanya":
                    print(e)
                    encontrou = True
            if not encontrou: print("Nenhum encontrado.")

        elif escolha == '4':
            print("\n--- Codificadores ---")
            for e in lista_especialistas:
                if isinstance(e, Codificadores):
                    print(e)

        elif escolha == '5':
            print("\n--- Decodificadores ---")
            for e in lista_especialistas:
                if isinstance(e, Decodificadores):
                    print(e)

        elif escolha == '6':
            print("\n--- Obstinados ---")
            for e in lista_especialistas:
                if isinstance(e, Obstinado):
                    print(e)

        elif escolha == '7':
            print("\n--- Entidades ---")
            for ent in lista_entidades:
                print(ent)

        elif escolha == '0':
            print("Obrigado por usar o sistema! Encerrando...")
            exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__=='__main__':
    main()
#Arkanis Classes
Este projeto implementa um sistema de gestão de personagens e entidades baseado no universo de Arkanis. O sistema utiliza Programação Orientada a Objetos (POO) em Python para modelar diferentes tipos de especialistas, os seus vínculos (Arkanya e Essys) e as suas classes específicas, além de permitir a interação através de um menu de consola.

#📋 Sobre o Projeto
O objetivo principal é simular um guia de personagens onde é possível catalogar e listar Especialistas e Entidades. O sistema define automaticamente a lealdade ("Lado") de cada personagem com base nos seus níveis de vínculo com "Arkanya" e "Essys".

Lógica de Alinhamento
O método definir_lado na classe base determina a afiliação do especialista:

Araldo: Se o vínculo com Essys for superior ao de Arkanya.

Guardiãs de Arkanya: Se o vínculo com Arkanya for superior ao de Essys.

Neutro: Se os vínculos forem iguais.

#🚀 Funcionalidades
O sistema possui um menu interativo (main.py) que permite:

Listar Todos os Especialistas: Exibe todos os personagens cadastrados com os seus nomes e lados.

Filtrar por Lado:

Listar apenas aliados do Araldo.

Listar apenas aliadas das Guardiãs de Arkanya.

Filtrar por Classe:

Codificadores: Especialistas capazes de codificar e descodificar Lankyas.

Descodificadores: Especialistas focados na descodificação.

Obstinados: Especialistas escolhidos por uma arma ou objeto "Obstinado".

Listar Entidades: Exibe as entidades supremas de Arkanya e as suas funções de julgamento.

#🛠️ Estrutura do Código
O projeto está modularizado nos seguintes ficheiros:

1. Classes Principais
especialistas.py: Contém a classe pai Especialistas. Define os atributos base (nome, arkanya, essys) e a lógica para definir o lado.

codificadores.py: Herda de Especialistas. Adiciona métodos para codificar_lankyas.

decodificadores.py: Herda de Especialistas. Foca-se na descodificação.

obstinados.py: Herda de Especialistas. Possui o atributo obstinada (a arma/objeto que escolheu o especialista).

entidadades.py: Classe independente Entidades_Arkanya para representar seres superiores com funções de julgamento (julgar).

2. Gestão de Dados e Execução
especialistas_cadastrados.py: Responsável por "popular" o sistema. Inicializa listas de objetos com dados de exemplo (ex: Bagi, Cellbit, Moonkase, etc.) para que o programa não comece vazio.

main.py: O ponto de entrada. Importa as classes e os dados, e executa o loop principal do menu.

#📦 Como Executar
Certifica-te de que tens o Python 3 instalado.

Navega até à pasta onde os ficheiros estão localizados:

Bash

cd arkanis_classe
Executa o ficheiro principal:

Bash

python main.py
#📊 Exemplo de Dados
O sistema já vem pré-carregado com alguns personagens conhecidos para teste:

Especialistas: Bagi, Choke, Moonkase, FunBabe.

Obstinados: Pac (Arco do Cupido), NinckLink (Foice Preta), entre outros.

Entidades: Lohikäärme, Feyhara, O Rato, etc.

#📐 Diagrama de Classes
O projeto inclui um diagrama visual da estrutura (Diagrama de Classes_Arkanis.drawio.png) que ilustra a herança entre a classe Especialistas e as suas subclasses (Codificadores, Decodificadores, Obstinado), bem como a relação com o main.

Desenvolvido para o estudo de Programação Orientada a Objetos com Python.

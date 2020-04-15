"""
PEP8 - Python Enhancement Proposal
Proposta de melhorias para a linguagem Python

The Zen of Python: import this

A ideia da PEP8 é que possamos escrever códigos Python de forma pythônica (Python Zen);


[1] - Utiliza Camel Case para nomes de classes;
      Camel Case:
       - Nome simples: Inicial maiúscula. Ex: class Calculadora:
       - Nome composto: Iniciais maiúsculas e sem traço ou underline. Ex: CalculadoraCientifica

    Exemplos:
    class Calculadora:
        pass

    class CalculadoraCientifica:
        pass


[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis
      Ex: soma(), soma_valores(), valida_cpf(), valida_cnpj()

    Exemplos:
    def soma():
        pass

    def soma_valores():
        pass

    def valida_cpf():
        pass

[3] - Utilize 4 espaços para a indentação
    Cuidado ao usar o Tab, mesmo que ele esteja configurado para dar 4 espaços, isso pode mudar de editor para editor,
    e no final pode ocasionar problemas, habitue-se a usar 4 espaços.

[4] - Linhas em branco
    - Separar funções e definições de classe em 2 (duas) linhas em branco
    - Métodos dentro de uma mesma classe devem ser declarados com 1 (uma) única linha em branco;

[5] - Imports
    - Imports em pacotes diferentes, devem ser feitos em linhas separadas.
        Exemplo correto:
            import sys
            import os
        Exemplo errado:
            import sys, os


    - Imports de objetos/classes em um mesmo arquivo, podem ser feitos na mesma linha.
        Exemplo (pode ser utilizado):
            from types import StringType, ListType
        ou assim:
            from types import (
                StringType,
                ListTupe
            )

    - Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e antes
      de constantes ou variáveis globais. Eles devem ser agrupados seguindo a ordem:
        1. módulos da biblioteca padrão
        2. módulos grandes relacionados entre si (por exemplo, todos os módulos de e-mail usados pela aplicação)
        3. módulos específicos da aplicação

      Por Maicon Saraiva: Opcionalmente, se algum import for feito somente em um local bem específico (condicional),
        ele pode ser feito inline (não é recomendado pelo PEP8 mas já vi em alguns projetos e pacotes do pypi.

[6] - Espaços em expressões e instruções
    - Não faça (espaços desnecessários):
        funcao( algo[ 1 ], { outro: 2 } )
        algo (1)
        dict ['chave'] = lista [indice]
        x                 = 1
        y                 = 2
        variavel_qualquer = 3

    - Correto:
        funcao(algo[1], {outro: 2})
        algo(1)
        dict['chave'] = lista[indice]
        x = 1
        y = 2
        variavel_qualquer = 3

[7] - Termine sempre uma instrução com uma nova linha
    - o mesmo vale para o final de um arquivo .py, sempre deixei uma linha em branco no final.


[999] - O PEP8 implementa também um corretor ortográfico (spell check). No Pycharm, esse recurso já vem habilitado
      de forma nativa, porém com o idioma em inglês.
      Para traduzir para o português, basta baixar um dicionário. Um que encontrei foi:
      https://github.com/rafaelsc/IntelliJ.Portuguese.Brazil.Dictionary.git
"""

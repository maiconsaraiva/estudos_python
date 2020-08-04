"""
Herança (Inheritance)

A ideia de herança é podermos reaproveitar código e extender classes existentes, aproveitando tudo que uma classe
já tem, e implementando coisas novas nela.


Quando uma classe herda de outra, ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe (Ex: classe Pessoa), a classe herdada é chamada por um dos nomes abaixo:
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica

Quando uma classe herda de outra classe (ex: classes Cliente e Funcionario), ela é chamada por um dos nomes abaixo:
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;


Para fazermos acesso (sobrescrever) um método da classe pai, usamos o método "super().nome_metodo"

### Sobrescrita de Métodos (Overriding) ###
- Sobrescrita de método ocorre quando reescrevemos/reimplementamos um método existente na super classe em classes
filhas.
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf_cnpj):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf_cnpj = cpf_cnpj

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario(Pessoa):

    def __init__(self, nome, sobrenome, cpf_cnpj, salario, matricula):
        super().__init__(nome, sobrenome, cpf_cnpj)
        self.__salario = salario
        self.__matricula = matricula

    # Sobrescrevendo o método nome_completo
    def nome_completo(self):
        return f'{self._Pessoa__nome} {self._Pessoa__sobrenome} - {self.__matricula}'


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf_cnpj, limite_credito):
        super().__init__(nome, sobrenome, cpf_cnpj)
        self.__limite_credito = limite_credito


funcionario = Funcionario('Glenda', 'Lima', '123456789', 1500, 123)
cliente = Cliente('Maicon', 'Saraiva', '04652857594', 5000)

print(funcionario.nome_completo())
print(cliente.nome_completo())

print(cliente.__dict__)
# {'_Pessoa__nome': 'Maicon', '_Pessoa__sobrenome': 'Saraiva', '_Pessoa__cpf_cnpj': '04652857594', '_Cliente__limite_credito': 5000}
# Observe que, como os atributos são privados, o Name Mangling é feito respeitando quem é a classe que o implementa.



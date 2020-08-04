"""
POO -  Métodos

- São funções que representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu
sistema.

- Em Python, dividimos os métodos em 2 grupos:
  - Métodos de Instância
  - Métodos de Classe

Relembrando: Qualquer elemento em Python que inicia e finaliza com duplo underline, é chamado de
dunder (Double Underline). Esses métodos/funções em Python são chamados de métodos mágicos.

Obs: Por mais que possamos criar nossas próprias funções usando o dunder, não é recomendado. O Python possui vários
  métodos com esta forma de nomeclatura, e se criarmos funções também com essa nomeclatura, podemos acabar sobrepondo
  algum já existente.

  Esses métodos, conhecidos como métodos mágicos, são métodos da própria linguagem Python em suas classes internas
  que nós podemos usar/implementar para atender nossas necessidades.


### Métodos de Instância Privados ###

- Assim como os tributos, por convenção, criamos os métodos com duplo underline no inicio do nome do método.
Ex: __nome_metodo()
E assim como os atributos, os métodos privados também recebem o Name Mangling: _NomeClasse__nome_metodo_privado() que
pode ser usado de forma publica (embora por convenção, não deva ser usado).


### Métodos de Classe ###

Para definir que um método é de classe, nós usamos um decorator: @classmethod

Métodos de Classe do Python são conhecidos em outras linguagens como Métodos Estáticos (Static Method).

Quando criamos um método dentro de uma classe, e ele não faz nenhum uso de atributo ou outro método da instância,
o ideal é criarmos ele como um Método de Classe. No Pycharm, se tentarmos criar um método de instância que não faz
nenhum acesso à um atributo de instância ou método de instância, ele já emite um warning recomendado que o método
poderia ser um Método de Classe.

### Métodos Estáticos ###
Mesmo que os Métodos de Classe sejam também métodos estáticos, no Python temos os métodos específicamente estáticos.
A declaração deles é parecida com o Método de Classe, porém usa o decorator @staticmethod (no lugar de @classmethod.
A grande diferença entre um e outro, é que, o método estático não tem acesso à classe e aos atributos de classe, e
o método e classe, eles não precisam por exemplo ter obrigatoriamente o parâmetro "cls" como primeiro parâmetro.


"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    instance_count = 0

    def __init__(self, numero, limite, saldo):
        self.__id = ContaCorrente.instance_count + 1
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo


class Produto:

    instance_count = 0

    def __init__(self, nome: str, unidade, valor):
        self.__id = Produto.instance_count + 1
        self.__nome = nome
        self.__unidade = unidade
        self.__valor = valor
        self.first_name = self.__first_name()

    def desconto(self, porcentagem):
        """ Retorna o valor do produto com o desconto"""
        return self.__valor * (1 - (porcentagem/100))

    def __first_name(self):
        """Exemplo de método privado que retorna o primeiro do produto"""
        return self.__nome.split(' ')[0]


p1 = Produto('Teclado Megaware Multimedia', 'UN', 23.90)

# Método de Instância
print(p1.desconto(10))  # 21.51

p1.__first_name()  # AttributeError: 'Produto' object has no attribute '__first_name'
# Outra forma de fazer:
print(Produto.desconto(p1, 10))  # 21,51

print(p1.first_name)


"""
Métodos de Classe
"""
from datetime import datetime
import locale


# Define o locale (internacionalização) para o formato do windows)
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


class ContaCorrente:

    instance_count = 0

    @classmethod
    def get_saldo_todas_contas(cls) -> list:
        """Obtém o saldo de todas as contas do sistema
        Retorna uma list de dicionários, contendo os campos: Número, Data Ultimo Movimento, Saldo"""
        return [

            {'numero': '10658-5', 'data_ultimo_movimento': datetime.today().__format__('%x'), 'saldo': 1490},
            {'numero': '19995-8', 'data_ultimo_movimento': datetime.now().strftime('%x'), 'saldo': 35_000}
        ]

    @staticmethod
    def teste_metodo_estatico():
        return 'String Estática'

    def __init__(self, numero, limite, saldo):
        self.__id = ContaCorrente.instance_count + 1
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo


conta1 = ContaCorrente('10658-5', 5000, 1490)

# Forma correta
print(ContaCorrente.get_saldo_todas_contas())

# Forma incorreta. Possível, mas incorreta.
print(conta1.get_saldo_todas_contas())


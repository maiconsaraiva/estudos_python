""""
Polimorfismo

Poli -> Mitas
Morfis -> Formas

Polimorfismo são objetos que podem possuir/assumir muitas formas.

No exemplo abaixo, as classes herdam todas da super classe Animal, mas as classes Cachorro() e Gato() fazem a
reimplementação do método falar(), já que eles falam de forma diferente (um late e o outro mia).
Essa mudança, é chamada de polimorfismo.

Note também que, a classe Rato(), embora herde de animal, não tem a implementação do método "falar()".
Se, em uma instância da classe Rato() tentarmos acessar o método falar() será gerada uma exceção do tipo
NotImplementedError. Exceção esta que nós implementamos intencionalmente, para forçar todos que implementarem a herança
à partir da classe Animal() a reimplementarem o método falar(), conforme a necessidade.
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar este método.')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala: Au! au!')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala: Miauu!')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)


steve = Cachorro('Steve')
steve.comer()
steve.falar()

gato = Gato('Gato de Botas')
gato.comer()
gato.falar()

rato = Rato('Mickey')
rato.comer()
rato.falar()  # NotImplementedError: A classe filha precisa implementar este método.

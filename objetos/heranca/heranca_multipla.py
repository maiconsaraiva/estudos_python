"""
POO - Herança Multipla

Herança múltipla é a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde
todos os atributos e métodos de todas as classes herdadas.

Obs: A herança múltipla pode ser feita de duas formas:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;


# Exemplo 1 - Multiderivação Direta
class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass


# Exemplo 2 - Multiderivação Indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


# Indiretamente a classe abaixo herda de Base2 e Base1 também.
class MultiDerivadaIndireta(Base3):
    pass


OBS: Não importa se a derivação é direta ou indireta. A classse que realizar a herança herdará todos os atributos e
métodos de todas as super classes (classes pai).
"""


class Animal:
    """Class of animals"""
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def cumprimentar(self):
        print(f'Olá, sou o {self.__nome}')


class Aquatico(Animal):
    """Class of aquatic animals"""

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def nadar(self):
        return f'O animal {self._Animal__nome} está nadando.'

    def cumprimentar(self):
        return f'Olá, eu sou {self._Animal__nome} aquático.'


class Terrestre(Animal):
    """ Class of terrestre animals """

    def __init__(self, nome, especie):
        super().__init__(nome, especie)

    def andar(self):
        return f'{self._Animal__nome} está andando.'

    def cumprimentar(self):
        return f'Olá, eu sou {self._Animal__nome}, e sou aquático.'


class Pinguim(Aquatico, Terrestre):
    """Class of animal Pinguim"""
    def __init__(self, nome, especie):
        super().__init__(nome, especie)


pinguim = Pinguim('Tux', 'Aquatico e Terrestre')


print(pinguim.andar())
print(pinguim.nadar())
print(pinguim.cumprimentar())  # Olá, eu sou Tux, e sou aquático.
# Note que o método "cumprimentar()"" existe nas duas super classes Aquatico e Terrestre. E como o pinguim herda das
# duas, qual dos dois métodos ele vai executar?
# R: Por padrão ele executa o da classe que foi informada primeiro na herança: Aquatico.
# Esse tipo de tratamento é chamado de "Method Resolution Order - MRO"



# Verificando de qual classe é uma instância:

print(f'Tux é instãncia de Animal: {isinstance(pinguim, Animal)}')  # True
print(f'Tux é instãncia de Aquatico: {isinstance(pinguim, Aquatico)}')  # True
print(f'Tux é instãncia de Terrestre: {isinstance(pinguim, Terrestre)}')  # True
print(f'Tux é instãncia de Object: {isinstance(pinguim, object)}')  # True




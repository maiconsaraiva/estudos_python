"""
MRO - Method Resolution Order (Ordem de Execução dos Métodos)

Quando temos herança multipla, e existe um mesmo método em ambas as super classes, o Python usa o MRO para determinar
qual dos dois métodos será executado.

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


print(pinguim.cumprimentar())  # Olá, eu sou Tux, e sou aquático. (executa o método da classe Aquatico)

# Verificando o MRO. O método __mro__ retorna uma tupla com todas as classes do qual Pinguim herda,
# e na ordem de execução determinada pelo Python, ou melhor, de acordo com a declaração/construção das classes (MRO)
print(Pinguim.__mro__)
"""
Resultado:
 (<class '__main__.Pinguim'>, <class '__main__.Aquatico'>, <class '__main__.Terrestre'>, <class '__main__.Animal'>, <class 'object'>)


Obs:
Além do __mro__, é possível obter essa informação usando:
    Pinguim.mro() -> Retorna a mesma tupla mencionada acima.

    Usando o help: help(Pinguin) que exibe a documentação da classe, e faz parte dessa documentação a lista do MRO.
        Neste caso o resultado não vem em uma tupla, e sim como parte da documentação help() da classe.
"""
print(Pinguim.mro())

print(help(Pinguim))

"""
Resultado para: print(help(Pinguim))

class Pinguim(Aquatico, Terrestre)
 |  Pinguim(nome, especie)
 |
 |  Class of animal Pinguim
 |
 |  Method resolution order:
 |      Pinguim
 |      Aquatico
 |      Terrestre
 |      Animal
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, nome, especie)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Aquatico:
 |
 |  cumprimentar(self)
 |
 |  nadar(self)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Terrestre:
 |
 |  andar(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Animal:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
"""


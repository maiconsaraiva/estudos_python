"""
POO - O método super()

O método super() se refere à super classe (classe pai)
"""


class Animal:
    """Class of animals"""
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz: {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca


gato = Gato('Félix', 'Gato', 'Siberiano')

gato.faz_som('miau')

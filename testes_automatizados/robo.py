class Robo:

    def __init__(self, nome, bateria=100, habilidades=[]):
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @property
    def habilidades(self):
        return self.__habilidades

    def carregar(self):
        self.__bateria = 100

    def dizer_nome(self):
        if self.__bateria > 0:
            self.__bateria -= 1
            return f'BEEP, BOOP, BEEP, BOOP. Eu sou o robô {self.__nome}'
        return 'Bateria fraca ou descarregada! Por favor, recarregue.'

    def aprender_habilidade(self, nova_habilidade, custo_bateria):
        if self.__bateria >= custo_bateria:
            self.__habilidades.append(nova_habilidade)
            self.__bateria -= custo_bateria
            return f'Nova habilidade aprendida com sucesso!'
        return 'Bateria insuficiente. Por favor, recarregue e tente novamente.'

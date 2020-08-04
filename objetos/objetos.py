"""
POO - Objetos

São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação computacional,
devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de uma classe como
variáveis do tipo definido na classe.
"""
from datetime import datetime
from locale import setlocale, LC_ALL
# Define o locale (internacionalização) para o formato do windows)
setlocale(LC_ALL, 'pt_BR.utf8')


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def ligada(self):
        return self.__ligada

    def ligar_desligar(self):
        """ Liga a lâmpada caso ela esteja desligada, ou desliga, caso esteja ligada """
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


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


lamp1 = Lampada('branca', 220, 60)

print(lamp1.ligada())  # False
lamp1.ligar_desligar()
print(lamp1.ligada())  # True

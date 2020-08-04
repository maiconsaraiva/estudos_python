"""
POO - Propriedades (properties)


Criando os getters e setters.

Em linguagens como o Java, ao declararmos atributos privados nas classes, costumamos criar métodos públicos para
manipulação desses atributos. Esses métodos são conhecidos por getters e setters, onde os getters retornam o valor do
atributo, e os setters alteram o valor do mesmo.

Exemplo de como seria feito seguindo algo parecido com o Java:
    def get_numero(self):
        return self.__numero

    def set_numero(self, value):
        self.__numero = value
"""


class Conta:

    instance_count = 0

    def __init__(self, numero, titular, limite, saldo):
        self.__id = Conta.instance_count + 1
        Conta.instance_count += 1
        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, value):
        self.__limite = value

    @property
    def saldo(self):
        return self.__saldo

    def extrato(self):
        return f'Conta: {self.__numero} \nSaldo: {self.__saldo}.\nLimite cheque especial: {self.__limite}'

    def depositar(self, valor):
        """Deposita um novo valor na conta e retorna o saldo atualizado.
        Aceita apenas valores positivos """
        if not valor > 0:
            raise ValueError(f'O valor precisa ser positivo  (maior que 0). Valor informado: {valor}')
        self.__saldo += valor
        return self.__saldo

    def sacar(self, valor):
        """Faz um saque da conta. Retorna o saldo atualizado
        Aceita apenas valores positivos """
        if not valor > 0:
            raise ValueError(f'O valor precisa ser positivo  (maior que 0). Valor informado: {valor}')
        if not valor <= self.__saldo:
            raise ValueError(f'Saldo insuficiente. Saldo atual: {self.__saldo}')
        self.__saldo -= valor
        return self.__saldo

    def transferir(self, valor, conta_destino):
        """Transfere o valor para uma outra conta"""
        if not valor > 0:
            raise ValueError(f'O valor precisa ser positivo (maior que 0). Valor informado: {valor}')

        if not self.__saldo >= valor:
            raise ValueError(f'Transferência Cancelada! A conta origem "{self.__numero}" não possui saldo '
                             f'suficiente para retirada da transferência. Saldo atual: {self.__saldo}')

        self.sacar(valor)
        conta_destino.depositar(valor)


conta1 = Conta('10658-5','Maicon J S Oliveira', 1000, 5000)

print(conta1.limite)
conta1.limite = 2000
print(conta1.limite)

print(conta1.numero)
conta1.numero = '19995-8'  # AttributeError: can't set attribute (atributo somente leitura)




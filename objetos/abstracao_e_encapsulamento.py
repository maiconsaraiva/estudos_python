"""
POO - Abstração e Encapsulamento

O grande objeto da programação orientada a objeto é encapsular o nosso código dentro de um grupo lógico e hierarquico
utilizando classes.

Abstração em POO, é o ato de expor dados relevantes de uma classe, escondendo atributos e métodos privados do usuário.
Fazendo uma analogia a um Smartphone, quando ligamos para alguém, simplesmente clicamos no ícone de ligação, digitamos
o número ou buscamos nos contatos, e iniciamos a chamada. Após fazermos isso, de forma não visual, o nosso aparelho
vai se conectar com a central da operadora, informar que estamos tentando uma ligação para um número desejado, e a
operadora vai rastrear e encontrar o dono daquele número, ao encontrar irá dar o sinal de que está tocando no celular
da pessoal para o qual ligamos, quando a pessoa atender, a operadora permitirá que as duas pessoas se falem
diretamente. O processo envolvido "por baixo dos panos" foi abstraido para que o usuário não precise ver ou nem mesmo
saber de coisas que ele não pode ou não precisa saber.
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
        # conta_destino.__saldo += valor  # Por que estou conseguindo acessar este atributo privado?
        conta_destino.depositar(valor)


conta = Conta('10658-5', 'Maicon Saraiva', 5000, 0)

# print(conta._Conta__saldo)  # Acesso errado (Name Mangling(

print(conta.depositar(100))

print(conta.extrato())

# print(conta.depositar(-1))  # ValueError: O valor precisa ser positivo e (maior que 0). Valor informado: ##

# print(conta.sacar(2000))  # ValueError: Saldo insuficiente: XX

conta2 = Conta('19995-8', 'Sismais Tecnologia', 10000, 35_000)

conta2.sacar(300)

# Transfere valor da conta
conta2.transferir(4500, conta)
# conta2.transferir(35000, conta)  # Transferência Cancelada! A conta origem "19995-8" não possui saldo suficiente...

print(f'Extrato da conta {conta._Conta__numero}:\n{conta.extrato()} ')

print(f'Extrato da conta {conta2._Conta__numero}:\n{conta2.extrato()} ')

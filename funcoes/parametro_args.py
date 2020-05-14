"""
 Entendendo o *args

 - O parâmetro do tipo "*args" é um parâmetro de entrada como outro qualquer.
   Isso significa que você poderá chamar de qualquer coisa, desde que comece com asterisco.
   Ex: *argumentos
   Mas por convenção (padronização) a comunidade decidiu que iria adotar o nome "args" para defini-lo.,

- O parâmetro *args coloca os valores extras informados como uma entrada em uma tupla.
  Então, desde já lembre-se que tuplas são imutáveis.

- Sabendo que o "args" dentro da função é uma tupla. Tudo que fazemos com tuplas, podemos fazer com o args.
"""


# Qual a vantagem do *args?

# No exemplo abaixo temos uma função que soma 3 números passados no parâmetro
"""
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3
print(soma_todos_numeros(1, 1, 1))  # Result: 3
"""


# E se quisermos criar uma função semelhante à anterior, mas que nos permita
# informar quantos numeros quisermos para serem somados?
# O *args vem para resolver esse problema. Nós passamos quantos parâmetros quisermos, e dentro da função crada,
# os parâmetros passados ficam armazenados dentro de "args", e "args" se torna uma tupla.
def soma_todos_numeros(*args):
    print(args)
    print(sum(args))


soma_todos_numeros(1, 2, 3)
soma_todos_numeros(1, 2, 3, 4)
soma_todos_numeros(1, 2, 3, 4, 5)


# o *args também pode ser usado em conjunto com outros parâmetros, mas ele tem que ficar no final
def total_pedidos_cliente(codigo_cliente, nome_cliente, *args):
    print('Total dos pedidos de {0} - {1}'.format(codigo_cliente, nome_cliente))
    print(sum(args))


total_pedidos_cliente('000001', 'Maicon Saraiva')  # O *args é opcional. Neste exemplo eu não passei eles.
total_pedidos_cliente('000002', 'Glenda Lima', 19.90, 10.50, 15.80)


# Outro exemplo de utilização de *args

def verifica_logins(*args):
    if ('SISMAIS' in args) or ('interprise' in args) or ('sismais' in args):
        return "Ok! Um dos logins informados é permitido."
    else:
        return 'Logins não estão na lista de permitidos.'


print(verifica_logins(30, 'teste', 'maicon', 'MAICON', 10.50))  # Result: Logins não estão na lista de permitidos.
print(verifica_logins('sismais', 'maicon', 'MAICON', 21, 1947))  # Result: Ok! Um dos logins informados é permitido.
print(verifica_logins('interprise'))  # Result: Ok! Um dos logins informados é permitido.


# Cuidado ao passar parametros que são de outros tipos para o args
# No exemplo abaixo, embora nós passemos uma lista de números junto com mais parâmetros, essa lista de números será
# entendida dentro do "args" como somente 1 (um) elemento da tupla, sendo um elemento do tipo "lista"
# Exemplo:
lista = [20, 30, 40]

def teste_lista(*args):
    print(args)
    print(sum(args))

teste_lista(20, 30, 40, 50, 60) # Result: (20, 30, 40, 50, 60) | 200
# teste_lista(lista, 50, 60)  # Result: ([20, 30, 40], 50, 60) | TypeError: unsupported operand type(s) for +: 'int' and 'list'


# Usando o desempacotamento para passar uma lista de valores no *args:
# Exemplo clássico:
lista = [20, 30, 40, 50]
num1, num2, num3, num4 = lista
teste_lista(num1, num2, num3, num4)  # Result: (20, 30, 40, 50) | 140

# Exemplo usando recurso pronto do python:. Basta passar a variável "lista" com o "*" na frente:
teste_lista(*lista, 60, 70)  # Result: (20, 30, 40, 50, 60, 70) | 270
# Obs: o "*" (asterisco) serve para  que informemos ao Python que estamos passando como argumento, uma coleção de dados.
# Desta forma, ele saberá que precisa desempacotar estes dados.

# A lógica serve também para tuplas:
tupla = (5, 10, 15, 20)
teste_lista(*tupla)  # Result: (5, 10, 15, 20) | 50

# A lógica serve também para tuplas:

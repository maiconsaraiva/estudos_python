"""
Reduce
- A partir do Python3+ a função reduce() não é mais uma função integrada do python (built-in).
  Agora temos que importar e utilizar esta função a partir do módulo 'functools'

- O próprio Guido Van Rossum, criado do Python disse sobre o reduce:
  "Utilize a função reduce() se você realmente precisar dela. Em todo caso, 99% das vezes, um loop for é mais legível"

Para entender o reduce, imagine que você tem uma coleção de dados:
iteravel = [a1, a2, a3, a4, ..., an]
e tem uma função que recebe dois parâmetros:
def funcao(x, y):
    return x * y


Assim como map() e filter() a função reduce() recebe dois parâmetros: uma função e um iterável.

reduce(funcao, iteravel)

A função reduce funciona da seguinte forma:
  Passo 1: res1 = funcao(a1, a2)  # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
  Passo 2: res2 = funcao(res1, a3)  # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda
  Isso é repetido até o final:
  Passo 3: res3 = funcao(res2, a4)
  .
  .
  .
  Passo N: resN = funcao(resM, aN)

 Ou seja, em cada passo, ela aplica a função passando como primeiro argumento, o resultado da aplicação anterior.
 No final, reduce() irá retornar o resultado retornado pela última execução da função

"""


# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista

# importando a função
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 23, 29, 50]

# Lembrando: para usar o reduce() a função precisa ter dois parâmetros de entrada

resultado = reduce(lambda x, y: x * y, dados)

print(resultado)  # Resultado: 68102034000

"""
É o mesmo que:
(2 * 3) = 6
(6 * 4) = 24
(24 * 5) = 120
(120 * 7) = 840
(840 * 11) = 9240
(9240 * 13) = 120120
(120120 * 17) = 2042040
(2042040 * 23) = 49966920
(49966920 * 29) = 1362040680
(1362040680 * 50) = 68102034000 (resultado final)
"""



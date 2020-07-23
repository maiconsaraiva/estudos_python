"""
Teste de Memória com Generators

Os Generator utilizam menos memória de armazenamento.
Obs: Embora tenha essa economia, não tem necessáriamente a economia no desempenho durante a execução.

Sequencia de Fibonacci:
1, 1, 2, 3, 5, 8, 13...

"""

"""
# Teste 1: Usando Listas: 464MB
def fib_lista(max):

    '''Função para gerar uma sequência de Fobonnaci

    Args:
        max ([int]): [Número máximo de números/elementos retornados na lista]
    '''
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b

    return nums


lista = fib_lista(20)
print(lista)  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]


for n in fib_lista(100000):
    print(n)
"""

# Teste 2: Função usando geradores: 2,4MB
def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


for n in fib_gen(100000):
    print(n)

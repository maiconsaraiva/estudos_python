"""
Tool for measuring execution time of small code snippets.

https://docs.python.org/3.8/library/timeit

A função timeit.timeit() recebe dois parâmetros. O primeiro é uma string contendo a função que a gente quer executar,
e o segundo é o número de vezes que a gente quer executar. O retorno, será o tempo em segundos que levou para executar
a função nas N vezes que foram passadas no parâmetro "number".

Podemos saber se nossa função é tem performance o suficiente.
"""
import timeit
import functools


# Marcando tempo de execução do código com timeit
# Loop for
tempo = timeit.timeit('" - ".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('" - ".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# Map
tempo = timeit.timeit('" - ".join(map(str,range(100)))', number=10000)
print(tempo)


# functools
def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(teste(5))

# Com a funtools, podemos passar qualquer função desejada como parâmetro para o timeit
tempo = timeit.timeit(functools.partial(teste, 2), number=1000)
print(tempo)

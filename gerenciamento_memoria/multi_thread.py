"""
Multi Thread (com o GIL sendo aplicado)
"""

import time
from threading import Thread


CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


t1 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))
t2 = Thread(target=contagem_regressiva, args=(CONTADOR//2,))

inicio = time.time()

t1.start()
t2.start()

# aguarda ambas as threads terminarem
t1.join()
t2.join()

fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')

# 3.335008144378662
"""
Veja que, mesmo utilizando multi thread, o GIL faz que o programa Python rode como se fosse uma única thread, então
o desempenho usando multi thread não tem tanta diferença em relação ao single thread.

A utilização do GIL prejudica a real utilização de multi thread e multi-cores nas máquinas, o que torna os projetos
Python lentos em alguns casos.
Por outro lado, o GIL torna as aplicações single-thread muito performáticas, e a grande maioria das aplicações não
precisam utilizar multi-thread.

Caso você tenha problemas com o GIL, você poderá utilizar multi-processing ao invés de multi-threading.
Utilizando processos ao invés de threads, cada processo Python ganha seu próprio interpretador Python e espaço em
memória. Desta forma o GIL não será problema.
"""

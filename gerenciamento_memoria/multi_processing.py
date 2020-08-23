"""
Multi Processing

Caso você tenha problemas com o GIL, você poderá utilizar multi-processing ao invés de multi-threading.
Utilizando processos ao invés de threads, cada processo Python ganha seu próprio interpretador Python e espaço em
memória. Desta forma o GIL não será problema.


IMPORTANTE: Embora seja mais rápido, é preciso ficar claro que, multi-processing são mais 'pesados' para a memória do
que multi-threading, pois, em cada processo teremos um ambiente Python próprio.

Interpretadores Alternativos Python:

Conforme mencionado antes, o Python possui múltiplas implementações, dentre as principais:
CPython, Jython, IronPython, e PyPy, escritos em C, Java, C# e Python respectivamente.

GIL só existe na implementação original (CPython). Então, se seu programa estiver rodando em outra implementação,
você não terá o problema que o GIL traz.

Você pode testar outros interpretadores Python sem mudar nada no seu código. Pode ver inclusive a performance de
multi-thread já que, as outras implementações não tem o GIL.
O PyPy é o Python feito em Python, ele é um exemplo de interpretador que é muito performático.

"""
import time
from multiprocessing import Pool


CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    pool = Pool(processes=2)
    inicio = time.time()
    r1 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    r2 = pool.apply_async(contagem_regressiva, [CONTADOR//2])
    pool.close()
    pool.join()
    fim = time.time()
    print(f'Tempo em segundos: {fim - inicio}')
    # 2.0229504108428955
    # Mais rápido que o single-thread e que o multi-thread.

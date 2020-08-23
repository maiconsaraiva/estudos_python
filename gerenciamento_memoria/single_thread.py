"""
Sigle Thread
"""
import time
from threading import Thread


CONTADOR = 50_000_000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')


# 3.6912050247192383

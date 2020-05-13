"""
Módulo Collections - Deque
https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta performance.
"""

# Import
from collections import deque

# Criando deques

deq = deque('geek')
print(deq)  # Result: deque(['g', 'e', 'e', 'k'])
print(type(deq))  # Result: collections.deque

# Adicionando elementos no final da lista
deq.append('U')
print(deq)

# Adicionando elementos no início a lista
deq.appendleft('A')
print(deq)  # Result: deque(['A', 'g', 'e', 'e', 'k', 'U'])

# Removendo o último elemento
elemento = deq.pop()
print(f'Elemento removido: {elemento}')

print(deq)

# Removendo o primeiro elemento
elemento = deq.popleft()
print(f'Elemento removido: {elemento}')

print(deq)



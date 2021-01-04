"""
Módulos Built-In são módulos integrados (que já vem instalados no Python)

- Módulos built-in são diferentes de funções built-in.
- As funções built-in são integradas e prontas para usar a qualquer momento.
  Para listar todas as funções built-in:
  dir(__builtins__)

- Já os módulos built-in são módulso que também vem instalados, mas devem ser importados para utilização.
  Essa importação evita que a memória fique sobrecarregada, já que iremos importar somente aquilo que desejamos 
  utilizar.
  Lista com todos os módulos built-ins do Python:
  https://docs.python.org/3/py-modindex.html






"""
# Forma recomendada para realizar multiplos imports:
from random import (
    randint,
    random,
    randrange,
    shuffle,
    choice
)

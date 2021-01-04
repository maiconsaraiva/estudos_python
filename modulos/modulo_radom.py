"""
Módulo Random e o que são módulos?

- Módulo Random -> Possui várias funções para geração de números pseudo-aleatórios

- Em Python, módulos nada mais são do que outros arquivos Python.

- Existem duas formas de se utilizar um módulo ou função dentro dele
Forma 1: Importando o módulo completo (Não recomendado);
    - Ex: import nome_modulo
    - Ao realizar o import do módulo completo, todas as funções, atributos, classes e propriedades que estiverem
      dentro dele, ficarão disponíveis (ficarão em memória). Caso você saiba quais funções precisa utilizar,
      então a melhor forma é fazendo o import somente dela.
      Ex: from nome_modulo import nome_funcao
Forma 2: Importando apenas função, ou funções que desejamos utilizar dentro daquele módulo.

"""

from biblioteca import nome_completo
import random


print(nome_completo('Maicon', 'Saraiva'))

print(random.randint(1, 1000))

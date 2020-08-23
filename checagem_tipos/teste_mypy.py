"""
Ferramenta MyPy - Optional Static Typing for Python
http://mypy-lang.org

Vai além do Type Hint e faz a checagem de tipos de fato.

O MyPy nasceu para ser uma nova linguagem de programação, derivada do Python e com tipagem estática.
Depois de um tempo, ele foi reescrito, não para ser uma nova linguagem, e sim para ser um checador de tipos da
linguagem oficial do Python.

Ele trabalha em conjunto com o Type Hinting

É instalado como um pacote normal Python:
pip install mypy

E sua utilização é feita da seguinte forma:
mypy nome_modulo.py
"""


def cabecalho(texto: str, alinhamento: bool = False) -> str:
    if not alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('maicon saraiva'))
print(cabecalho('maicon saraiva', True))

print(cabecalho('maicon saraiva', 'oiiii'))
"""
mypy teste
Ao rodar esse modulo com o mypy, a linha acima irá gerar o seguinte erro:

teste_mypy.py:29: error: Argument 2 to "cabecalho" has incompatible type "str"; expected "bool"
Found 1 error in 1 file (checked 1 source file)

"""


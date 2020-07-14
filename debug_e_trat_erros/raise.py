"""
raise -> Lança exceptions

Obs: Não é uma função e sum uma palavra reservada, assim como "def", -"None", etc.

Serve para gerando nossos próprios erros para o Python.

A forma geral utilizada é:
raise TipoDoErro('Mensagem de Erro')

raise ValueError('Valor incorreto')  # ValueError: Valor incorreto
"""


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('"texto" precisa ser do tipo "str"')
    if type(cor) is not str:
        raise TypeError('"cor" precisa ser do tipo "str"')

    # Apenas essas três cores são permitidas
    cores = ('azul', 'amarelo', 'branco')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre:{cores}')

    print(f'Texto: {texto}, Cor: {cor}')


# colore('Maicon', 'azul')  # Texto: Maicon, Cor: azul
# colore(True, 'azul')  # TypeError: "texto" precisa ser "str"
# colore('Maicon', 4)  # TypeError: "cor" precisa ser do tipo "str"
# colore('Maicon', 'laranja')  # ValueError: A cor precisa ser uma entre:('azul', 'amarelo', 'branco')


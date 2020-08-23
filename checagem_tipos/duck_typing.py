"""
Duck Typing

Diz o seguinte: O tipo ou a classe de um objeto é menos importante do que a classe que o define. Ao invés de checar
a classe ou o tipo de dado, é checado a presença ou não de métodos específicos.

A ideia do uso do nome Duck Typing é:
Se algo: anda como um pato, parece com um pato e nada como um pato, então é um pato.
Ou seja, significa que métodos similares, devem ter métodos e comportamentos similares.
"""


class CisneNegro:

    def __len__(self):
        return 42


livro = CisneNegro()

print(len(livro))

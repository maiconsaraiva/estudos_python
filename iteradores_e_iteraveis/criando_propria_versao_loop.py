"""
Criando a própria versão do loop
"""


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Maicon Saraiva')
meu_for([1, 2, 3, 4, 10, 20])

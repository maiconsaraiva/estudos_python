"""
Tipos em Comentários

Prós:
- O MyPy reconhece;
- A IDE também;

Contra:
- Não é recomendado, já que podemos fazer isso direto no código;

"""
import math


def circunferencia(raio):
    # type: (float) -> float
    return 2 * math.pi * raio


print(circunferencia(8))


# Outra forma que pode ser encontrada por ai:
# Muito estranho e muito ruim.
def cabecalho(
    texto, # type: str
    alinhamento = True # type: bool
):  # type: (...) -> str
    if alinhamento:
        return 'a'
    else:
        return 'b'

print(cabecalho('maicon', True))

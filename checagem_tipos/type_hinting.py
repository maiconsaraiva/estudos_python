"""
Type Hinting
https://docs.python.org/3/library/typing.html

O que é?
É uma solução formal, de indicar estaticamente o tipo de um dado, em uma linguagem de programação em que a tipagem é
dinâmica. Como é o caso do Python.

Lembrando que essa é uma implementação que veio da PEP 484, e entrou em vigor à partir do Python 3.5.


Obs:
- Essa abordagem de tipagem estática não é algo muito usado no cotidiano do Python

Prós e Contas

Prós:
- Facilita a detecção de erros (com ajuda da própria IDE ou ferramentas como MyPy)
- Melhora a documentação do código. Se houver mais pessoas trabalhando por exemplo, a pessoa já irá saber qual o tipo
deve ser passado como argumento.
- Melhora a funcionalidade das IDE's para Code Completion e Sugestões de Correção


Contras:
- Para o Python não é comum ainda usar essa abordagem, então é na verdade estranho ainda usar Type Hint no
desenvolvimento Python;
- Apesar do Type Hint ter sido implementado já na versão 3.5 do Python, foi só na versão 3.7 que o recurso ficou
completo.
- Fazendo o uso de tipos, temos uma ligeira queda de performance na execução dos programas Python.
(Eu achei que isso iria ajudar a ter mais performance).


Obs: Se a velocidade não for tão importante, a recomendação é que você sempre utilize o Type Hinting para ter um
sistema mais robusto e livre de erros.
"""


def cumprimentar(nome: str) -> str:
    return f'Olá, {nome}'


print(cumprimentar('Maicon'))  # Olá, Maicon
print(cumprimentar(1))  # Olá, 1
"""
Note que, embora o parâmetro "nome" na função tenha sido especificado como str, se eu passar o inteiro ela funciona
normalmente. Isso por que o Type Hint é apenas um alerta, mas não impede a execução.
Existem no entanto ferramentas que fazem verdadeiramente a checagens dos tipos, e geram erro caso a tipagem não seja
obedecida. Uma delas é o MyPy

Ela pode ser utilizada por exemplo para que IDE's como o Pycharm emitam um alerta sobre a tipagam.
Outra vantagem do Type Hint é que, a IDE consegue fornecedor melhor o Code Completion / Code Insight
"""

def cabecalho(texto: str, alinhamento: bool = False) -> str:
    if not alinhamento:
        return f'{texto.title()}\n{"-" * len(texto)}'
    else:
        return f' {texto.title()} '.center(50, '#')


print(cabecalho('maicon saraiva'))
print(cabecalho('maicon saraiva', True))

print(cabecalho('maicon saraiva', alinhamento='oiiii'))  # Embora eu não tenha passado boolean


"""
Para definir a tipagem dentro de tipos avançados (lista, dicionário, tupla) existe um módulo builtin do Python, que é
o "typing", ele permite declararmos tipos avançados e quais os tipos que serão permitidos dentro deles.

Exemplos:
"""
from typing import Dict, List, Tuple, Set

nomes: List[str] = ['Maicon', 'Glenda']

versoes: Tuple[int, int, int] = (1, 2, 3)

# Dicionário, onde a chave é string e o valor é bool
opcoes: Dict[str, bool] = {'ar_condicionado': True, 'banco_couro': False}

valores: Set[int] = {3, 4, 5, 6, 10}

print(nomes)  # ['Maicon', 'Glenda']
print(versoes)  # (1, 2, 3)
print(opcoes)  # {'ar_condicionado': True, 'banco_couro': False}
print(valores)  # {3, 4, 5, 6, 10}

print(__annotations__)
# {'nomes': typing.List[str], 'versoes': typing.Tuple[int, int, int], 'opcoes': typing.Dict[str, bool],
# 'valores': typing.Set[int]}

"""
Preservando metadados com wraps

Metadados -> São dados intrínsecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalidades.

"""


# Problema
def ver_log(funcao):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma a + b"""
    return a + b


# O problema:
print(soma.__name__)  # logar
print(soma.__doc__)  # Eu sou uma função (logar) dentro de outra

# Nos exemplos acima, o __name e __doc__ retornam os dados da Decorator Function, e não da função soma propriamente.
# Ou seja, os metadados da função são alterados por intermedio do decorator
# É ai que entra o papel dos wraps


# ##################################################################
# Resolução do Problema

# Primeiro fazemos import do wraps
from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # <<<<<<<<<<<<<< O uso do @wrap(funcao) resolve o problema
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma a + b"""
    return a + b


# O problema resolvido:
print(soma.__name__)  # soma
print(soma.__doc__)  # Soma a + b

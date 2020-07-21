"""
Try  / Except / Else / Finally

Dica de quando e onde tratar o código:
- Toda entrada do usuário deve ser tratada! Isso já irá evitar diversos erros.

-> Else: É executado somente se não houver o erro.
-> Finally: É executado incondicionalmente, mesmo se der erro.
   Geralmente é usado para fechar, ou desalocar recursos.
"""

"""
repete = True
while repete:
    try:
        entrada = input('Informe um Número: ')
        num = int(entrada)
        repete = False
        print(f'Número digitado: {num}')
    except ValueError:
        print(f'"{entrada}" não é um numero válido')
"""

"""
# Exemplo com o Else
try:
    entrada = input('Informe um Número: ')
    num = int(entrada)
    print(f'Número digitado: {num}')
except ValueError:
    print(f'"{num}" não é um numero válido')
else:
    print(f'Número digitado: {num}')
"""

"""
# Exemplo com Finally
try:
    entrada = input('Informe um Número: ')
    num = int(entrada)
except ValueError:
    print(f'"{entrada}" não é um numero válido')
else:
    print(f'Número digitado: {num}')
finally:
    print('Execução concluída!')  # Sempre irá executar, mesmo que dê alguma exception
"""

"""
# Exemplo com função
def dividir(a, b):
    return a / b

try:
    res = dividir(5, 0)
    print(res)
except ValueError:
    print('Divisão inválida!')
"""


# Exemplo com tratamento semi-genérico
def dividir(a, b):
    return a / b


try:
    res = dividir(5, 0)
    print(res)
except (ValueError, ZeroDivisionError) as err:
    print(f'Divisão inválida: {err}')

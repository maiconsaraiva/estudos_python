"""
Tipo de Dados Booleano ( bool, em outras linguagens também pode ser representando como "boolean" )

Vem da Álgebra Booleana, criada por George Boole

Os resultados serão sempre 2 tipos
True -> Verdadeiro
False -> Falso

IMPORTANTE: A atribuição/comparação deverá ser sempre com a ínicial do False e True em maiúscula.
  # Errado: true, false
    b_conectar = false
  # Correto: True, False
    b_conectar = False

"""

b_ativo = False
print(f'Valor da variavel b_ativo: {b_ativo}')


""" 
Operações básicas envolvendo o tipo Boolean
"""

# Negação (not)
if not b_ativo:
    print('Não está ativo')

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro para que a condição seja
executada.

True or True -> True
True or False -> True
False or False -> False
False or True -> True
"""
print('Acesso ao sistema está ativo?')
b_ativo_definitivamente = False
b_ativo_temporariamente = True
if b_ativo_definitivamente or b_ativo_temporariamente:
    print('Sim, está ativo.')
    if (not b_ativo_definitivamente) and b_ativo_temporariamente:
        print('Mas está ativo apenas temporariamente')
    else:
        print('E é definitivamente.')

# E (and)
"""
Também é uma opção binária, ou seja, depende de dois valores. Para que a condição seja executada, ambos os valores
devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and True -> False
"""
print('Usuário está logado?')
b_ativo = False
b_logado = True
if b_ativo:
    if b_logado and b_ativo:
        print('O usuário está logado no sistema!')
    else:
        print('O usuário não está logado')
else:
    print('Usuário INATIVO!')

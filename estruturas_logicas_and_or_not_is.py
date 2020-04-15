"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
  - not
Operadores binários:
  - and, or, is

Para o 'and', ambos os valores devem ser True
Para o 'or', um ou outro valor precisa ser True
"""

print('Acesso ao sistema está ativo?')
ativo_definitivamente = False
ativo_temporariamente = True
if ativo_definitivamente or ativo_temporariamente:
    print('Sim, está ativo.')
    if (not ativo_definitivamente) and ativo_temporariamente:
        print('Mas está ativo apenas temporariamente')
    else:
        print('E é definitivamente.')

idade = 18

if idade is 18:
    print('Idade é 18!')

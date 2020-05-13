"""
Módulo Collections - Default Dict
https://docs.python.org/3/library/collections.html#defaultdict-objects

Default Dict -> São dicionários que quando criados definimos um valor default, podendo ser utilizado uma função Lambda, 
                esse valor será utilizado sempre que não houver um valor definido para uma chave.

# Diferenças entre o DefaultDict e o Dict tradicional:
  - Ao acessarmos uma chave que não existe, não será gerado um KeyError, ao contrário, a chave será criada e valor irá
    receber o valor default (passado na criação do DefaultDict)


Obs: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.    
"""

# Exemplo em dicionário comum
pessoa = {'nome':'Maicon', 'idade': 29, 'sobrenome': 'Saraiva', 'endereco': 'Rua Ranulfo Costa'}

print(pessoa)
print(pessoa['nome'])
# print(pessoa['cidade'])  # Gera um KeyError

# Exemplo com DefaultDict

from collections import defaultdict
pessoa2 = defaultdict(lambda: 'valordefault')
pessoa2['nome'] = 'Maicon'
# "sobrenome" ainda não existe, mas em vez de termos um KeyError, ele irá criar o elemento usando o valor default "valordefault"
print(pessoa2['sobrenome'])   # Resultado: valordefault
print(pessoa2)  # Resultado: defaultdict(<function <lambda> at 0x012EB538>, {'nome': 'Maicon', 'sobrenome': 'valordefault'})
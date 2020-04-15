"""
Tipos de dados no Python

- Númerico / Inteiro

"""

""" A atribuição de valores a variáveis pode ser feita de forma agrupada
 (com as variáveis e valores de atribuição separados por vírgulas)
"""
# Exemplo clássico:
variavel_1 = 'Teste'
variavel_2 = 'Teste2'
# Exemplo com atribuição agrupada
variavel_3, variavel_4 = 'Teste3', 'Teste4'
variavel_int, variavel_float, variavel_string = 1, 4.55, 'Teste String'

""" 
Saber o tipo de dados de uma variável:
  type(variavel)
Exemplo: 
  num = 5
  type(num) # Resultado: int
  num = 5.5
  type(num) # Resultado: float
  
  texto = 'Teste de string'
  type(texto) # Resultado: str 
"""

# Exemplos, verificando o tipo da variável e executando um código condicional
variavel = 'Texto string'
if type(variavel) is str:
    print(f'"variavel" com o conteúdo "{variavel}" é uma string.')
else:
    print(f'"variavel" com o conteúdo "{variavel}" NÃO é uma string')

variavel = '1.5'  # Continua sendo uma string
if type(variavel) is str:
    print(f'"variavel" com o conteúdo "{variavel}" CONTINUA sendo uma string.')
else:
    print(f'"variavel" com o conteúdo "{variavel}" NÃO é uma string')

variavel = 1.5
if type(variavel) is str:
    print(f'"variavel" com o conteúdo "{variavel}" é uma string.')
else:
    print(f'"variavel" com o conteúdo "{variavel}" NÃO é uma string')


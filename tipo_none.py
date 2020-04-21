"""
O tipo de dado None em Python, representa o Tipo sem Tipo (indefinido).
Pode ser conhecido também como um tipo vazio. Mas é recomendado usar a expressão "Tipo vazio" ou "Tipo indefinido"

A primeira letra deve ser sempre maiúscula:
Certo: None
Errado: none

Quando podemos utilizar?

-  Podemos utilizar quando queremos iniciarlizar uma variável e inicializa-la com um tipo sem tipo, 
   antes de recebermos algum valor que represente um tipo normal.

Observação:
O tipo None em Python é sempre considerado como False. Podemos usar essa informação por exemplo para realizar 
determinada ação caso seu valor seja None (não definido)   
"""

numeros = None
print(numeros)
print(type(numeros))  # Resultado: NoneType / None

numeros = (1, 2, 3, 55, 10.5)
print(numeros)
print(type(numeros))


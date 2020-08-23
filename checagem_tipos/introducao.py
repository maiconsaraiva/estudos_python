"""
Checagem de Tipos em Python

Como já sabemos, o Python é uma linguagem de programação de tipagem dinâmica forte.

Na evolução das versões do python, ele vem recebendo novos recursos que ajudam em novas abordagens para a tipagem de
dados. São abordagens mais modernas em relação ao tipo e uso desses dados.

Nas linguagens que usam a abordagem de tipagem estática, o erro de tipos é detectado já na compilação.
Outra cosia das linguagens de tipagem estática, é que, uma vez que uma variável é inicializada com um determinado tipo,
não é possível mais modificar o tipo depois de inicializada.

A PEP 484 sugeriu a implementação dos Typ Hints (Dicas de Tipos). Existem ainda outras bibliotecas que oferecem
a checagem da tipagem.

Nesta seção vamos abordar exemplos do uso das novas abordagens, fazendo a tipagem explícita dos dados.
"""

# Tipagem Dinâmica (implícita)
inteiro = 10
print(type(inteiro))  # <class 'int'>

# Dinamicamente atribuimos outro valor de outro tipo à mesma variável inteiro.
# Desta forma o interpretador do Python faz a checagem de tipo somente quando eu executar o código.
inteiro = 'teste'
print(type(inteiro))  # <class 'str'>

# Embora esse dinamismo nos dê maior flexibilidade e velocidade na hora de codificar. É passível de erros, uma vez que
# podemos por exemplo, passar uma variável do tipo inteiro como argumento de uma função que na verdade esperava um tipo
# string, gerando um erro que só é reconhecido quando o código é executado.

"""
Conjuntos (set)
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoriza dos conjuntos da matemática.

- No Python, os conjuntos são chamados de "sets"
- Dito isso, da mesma forma que na matemática:
  - Sets (conjuntos) não possuem valores duplicados;
  - Sets (conjuntos) não possuem valores ordenados;
  - Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação
deles. Quando não precisamos nos preocupar com chaves, valores e itens duplicados.

Os sets (conjuntos) são referenciados em Python com chaves: {}

Dferença entre conjuntos (sets)  e Mapas (dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

Assim como lista, tupla e dicionários, os conjuntos (sets) também aceitam qualquer tipo de dados.

"""

# Definindo um conjunto

# Forma 1

conjunto = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos
print(conjunto)  # Resultado: {1, 2, 3, 4, 5, 6, 7}. Repare que os números repetidos foram ignorados, e não geraram erro
print(type(conjunto))  # Resultado: set


# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erros, e não
# fará parte do conjunto.

# Forma 2:
conjunto2 = {1, 2, 3, 4, 5, 5}
print(conjunto2)  # Resultado: {1, 2, 3, 4, 5}
print(type(conjunto2))  # Resultado: set


# Podemos converter vários tipos de dados em um set

# Lista
lista = ['A', 'B', 'C', 'D']
s = set(lista)
print(s)  # Resultado: {'D', 'C', 'B', 'A'}
print(type(s))  # Resultado: set

# Tupla
tupla = set( ('A', 'B', 'C', 'D') )
print(tupla)  # Resultado: {'B', 'A', 'C', 'D'}

# String
set_letras = set('Maicon Saraiva')  # Resultado: {'r', 'v', 'i', 'o', ' ', 'S', 'c', 'n', 'a', 'M'}
print(set_letras)

# Verificando se algum valor está dentro do conjunto
print('n' in set_letras)  # Resultado: True
print('j' in set_letras)  # Resultado: False


# Importante lembrar que: Além de não termos valores duplicados, não temos ordem. Mesmo que você crie um dicionário
# e imprime logo em seguida, a ordem não virá como você definiu e nem por ordem alfabética
s = set( {99, 1, 5, 50, 3, 4, 5, 8, 10, 9} )
print(s)  # Resultado; {1, 3, 99, 5, 4, 8, 9, 10, 50}


# Iterando em um conjunto
for n in s:
    print(n)

"""
Usos interessantes para conjuntos (sets):

- Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes informam
manualmente a cidade de onde vieram.

Nós adicionamos cada cidade um uma lista Python, j[a que em uma lista podemos adicionar novos elementos e ter
repetição.

Supondo que 10 pessoas vieram de uma mesma cidade, na lista eu terei a cidade repetida 10 vezes.
Se eu quiser saber a quantidade total distinta de cidades, eu posso jogar o conteúdo dessa lista em um conjunto.
"""

cidades = ['Caculé', 'Licínio de Almeida', 'Jacaraci', 'Urandi', 'Licínio de Almeida', 'Caculé', 'Caculé', 'Mortugaba']

print(f'Total de respostas: {len(cidades)}')   # Resultado: 8
print(f'Total de cidades: {len(set(cidades))}')  # Resultado: 5 (removeu as repetições)


# Adicionando elementos em um conjunto
s = {1, 2, 3, 3, 4}

s.add(5)
s.add(5)  # Elemento duplicado será simplesmente ignorado, sem gerar nenhuma exception
print(s)

# Removendo elementos
# Forma 1
s.remove(1)
print(s)

# s.remove(10)  # Se tentarmos remover um elemento que não existe, será gerada uma exception KeyError

# Forma 2
s.discard(2)
print(s)

s.discard(10)  # Diferente do .remove(), o discard não gera exception caso o elemento não exista


# Copiando um conjunto para outro
s = set({'A', 'B', 'C', 'D'})
novo = s.copy()  # Deepcopy
novo.remove('A')
print(s)
print(novo)

# Shallow copy (apenas apontamento por referência)
s = set({'A', 'B', 'C', 'D'})
novo = s  # Shallowcopy
novo.remove('A')  # Ao remover o elemento de "novo" ele também foi removido de "s"
print(s)
print(novo)

# Removendo todos os elementos de um conjunto
novo.clear()
print(novo)

"""
Métodos Matemáticos de Conjuntos
"""

# Imagine que temos 2 elementos: Um contendo estudantes de curso de Python, e outros contendo os estudantes de Java
estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Veja que alguns alunos que estudam Python, também estudam Java

# PROBLEMA 1: Precisamos gerar um conjunto com nomes de destudantes únicos:

# Forma 1: (Recomendado, pois fica mais claro o que está acontecendo)
estudantes_unicos1 = estudantes_python.union(estudantes_java)
print(estudantes_unicos1)

# Forma 2: Utilizando o caractere pipe: |  ( Obs: Conjuntos não aceitam concatenação "+" )
estudantes_unicos2 = estudantes_python | estudantes_java
print(estudantes_unicos2)


# PROBLEMA2: Intersecção (estudates que estudam tanto Python quanto Java)
# Forma 1: Usando o método .intersection()
estudantes_ambos = estudantes_python.intersection(estudantes_java)
print(estudantes_ambos)  # Resultado: {'Patrícia', 'Julia'}  (as únicas que estudam os dois cursos)

# Forma 2: Usando o &
estudantes_ambos2 = estudantes_python & estudantes_java
print(estudantes_ambos2)  # Resultado: {'Patrícia', 'Julia'}

# PROBLEMA 3: Gerar um conjunto de estudantes que não estão no outro curso

estudantes_somente_python = estudantes_python.difference(estudantes_java)
print(estudantes_somente_python)  # Resultado: {'Ellen', 'Pedro', 'Guilherme', 'Marcos'}

estudantes_somente_java = estudantes_java.difference(estudantes_python)
print(estudantes_somente_java)  # Resultado: {'Gustavo', 'Fernando', 'Ana'}


# Soma, Valor Mínimo, Valor Máximo, Tamanho.
# Se os valores forem reais ou inteiros, os métodos sum(), min(), max() podem ser usados normalmente em conjuntos.
s = {1, 2, 3, 4, 5}
print(sum(s))  # Resultado: 15
print(min(s))  # Resultado: 1
print(max(s))  # Resultado: 5
print(len(s))  # Resultado: 5 (quantidade de elementos no conjunto)

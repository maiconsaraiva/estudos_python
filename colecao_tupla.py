"""
Tupla (tuple)
Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças:
  - As tuplas são representadas visualmente por parenteses (). É uma diferença visual
  - As tuplas são imutáveis. Ou seja, é como se a tupla fosse uma constante de uma lista.
    Uma vez que uma tupla é criada, não é possível modificar seu conteúdo, apenas trabalhar em cima deles.

    Se você quiser alterar uma tupla, você vai na verdade criar uma nova instância da variável, sobrepondo a original.

    Método para adição, remoção, etc. não existem para tupla, já que elas são imutáveis.

    Já outros métodos como: sum(tuple), max(tuple), max(tuple), len(tuple), etc. funcionam normalmente.

Todo o resto é semelhante à uma lista.

Dicas na utilização de tuplas:
  - Devemos utilizar tuplas sempre que não precisarmos ou não queremos modificar os dados contidos em uma coleção
  - Tuplas são mais rápidas do que listas (tem um melhor desempenho). O fato de serem imutáveis proporciona isso.
  - Trabalhar com elementos imutáveis, traz segurança para o código
"""

# CUIDADO 1: As tuplas são representadas por parenteses, mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

# É possível criar uma tupla sem necessariamente precisar usar os parenteses.
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))  # Resultado: tuple

# CUIDADO 2: Criação de tupla com apenas 1 elemento.

# No exemplo abaixo será criado na verdade uma variável do tipo "int" e não "tuple"
tupla3 = (4)
print(tupla3)
print(type(tupla3))  # Resultado: int

# No exemplo abaixo criamos um tupla com somente 1 elemento mas do jeito certo
tupla4 = (4,)  # A vírgula determina que o objeto criado será uma tupla
print(tupla4)
print(type(tupla4))  # Resultado: tuple

# Outro exemplo, sem precisar usar o parenteses
tupla5 = 4,  # Mesmo sem usar parenteses, a vírgula é suficiente para determinar que o objeto criado será uma tupla
print(tupla5)
print(type(tupla5))  # Resultado: tuple

# CONCLUSÃO: Podemos concluir que na definição de uma variável do tipo "tuple", apenas a vírgula é realmente necessária


"""
Gerando tupla com range
"""

tupla = tuple(range(0, 10))
print(tupla)

tupla = tuple(range(0, 51, 10))
print(tupla)  # Resultado: (0, 10, 20, 30, 40, 50)

"""
Concatenação de tuplas
"""
tupla1 = 1, 2, 3, 4
tupla2 = 5, 6, 7, 8
tupla3 = tupla1 + tupla2
print(tupla3)  # Resultado: (1, 2, 3, 4, 5, 6, 7, 8)


"""
Se você quiser alterar uma tupla, você vai na verdade criar uma nova instância da variável, sobrepondo a original.
Ou seja, a tupla é imutável, mas não é uma constante.
"""
tupla1 = 1, 2, 3, 4
tupla2 = 5, 6, 7, 8
tupla1 = tupla1 + tupla2
print(tupla1)  # Resultado: (1, 2, 3, 4, 5, 6, 7, 8)

"""
Iterando sobre uma tupla.
Fazemos da mesma forma que uma lista.
"""
tupla = ('A', 'B', 'C', 'D', 10, 9, 8, 1, 2, 3)

for n in tupla:
    print(n)

# com chave/valor
for i, n in enumerate(tupla):
    print(f'Índice: {i}. Valor: {n}')

# Contado elementos dentro de uma tupla
tupla = ('A', 'A', 'B', 'B', 'C', 'D')
print(tupla.count('A'))  # Quantos 'A' eu tenho na tupla? Resultado: 2
print(tupla.count('B'))  # Quantos 'B' eu tenho na tupla? Resultado: 2
print(tupla.count('D'))  # Quantos 'D' eu tenho na tupla? Resultado: 1

# Exemplo de um uso viável e recomendável de Tuple, contendo os meses do ano, que são imutáveis.
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# Acessando o mẽs específico
print(meses[5-1])  # Acessa o mês 5 "Maio" na lista. Obs: Lembrando que o índice começa em "0", por isso usei o 5-1

# Verificando qual o índice de um dos meses:
print(meses.index('Julho'))  # Resultado: 6

# Slice de Tupla: Também funciona como em uma lista
# tupla[inicio:fim:passos]

# Imprimindo os meses à partir de Maio
print(meses[5-1::])

"""
Copiando tuplas

Diferente da lista, na tupla não existe o "Shallow Copy". 
Exemplo:
  tupla = (1, 2, 3)
  nova = tupla
No exemplo acima, "nova" será uma cópia isolada e diferente de "tupla". As alterações (ou melhor dizendo, sobreposições)
feitas em "nova" não serão refletidas em "tupla" (como ocorreria se fossem uma lista).
"""
# Exemplo
tupla = (1, 2, 3)
nova = tupla
nova = nova + (4, 5, 6)
print(nova)  # Resultado: (1, 2, 3, 4, 5, 6
print(tupla)  # Resultado: (1, 2, 3)


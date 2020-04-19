"""
Listas

Listas em Python funcionam como vetores/arrays, ou como são comumente chamadas em outras linguagens, arrays.
A diferença é que essas listas são muito mais DINÂMICAS e também podem conter QUALQUER tipo de dados.

- Dinâmico:
  - Em algumas linguagens, como C, Java ou Delphi, possuem tamanho e tipo de dados fixos.
    No Delphi por exemplo, ao declarar uma variável do tipo array, é preciso fixar o tamanho dela.
    Até existe a possibilidade de de aumentar o tamanho depois de criada, mas ai você precisa usar comandos específicos
    para extender esse tamanho, enquanto que no Python basta simplesmente você atribuir um novo tipo de dado em uma nova
    posição, que ele irá aceitar perfeitamente. O PHP funciona de forma semelhante em seu tipo array().


- Qualquer Tipo de Dado:
  - Você pode criar uma lista em Python contendo Strings, Inteiros, Floats, Booleanos, ou ainda Classes inteiras.
  - É possível também criar uma lista mista. Ex: Na posição 1 contém uma string, na 2 um Inteiro, na 3 uma classe,
    e por ai vai.

- As listas em Python são representadas por colchetes.

ToDo: Depois que eu dei o sort() em uma lista, é possível reverter ao estado original?
ToDo: Como contar de forma geral quantos elementos uma lista tem?
"""

# Exibindo o type. O resultado será "list"
type([])

# Lista com valores inteiros
lista_inteiros = [1, 99, 27, 50, 200, 500, 2, 3, 5, 1, 99, 10, 9, 8]

# Lista com strings
lista_strings = ['Maicon', 'Jecson', "Saraiva", '''De''', """Oliveira"""]

# Criando uma lista contendo todas as palavras de uma string ("quebrando" uma string em uma lista
lista_maicon = 'Maicon Saraiva de Oliveira'.split()
print(lista_maicon)  # Resultado: ['Maicon', 'Saraiva', 'de', 'Oliveira']
# Obs: Por padrão, o split() considera o ' ' (espaço) como separador/delimitador da string.

# Usando outro separador/delimitador
colunas_cliente = 'CODIGO;NOME;FANTASIA;CPF;RG;ENDERECO;EMAIL;TELEFONE'
colunas_cliente = colunas_cliente.split(';')
print(colunas_cliente)  # Resultado: ['CODIGO', 'NOME', 'FANTASIA', 'CPF', 'RG', 'ENDERECO', 'EMAIL', 'TELEFONE']

"""
Contrário ao split(), temos o join(), que junta os elementos de uma lista em uma só string, separando por um caractere
específico.
"""
string_colunas = ','.join(colunas_cliente)  # Cria a string, mas desta vez usa a vírgula para separar o conteúdo
print(string_colunas)  # Resultado: CODIGO,NOME,FANTASIA,CPF,RG,ENDERECO,EMAIL,TELEFONE


# Lista com valores booleanos
lista_booleanos = [True, True, False, True, False, False, True]

# Lista vazia
lista_vazia = []

# Lista à partir de um range (visto na aula sobre ranges)
lista_range = list(range(1, 11))  # Resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lista com varios tipos de dados
lista_mista = [1, 5, 20, ['A', 'B'], 'Ma', 'ria', True, False, 5.40, 9.99]

# Lista criada contendo todos os caracteres de uma string
lista_caracteres = list('Maicon Saraiva')
print(lista_caracteres)  # Resultado: ['M', 'a', 'i', 'c', 'o', 'n', ' ', 'S', 'a', 'r', 'a', 'i', 'v', 'a']

# Criando uma lista dentro de uma lista
empresa = ['Sismais Tecnologia', ['Endereço 1', 'Endereço 2', 'Endereço 3']]
print(empresa)

# Podemos facilmente verificar se um determinado valor está dentro de uma lista
# Numerica:
if 27 in lista_inteiros:
    print('O número 27 está sim na lista "lista_inteiros" ')
else:
    print('O número 27 NÃO está na lista')

# String
nome = "Maicon"
if nome in lista_strings:
    print(f'O nome "{nome}" está presente na lista "lista_strings" ')
else:
    print(f'O nome "{nome}" NÃO está presente na lista "lista_strings" ')

# Ordenando uma lista. Note que lá em cima a lista "lista_inteiros" não está ordenada
lista_inteiros_ordenada = lista_inteiros
lista_inteiros_ordenada.sort()
print(lista_inteiros_ordenada)

"""
Invertendo a ordem de uma lista
Obs: O "reverse()" não necessáriamente coloca os dados em ordem decrescente, ele apenas inverte a ordem dos elementos.
"""
# Altera a lista revertendo a ordem dos elementos (neste caso, colocando em ordem descrescente)
lista_inteiros.reverse()

# Invertendo a ordem de uma lista mas sem alterar a variável
print(lista_inteiros[::-1])  # Imprime a lista em ordem reversa, mas não altera a ordem original

# Podemos contar o total de elementos em uma lista
print('==== Contagem de elementos da lista "len()":')
print(len(lista_inteiros))  # Resultado: 14

# Podemos facilmente contar o número de ocorrências de um valor em uma lista (o famoso: count)
print(lista_inteiros.count(1))  # Conta quantos elementos com o número "1" a lista contém. Resultado: 2
print(lista_caracteres.count('a'))  # Conta quantas letras 'a' a lista tem. Resultado: 4

"""
Para adicionar elementos em uma lista, usamos a função append() ou insert()
Obs: Com o append conseguimos adicionar apenas um elemento por vez. Para adicionar vários elementos, usamos o "extend"
"""
lista_strings.append('Teste Append')  # Adiciona o novo elemento no final da lista
print(lista_strings)

# o insert() é usado para inserir um novo elemento em uma posição específica da lista
print('========= Exemplo com insert()')
lista_nomes = ['Maria', 'João', 'José']
lista_nomes.insert(1, 'Joaquim')  # Insere o nome Joaquim na posição 1 da lista (ou seja, entre Maria e João)
print(lista_nomes)

# Adicionando vários elementos
lista_strings.extend(['Teste extend 1', 'Teste extend 2', 'Teste extend 3', 59.90, True, False])
print(lista_strings)
print(lista_strings[9])  # Resultado: 59.90
print(type(lista_strings[9]))  # Resultado: float


"""
Concatenando duas listas (usando o método extend)

Há duas formas:
  - Com o extend()
  - ou concatenação normal: lista3 = lista1 + lista2 
"""


lista_concatenada = lista_caracteres.copy()
lista_concatenada.extend(lista_inteiros)
print('====== Lista concatenada:')
print(lista_concatenada)

print('====== Lista concatenada 2:')
lista_concatenada2 = lista_caracteres + lista_inteiros + [lista_booleanos]
print(lista_concatenada2)

# Repetir/multiplicar elementos de uma lista
lista = [1, 2, 3] * 3
print(lista)  # Resultado: [1, 2, 3, 1, 2, 3, 1, 2, 3]
# É o mesmo que:
lista = [1, 2, 3]
lista = lista * 3
print(lista)  # Resultado: [1, 2, 3, 1, 2, 3, 1, 2, 3]

"""
Removendo Elementos de uma Lista
"""
# Remover o último elemento de uma lista
lista_nomes.pop()  # Remove o 'José'
# É o mesmo que usar:
lista_nomes.pop(len(lista_nomes)-1)  # Remove 'João'

# O pop() remove o último elemento, mas também o retorna na função.
elemento_removido = lista_nomes.pop()  # Remove 'Joaquim'
print(elemento_removido)  # Resultado: 'Joaquim'
print(lista_nomes)  # Restou somente 'Maria' na lista

# Remover elemento específico do elemento
elemento_removido = lista_strings.pop(9)  # Remove o "59.90" da lista.
print(elemento_removido)

# Remover todos os elementos (zerar a lista)
lista_nomes.clear()
print(lista_nomes)  # Resultado: []

"""

Iterando sobre listas (for / while). Já foram vistos na aula de fore while, mas segue reforço:

print('====== Iterando em uma lista')
for i, elemento in enumerate(lista_mista):
    print(f'Item {i} - Elemento: {elemento}')

# Usando o While
carrinho = []
produto = ''
while produto != 'sair':
    print('Adicione um produto na lista, ou digite "sair" para sair:')
    produto = input()
    if produto == 'sair':
        break
    else:
        carrinho.append(produto)

print('Produtos no Carrinho: ')
for i, produto in enumerate(carrinho):
    print(f'Item {i} - {produto}')
else:
    print('Carrinho vazio!')
    
"""


# Pegar o elemento X da lista, iniciando do final para o início
cores = ['A', 'B', 'C', 'D']
print(cores[-1])  # Resultado: 'D' (pega o 1° elemento da lista, iniciando do final para o início)
print(cores[-3])  # Resultado: 'B'

# Obter o índice do elemento em uma lista, pelo seu valor
# Obs: Caso não tenha o elemento na lista, será apresentado um erro.
print(lista_strings.index('Saraiva'))  # Resultado: 2

# Também podemos pegar o índice do elemento, mas iniciando a busca à partir do elemento X
lista_caracteres = list('Maicon Saraiva')
print(lista_caracteres.index('a', 9))  # Resultado: 10 (Ignora o 1° e o 2° 'a', e pega a letra entre r e i )
print(lista_caracteres.index('a', 7, 10))  # Resultado: 8 (Busca o ínice da letra "a", mas dentro do intervalo entre 7 e 10)

# Trabalhando com Slice de Lista

lista = ['A', 'B', 'C', 'D']
# Pega todos os elementos da lista, à partir do indice 1
print(lista[1:])  # Resultado: ['B', 'C', 'D'].
# Pega os elementos da lista começando do início e indo até o indice 2 (3-1)
print(lista[:3])  # Resultado: ['A', 'B', 'C']
# Pegando do índice 1 até o 2 (3-1)
print(lista[1:3])  # Resultado: ['B', 'C']
# Invertendo a lista
print(lista[::-1])  # Resultado: ['D', 'C', 'B', 'A']
# Pegando o índice na posição 1, na ordem invertida.
print(lista[::-1][1])  # Resultado: C

# Trabalhando com os "passos" (intervalo de avanço) nas listas.

# Avança toda a lista, pulando de 2 em 2
print(lista[::2])  # Resultado: ['A', 'C']

# Começa na posição 1, e vai até o final, pulando de 2 em 2
print(lista[1::2])  # Resultado: ['B', 'D']

# Percorre a lista de trás pra frente, pulando de 2 em 2
print(lista[::-2])  # Resultado: ['D', 'B']


# Exemplo de atribuição e inversão de valores em elementos de uma lista
nomes = ['Maicon', 'Saraiva']
# O valor da posição "0" vai receber o que está na posição 1, e o da 1 vai receber o que está na posição 0
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)  # Resultado: ['Saraiva', 'Maicon']  Obs: Diferente dos exemplos anterior, aqui a lista foi realmente alterada.

# Se for pra fazer essa inversão na lista toda, o método "reverse" também resolve.
nomes = ['Maicon', 'Saraiva']
nomes.reverse()
print(nomes)  # Resultado: ['Saraiva', 'Maicon']

nomes = ['Maicon', 'Jecson', 'Saraiva', 'De', 'Oliveira']
nomes.reverse()
print(nomes)  # Resultado: ['Oliveira', 'De', 'Saraiva', 'Jecson', 'Maicon']

"""
Operações numericas envolvendo listas

Soma, Valor Mínimo, Valor Máximo, Tamanho, etc.
"""

lista = [1, 2, 3, 4, 5, 6]

# Soma
print(sum(lista))  # Resultado: 21 ( 1 + 2 + 3 + 4 + 5 + 6 )
# Valor máximo
print(max(lista))  # Resultado: 6
# Valor mínimo
print(min(lista))  # Resultado: 1
# Tamanho (quantidade de elementos)
print(len(lista))  # Resultado: 6


lista = ['A', 'B', 'C', 'D', 'E', 'F']

# Soma
# print(sum(lista))  # O sum não pode ser feito com valores não numericos
# Valor máximo
print(max(lista))  # Resultado: F
# Valor mínimo
print(min(lista))  # Resultado: A
# Tamanho (quantidade de elementos)
print(len(lista))  # Resultado: 6

"""
Transformar uma Lista em Tupla
"""

tupla = tuple(lista)

# A diferença visível entre tupla e lista, é que a lista fica dentro de colchetes, e a tupla dentro de parenteses.
print(tupla)  # Resultado: ('A', 'B', 'C', 'D', 'E', 'F')
print(type(tupla))  # Resultado: tuple


"""
Desempacotamento de lista

# Obs: No desempacotamento de lista, a quantidade de variáveis tem que ter exatamente a mesma quantidade 
       de elementos da lista.
Exemplo:
lista = [1, 2, 3, 4]
num1, num2, num3 = lista  # Esse código irá gerar uma exception do tipo "ValueError"
"""
# Exemplo correto
lista = [155, 190, 255.0]
num1, num2, num3 = lista
print(f'{num1}\n{num2}\n{num3}')

"""
Cópias de lista


Shallow Copy (Cópia rasa)
IMPORTANTE: É preciso ter cuidado ao criar uma nova lista baseada em outra. 
Se usar simplesmente: 
  lista2 = lista1
Na verdade, estaremos criando cópia que aponta par aa original, como se fosse um apontamento por referência(ponteiro)
Ou seja, todas as alterações feitas em "lista2", estarão sendo feitas automaticamente em "lista1".
No Python, esse tipo de mecanismo é chamado de "Shallow Copy", ou cópia rasa.

Maneiras recomendada de se fazer (caso queira criar uma cópia distinta):

DeepCopy (ou cópia profunda)

    lista_caracteres2 = lista_caracteres.copy()  # Disponível à partir da versão 3.3 do Python
  

    Ao utilizar o "lista.copy()" criamos duas cópias totalmente independentes, ou seja, modificando uma não afeta a outra.
    Em Python isso é chamado de DeepCopy, ou cópia profunda
   
    OBS: Se a lista contiver objetos/classes e você quiser copiá-los também, use o deepcopy da biblioteca "copy"
      import copy
      lista2 = copy.deepcopy(lista1)
      
Existem ainda outras maneiras de se fazer:
  https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
      
"""





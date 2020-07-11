"""
Erros mais comuns em Python

Listagem das expcetions existentes no core do Python:
https://docs.python.org/3.8/library/exceptions.html

Obs:
- Exceptions e Erros são sinônimos na programação.
- Importante ler e prestar atenção na saída de erro, ou seja, compreender o que o erro quer dizer.
"""

"""
SyntaxError -> Ocorre quando o python não reconhece o que foi digitado como parte da linguagem.
# Ex 1
def funcao:  # SyntaxError: invalid syntax (pois funções tem que ter parenteses)
    print('teste')
# Ex 2 (não é possível atribui como variável uma palavra reservada)
None = 1  # SyntaxError: cannot assign to None
def = 'Oi' # SyntaxError: invalid syntax
list = 'Oii' # (neste caso o Python até aceita, mas não é recomendado)
"""

"""
NameError -> Ocorre quando uma palavra não é reconhecida como variável, função, classe ou qualquer outra coisa da
linguagem.

# Ex 1
print(nome)  # NameError: name 'nome' is not defined
# Ex 4
funcao_naocriada('teste')  # NameError: name 'funcao_naocriada' is not defined

# Ex 3
a = 2
if a > 5:
    msg = 'É maior do que 5!'
print(msg) # NameError: name 'msg' is not defined (como não entramos na condição, a variável msg não foi criada)

"""

"""
TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo incompatível

# Ex 1
len(1)  # TypeError: object of type 'int' has no len()
# Ex 2
sorted(2)  # TypeError: 'int' object is not iterable
# Ex 3
a = 'Maicon' + ['Saraiva']  # TypeError: can only concatenate str (not "list") to str
"""

"""
IndexError -> Ocorre quando tentamos acessar um elemento pelo índice, mas que o índice não exista
# Ex 1
lista = ['Maicon']
lista[0]  # Ok
lista[1]  # IndexError: list index out of range

# Ex 2
nome = 'Maicon'
letra = nome[6] # IndexError: string index out of range

# Ex 3
lista = ['Maicon', 'Sarava', 'De', 'Oliveira']
lista.pop(3)
lista.pop(3)  # IndexError: pop index out of range  (o elemento já foi excluído, então não existe mais a posição 3
"""

"""
KeyError -> Semelhante ao IndexError, mas é valido para Dicionários. Ou seja, ocorre quando tentamos acessar uma chave
que não existe.
# Ex 1
lista = {'a': 1, 'b': 10, 'd': 20}
lista['d']  # Ok
lista['c']  # KeyError: 'c'  (a chave "c" não existe)
"""

"""
ValueError -> Ocorre quando uma função/operação/built-in (integrada) recebe um argumento com tipo certo, mas valor
errado.
# Ex 1
lista = ['Maicon', 'Sarava', 'De', 'Oliveira']
lista.index('Jecson')  # ValueError: 'Jecson' is not in list

# Ex 2
int('25.6')  # ValueError: invalid literal for int() with base 10: '25.6'
int('AB26.6')  # ValueError: invalid literal for int() with base 10: 'AB26.6'
"""

"""
AttributeError -> Ocorre quando uma variável ou objeto não tem um atributo ou função.

# Ex 1
lista = ['Maicon', 'Saraiva']
lista.sort()  # Ok

nome = 'Maicon Saraiva'
nome.sort()  # AttributeError: 'str' object has no attribute 'sort'

tupla = ('Maicon', 'Saraiva')
tupla.sort()  # AttributeError: 'tuple' object has no attribute 'sort'
"""

"""
IndentationError -> Ocorre quando não respeitamos a indentação do Python.

# Ex 1
for i in range(0,10):
print('Erro de indentação! :O')  # IndentationError: expected an indented block

# Ex 2
def minha_funcao():
print('Minha função!')  # IndentationError: expected an indented block

IMPORTANTE: Embora o padrão de indentação para o Python seja de 4 espaços, não é obrigatória essa quantidade.
  Se existir somente 1 espaço em branco, o código já irá funcionar.
  Porém, usar a indentação fora do padrão pode causar problemas, como por exemplo execução de códigos em momentos
  errados.

# Exemplo de indentação com somente um espaço, que não dá erro:
for i in range(0,10):
 print('Erro de indentação! :O')
"""




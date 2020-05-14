"""
Escopo de Variáveis

Dois casos de escopo:
1. Variáveis globais:,
  - São reconhecidas em todo o programa, ou seja seu escopo é válido em todo o programa (arquivo)
  para o arquivos.
  - Para acessar uma variável global dentro de uma função, devemos "redeclarar" ela da seguinte forma:
    global nome_da_variavel  # Ao usar o termo "global" avisamos ao Python que queremos acessa-la.

2. Variáveis locais:
  - São reconhecidas somente no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi
  declarada.

RECOMENDAÇÃO:
- Se puder evite ao máximo variáveis globais
"""

nome = 'Maicon Saraiva'  # Variável global

if nome == 'Maicon Saraiva':
    idade = 29  # Variável local (se eu tentar usar ela fora desse bloco dará erro.
    data_nascimento = '23/07/1990'  # Variável local também

print(nome)  # Imprime normalmente
print(idade)  # Gera um erro (a variável não existe). ToDo: Não está dando erro. por que?

"""  

Para declarar avariáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que, ao declararmos uma variável, nós não colocamos o tipo de
dado dela. Este tipo é inferido ao atribuirmos o valor à mesma.

Em outras linguagens como Delphi, C, etc, o tipo precisa ser informado em sua declaração. A esse tipo de abordagem
damos o nome de: Variável fortemente tipada

Exemplo em C:
int numero = 42;

Exemplo em Delphi:
var integer numero := 42;

Exemplo em Python:
numero = 42  # O Python reconhece automaticamente que esta variável é do tipo inteiro.

"""

# No Python como a tipagem é dinâmica, é possível atribuir valores de tipos diferentes em uma mesma variável.
# Exemplo:

numero = 42
numero = 'Maicon Saraiva'  # A variável "numero" recebeu uma nova atribuição e agora passa a ser uma string.


"""
Escopos de Variáveis dentro e fora da função


"""


nome = 'Maicon'  # Variável global


def diz_nome():
    nome = 'Glenda'
    return nome


print(diz_nome())  # Resultado: Glenda
print(nome)  # Resultado: Maicon

# Note que, mesmo tendo definido a variável "nome" como "Glenda" na função "diz_nome()", na última impressão,
# ainda foi impresso o nome "Maicon". Isso ocorreu por que, na verdade, a variável "nome" dentro da função é uma
# variável local, e ela não afetou em nada a variável global (que está fora do escopo da função), e ainda não foi
# modificada. Além disso a variável "nome" é uma variável local da função e não pode ser acessada de fora dela.


# Acessando uma variável global dentro de uma função
sistema = 'Sismais ERP'


def dados_cliente():
    primeiro_nome = 'Maicon'
    sobrenome = 'Saraiva'
    global sistema
    return f'Nome: {primeiro_nome}, Sobrenome: {sobrenome}, Sistema: {sistema}'


print(dados_cliente())  # Resultado: Nome: Maicon, Sobrenome: Saraiva, Sistema: Sismais ERP


# É possível também alterar a variável global dentro da função
seu_nome = 'Não informado ainda'


def define_seu_nome():
    global seu_nome
    seu_nome = 'Maicon Saraiva'


define_seu_nome()
print(seu_nome)  # Resultado: Maicon Saraiva





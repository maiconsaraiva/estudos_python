"""
Escopo de Variáveis

Dois casos de escopo:
1. Variáveis globais:,
  - São reconhecidas em todo o programa, ou seja seu escopo é válido em todo o programa (arquivo)
  para o arquivos.

2. Variáveis locais:
  - São reconhecidas somente no bloco onde foram declaradas, ou seja, seu escopo está limitado ao bloco onde foi
  declarada.
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

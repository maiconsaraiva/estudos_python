"""
Recebendo dados de usuário

Em Python, string é tudo aquilo que estiver entre:
- Aspas simples
  'Maicon Saraiva'
- Aspas duplas
  "Maicon Saraiva"
- As simples triplas
  '''Maicon Saraiva'''
- Aspas duplas triplas
"""
from datetime import datetime, date

# Exemplo de string em aspas duplas triplas: """Maicon Saraiva"""

# Entrada de dados
# print("Qual o seu nome?") (Essa pergunta pode ser feita diretamente no input)
nome = input("Qual o seu nome? ")

# print('Quantos anos você tem?')
idade = int(input("Qual a sua idade? "))  # Obs: O dado recebido em um input sempre será uma string

# Processamento
nome = nome.title()

# Saida de dados
""" 
Os dois prints abaixo são usados na versão 2.x do Python (mais antigos), 
porém até a versão atual (3.8), ainda funciona
"""
# print('Olá %s, seja bem vindo! ' % nome)
# print('Olá %s, seja bem vindo! Sua idade é %s' % (nome,idade))

"""
Versão do print criados à partir da versão 3.4/3.5 do Python
"""
# print('Olá {0}, seja bem vindo!'.format(nome))
# print('Olá {0}, seja bem vindo! Sua idade é: {1}'.format(nome, idade))

# Versão mais atual, criada a partir da versão 3.7 do Python
print(f'Olá {nome}, seja bem vindo! Você nasceu em {date.today().year - idade} e tem {idade} ano(s).' +
    f' (Python 3.7 e maior)')

""" 
Exemplo de print() mudando o kwargs "end" que determina o caractere de final de linha.
O valor default do end é "\n", e é por isso que sempre que acionamos o print('alguma_coisa') é impresso em uma nova 
linha. Para mudar isso, basta personalizar o valor de "end", como podemos ver no exemplo abaixo.
"""
print('8 ---------------------')
for letra in nome:
    print(letra, end=' ')




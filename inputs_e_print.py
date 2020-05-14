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

print(f'Olá {nome}, seja bem vindo! Você nasceu em {date.today().year - idade} e tem {idade} ano(s).')

for letra in nome:
    print(letra, end=' ')

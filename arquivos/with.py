"""
Utilizando o bloco with

O bloco with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with
"""

# Quando sairmos do with o próprio with irá fechar o arquivo
# Essa é a forma Pythonica de se trabalhar com arquivos. (sempre dentro do contexto).
with open('../_pesquisar.txt') as arquivo:
    print(arquivo.closed)  # False

# Embora a variável ainda exista, o arquivo foi fechado automaticamente.
print(arquivo.closed)  # True

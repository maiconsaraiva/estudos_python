"""
Seek e Cursor

seek() -> É utilizado para movimentar o cursor pelo arquivo. Ela recebe um parâmetro que indica onde queremos colocar
o cursor.
"""

arquivo = open('../_pesquisar.txt', encoding='UTF-8')

arquivo.read()
arquivo.seek(21)  # Posiciona o cursor
# print(arquivo.read())  # Faz a leitura à partir da posição indicada pelo seek()


# Efetuando leituras linha a linha
arquivo.seek(0)
print(arquivo.readline())  # 1
print(arquivo.readline())  # 2
print(arquivo.readline())  # 3
print(arquivo.readline())  # 5

# readlines() -> Retorna todas as linhas em uma lista (cada linha se torna um item da lista)
arquivo.seek(0)
print(len(arquivo.readlines()))  # 30

arquivo.close()

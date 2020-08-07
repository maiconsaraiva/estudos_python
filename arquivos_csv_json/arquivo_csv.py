"""
Lendo arquivo CSV

CSV - Comma Separated Values - Valores Separados por Vírgula

O Python possui um módulo builtin para ler dados de arquivos CSV.

A leitura pode ser feita de duas formas:
- reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
- DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;


# Usando o reader

from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    # Pula a primeira linha, que contém o cabeçalho
    next(leitor_csv)
    for linha in leitor_csv:
        # cada linha é uma lista contendo os elementos separados pelo Comma (ou outro separador)
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros.')


"""

# Usando o DictReader
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arquivo:
    leitor_csv = DictReader(arquivo)

    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu em {linha['País']} e mede {linha['Altura (em cm)']} centímetros.")

    # Obs: O DictReader retorna cada linha em um dicionário com chave e valor.





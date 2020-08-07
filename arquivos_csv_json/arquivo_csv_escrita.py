"""
Escrevendo em arquivo CSV.

writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
Utilizamos o método writerow para escrever cada linha. Este método recebe uma lista.
"""

from csv import writer, DictWriter

with open('filmes.csv', 'w', encoding='utf-8', newline='\n') as arquivo:
    csv = writer(arquivo)
    csv.writerow(['Título', 'Gênero', 'Duração (em minutos)'])
    csv.writerow(['Transformers 1', 'Ficção Cientifica', 140])
    csv.writerow(['Independence Day', 'Ficção Cientifica', 120])
    csv.writerow(['Rambo 4', 'Ação', 90])


# usando o WriteDict

with open('filmes2.csv', 'w', encoding='utf-8', newline='\n') as arquivo:
    csv = DictWriter(arquivo, fieldnames=['Título', 'Gênero', 'Duração (em minutos)'])
    csv.writeheader()
    csv.writerow({'Título': 'Transformers 1', 'Gênero': 'Ficção Cientifica', 'Duração (em minutos)': 140})
    csv.writerow({'Título': 'Independence Day', 'Gênero': 'Ficção Cientifica', 'Duração (em minutos)': 120})
    csv.writerow({'Título': 'Rambo 4', 'Gênero': 'Ação', 'Duração (em minutos)': 90})

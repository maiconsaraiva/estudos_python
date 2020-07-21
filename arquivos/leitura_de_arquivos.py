"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir';

open() -> Na forma mais simples de utilização, nós passamos apenas um parâmetros de entrada, que neste caso é o nome
do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper

Se o arquivo não for encontrado, é retornar o erro FileNotFoundError.

OBS:
- Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e o
  programa. Essa conexão é chamada de Streaming.
  Ao finalizar os trabalhos com o arquivo, devemos fechar essa conexão. Para isso utilizamos o close()
- Se tentarmos acessar/manipular um arquivo quando ele está fechado teremos uma exception ValueError
"""

arquivo = open('../_pesquisar.txt', encoding='UTF-8')
print(arquivo)  # <_io.TextIOWrapper name='../_pesquisar.txt' mode='r' encoding='cp1252'>
print(type(arquivo))  # <class '_io.TextIOWrapper'>

# Para ler o conteúdo do arquivo usamos a função read()
# print(arquivo.read())  # o read() percorre todo o arquivo retornando-o em uma String

# O Python utiliza um recurso para trabalhar com arquivos chamado de cursor. Esse cursor, funciona como o curso
# quando estamos escrevendo.
ret = arquivo.read()
print(type(ret))  # <class 'str'>

# quebrando o conteúdo do arquivo em uma lista de strings
print(len(ret.split('\n')))

arquivo.close()

print(arquivo.closed())  # closed() verifica se o arquivo está aberto ou fechado

"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional, o software precisa ter permissão.

Nem sempre o software vai ter permissão de leitura e/ou escrita no arquivo.
O StringIO entra para ajudar neste cenário, ele é utilizado para ler e criar arquivos em memória, como se fosse um
arquivo no disco.

"""
from io import StringIO

mensagem = 'Esta é apenas uma string normal\n'

# Podemos criar um arquivo em memória já com uma string inserida ou vazio. Depois de criado podemos ir manipulando.
arquivo = StringIO(mensagem)  # Seria o mesmo que: arquivo = open('filename.ext', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto\n')

arquivo.seek(0)
print(arquivo.read())

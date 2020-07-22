"""
Sistema de Arquivos - Manipulação

https://docs.python.org/3.8/library/os.html

"""
import os


'''
nome_arquivo = '../arquivos2/teste.txt'
diretorio = os.path.dirname(nome_arquivo)
if not os.path.exists(diretorio):
    os.mkdir(diretorio)  # É importante verificar se já não existe, pois caso exista e dente criar, dará erro.



if os.path.exists(nome_arquivo):
    with open(nome_arquivo, 'r+') as arquivo:
        arquivo = open(nome_arquivo, 'r+')
        arquivo.write(f'Escrevendo na linha: {len(arquivo.readlines())+1}\n')
        arquivo.close()

else:
    """
    A recomendação para criar arquivos no sistema operacional é usando o os.mknod()
    Obs: O mknod pode não funcionar no sistema operacional, no MacOS pode haver um erro de PermissionErros,
    por que lá no Mac esse comando precisa de poderes administrativos, e o programa python quando é executado não é
    executado com poderes administrativos.

    E no Windows o os.mknod() não funciona.

    - Ao usar o mknod, se o arquivo já existir será gerado um erro.
    """
    if os.name == 'posix':
        os.mknod(nome_arquivo)
    else:
        open(nome_arquivo, 'w').close()  # No Windows, a alternativa que temos é essa.

    with open(nome_arquivo, 'w') as arquivo:
        arquivo = open(nome_arquivo, 'w')
        arquivo.write('Primeira linha!\n')
        arquivo.close()
'''

# Renomeando e movendo um arquivo
open('teste.txt', 'w').close()

# Se o arquivo já existir é gerado um erro.
# Se tentarmos mover para um diretório que não existe, também dará erro
# O rename() serve tanto para arquivo quanto para diretórios.
# Se for um diretório e ele não estiver vazio, dará um erro OSError
os.rename('teste.txt', 'teste_renomeado.txt', )
# o replace() renomeia e/ou move, e caso o arquivo já exista, faz a substituição.
os.replace('teste_renomeado.txt', '../teste_renomeado.txt')


"""
Deletando um arquivo: os.remove(nome_arquivo)
########################################################################################
IMPORTANTE: Ao deletar um arquivo ou diretório com o Python, ele não vai para a lixeira,
é deletado definitivamente.
Se, em vez de deletar definitivamente, desejarmos enviar para a lixeira, podemos usar
uma biblioteca de terceiros, como por exemplo a send2trash:
pip install send2trash
########################################################################################

- o remove() é exclusivo para arquivos, se você tentar deletar um diretório com ele, terá o erro:
  IsADirectoryError
- Se o arquivo a ser deletado, estiver em uso, será retornado um erro;
- Caso o arquivo não exista teremos um FileNotFoundError
os.remove('../teste_renomeado.txt')
"""

"""
Deletando um diretório: os.rmdir()

- Se o diretório não existir teremos o FileNotFoundError
- Se o diretório tiver qualquer conteúdo, teremos um OSError
- Para remover um diretório e todos os subdiretórios e arquivos, temos que fazer um tratamento,
podemos fazer usando o scandir():

for arquivo in os.scandir('nome_diretorio'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# Para remover um diretório e os subdiretórios dentro dele (recursivamente), usamos o removedirs()
os.removedirs('nome_diretorio/')

- Se algum dos diretórios conter arquivos ou outros diretórios o processo para.

"""

# Enviando um arquivo para a lixeira com a biblioteca de terceiros send2trash
from send2trash import send2trash

send2trash('../teste_renomeado.txt')  # Funciona tanto para Linux, Mac e Windows
# Se o arquivo não existir teremos o OSError
# O send2trash serve tanto para arquivos, quanto para diretórios.

# Reforçando: os.remove() -> Exclui definitivamente.


"""
Trabalhando com arquivos e diretórios temporários.

A maioria dos sistemas operacionais tem diretórios temporários, que geralmente tem permissão livre e podemos
utilizar para gravar arquivos temporários.
Para isso fazemos uso do módulo tempfile
"""
import os
import tempfile


# obtendo a pasta raiz temporária
print(tempfile.gettempdir())


with tempfile.TemporaryDirectory() as tmpdir:
    print(f'Criando arquivo no diretório temporário: {tmpdir}')
    """ Usando o contexto de with abaixo, após sair, o diretório temporário, bem como os arquivos criados dentro dele,
    serão excluídos automaticamente. """
    with open(os.path.join(tmpdir, 'arquivo_temporário.txt'), 'w') as tmpfile:
        tmpfile.write('Teste')
    # input() só pro sistema ficar aguardando a gente, para sabermos o nome do diretório temporário e verificar se o
    # arquivo existe, pois, após sair do with o arquivo e o diretório serão excluidos automaticamente.
    input()

# Além do tempfile.TemporaryDirectory, temos também o tempfile.TemporaryFile() e o tempfile.NamedTemporaryFile,
# porém a escrita neles é um pouco diferente pois, temos que escrever em formato binário
# O TemporaryFile() funciona no Windows
with tempfile.TemporaryFile() as tmp:
    print(f'Escrevendo em arquivo temporário: {tmp.name}')
    tmp.write(b'Teste de Escrita em formato binario!')
    tmp.seek(0)
    print(tmp.read())
    # input()

# Obs: podemos usar o TemporaryFile() tanto dentro de um contexto (que é excluido automaticamente ao final),
# quanto fora, quando não queremos excluir o arquivo ao final. Ou queremos excluir manualmente depois.

# Usando o NamedTempFile. Para este não usamos o contexto with
# IMPORTANTE: Como a própria documentação diz, se, na criação do arquivo, o kwargs "delete" for igual a True (padrão),
# então após o close() o arquivo será deletado automáticamente.
tmpfile = tempfile.NamedTemporaryFile(delete=True)
print(f'Usando o tempfile.NamedTemporaryFile(): {tmpfile.name}')
tmpfile.write(b'Ola Mundo!')  # Formato binário
tmpfile.seek(0)
print(tmpfile.read())
input()
tmpfile.close()


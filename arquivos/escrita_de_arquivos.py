"""
Escrever em Arquivo

- Ao abrir um arquivo para leitura, não podemos efetuar a leitura dele, apenas escrever.
  Da mesma forma, se abrirmos um arquivo para escrita, não podemos ler ele, apenas efetuar a escrita.
- Passamos o parâmetro de escrita no open()

- Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir ele será criado, e se já existir,
todo o conteúdo anterior será sobreposto.
"""

# Abre o arquivo em modo "w" (substitui o conteúdo, caso o arquivo já exista)
with open('novo_arquivo.txt', mode='w', encoding='UTF-8') as arquivo:
    # Escrevendo da forma abaixo, vamos sobrescrever o arquivo, caso ele já exista. É preciso ter cuidado.
    # A função write() recebe string com o conteúdo que queremos gravar no arquivo.
    arquivo.write('Escrevendo no arquivo!\n')
    arquivo.write('Escrevendo uma outra linha!\n')

# Abrindo o arquivo no modo "a" append (adiciona ao final, caso o arquivo já exista)
with open('novo_arquivo.txt', mode='a') as arquivo:
    arquivo.write('Terceira linha!\n')
    arquivo.seek(0)
    arquivo.write('Este conteúdo, será adicionado na primeira linha. Pois usamos o seek(0)\n')


# O mode "+" abre o arquivo para o modo de atualização (leitura e escrita)
# O '+' deve ser usado combinado com outros modos
with open('novo_arquivo.txt', mode='r+') as arquivo:
    arquivo.write('Nova\n')

"""
 Tipo String (str)
 Em Python um dado é considerado String sempre que:

- Estiver entre aspas simples. Exemplos:
  'uma string', '234','23.4', 'a','True', ''
- Estiver entre aspas duplas.
  "Uma String"
- Estiver entre aspas simples triplas
  '''Uma String''', '''Outra String'''
- Estiver entre aspas duplas triplas

O mais comum é utilizar a aspas simples: 'Minha String', e em segundo lugar, aspas duplas: "Minha String"
"""
from datetime import datetime, date

# Exemplo com aspas duplas triplas: """Minha String"""

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))
print(nome)
print(f'type from str "nome": {type(nome)}')
print(f'dir from var "nome":\n {dir(nome)}')
print(f'help from nome.upper:')
print(help(nome.upper))

nome = 'Angelina\nJolie'  # Quebra de linha (reconhecida no Shell do Python
print(nome)
"""
 split() quebra a string em uma list de strings.
 Resultado: ['Angelina', 'Jolie']
 Obs: Por padrão ele quebra por espaço
"""
lista_nome = nome.split()
print(lista_nome)
print(f'tipo de variável de "lista_nome": {type(lista_nome)}')

# Pegar parte do conteúdo de uma string (Slice de String).
nome = 'Maicon Saraiva'
# Obs: Nesse método, ele traz os caracteres da posição X até a posição Y-(menos)1. Ex: nome[0:4] vai pegar da 0 à 3.
print(nome[0:4])  # Vai retornar: "Maic". Ou seja: traga-me os caracteres da posição 0, até a 3
print(nome[4:6])  # Retorno: "on"
print(nome[7:14])  # Retorno: "Saraiva". Ou seja: traga-me os caracteres da posição 7 até a 13
print(nome[7::])  # Retorno: "Saraiva". Ou seja: traga-me os caracteres da posição 7 até a última posição
print(nome[7])  # Retorno: "S". Ou seja: traga-me o caractere que está na posição 7 da string
print(nome[0], nome[7])  # Retorno: "M S". Ou seja: traga-me o caractere da posição 0, em um join, traga o da posição 7

"""
 Inversão da String
[::-1]  -> Comece do primeiro elemento, vá até o último elemento, e inverta tudo
"""
print(nome[::-1])  # Retorno: aviaraS nociaM (Método Pythônico)

# Pegar palavra específica após um split
print(nome.split()[0])  # Resultado: "Maicon"
print(nome.split()[1])  # Resultado: "Saraiva"

# Pegar somente primeira palavra e última palavra de uma string.
nome = 'Maicon Jecson Saraiva de Oliveira'
print(f'Seu primeiro e último nome: {nome.split()[0]} {nome.split()[4]} ')  # Resultado: Maicon Oliveira

# Replace
print(nome.replace('o', '0'))  # Substitui a letra "o" (mínuscula) por "0". Resultado: Maic0n Jecs0n Saraiva de Oliveira

# Concatenação de Strings
nome = 'Maicon' + ' Saraiva'  # Exemplo de concatenação clássico

# No Python é possível repetir o valor de uma string simplesmente multiplicando a variável pelo valor desejado.
# Funciona como se fosse um "for" automático. Exemplo:
nome = 'Maicon'
nome = nome * 3
print(nome)  # Resultado: 'MaiconMaiconMaicon'

"""
Exemplo usando a multiplicação/repetição de string, imprimindo no console um emoji, usando o seu código unicode.
A tabela de emoji em Unicode, está disponível no link: https://apps.timwhitlock.info/emoji/tables/unicode
E sim, emojis podem ser impressos no Console, convertendo eles de uma maneira simples:
Exemplo:
  Emoji de sorriso aberto, Unicode: U+1F603
  Código que deve ser usado na impressão no console: \U0001F603
  (substitui-se o caractere "+" por três "0" (zeros), e adiciona-se a "\" no início)

# Obs: Não são todos os emojis que são reconhecidos pelo console.
"""

# Exemplos:
emoji_sorriso = '\U0001F603'
print(emoji_sorriso + ' Sorriso: ' + emoji_sorriso)

emoji_naovejo_macaco = '\U0001F60D'
for i in range(1, 11):
    print(emoji_naovejo_macaco * i)

"""
Concatenação de string
"""

# Com "+" (método semelhante a outras linguagens)
nome = 'Maicon'
sobrenome = 'Saraiva'
nomecompleto = nome + ' ' + sobrenome
print(nomecompleto)  # Resultado: Maicon Saraiva

# Com O .join
nome = 'Maicon'
sobrenome = 'Saraiva'
# Antes do join, o ' ' (espaço) determina que será usado entre uma string e outra.
# E dentro do join, passamos uma lista ou tupla com os elementos que queremos juntar.
nomecompleto = ' '.join([nome, sobrenome])
print(nomecompleto)  # Resultado: Maicon Saraiva

"""
Formatando dados de uma variável ao atribuir para uma string:
"""
preco = 10;
desconto = 5;  #Em percentual
preco_promocao = 9.50;

print('Preço promocional: {:.2f} (com {}% de desconto)'.format(preco_promocao, desconto))

print('{:-^48}'.format(' C L I E N T E '))
print('{:>38}'.format('Dinheiro.........: '),'{:>9.2f}'.format(2950.06))
print('{:>38}'.format('Cartão de Crédito: '),'{:>9.2f}'.format(15.556))
print('{:>38}'.format('Cartão de Débito.: '),'{:>9.2f}'.format(15.556))
print('{:>38}'.format('Cheque a Vista...: '),'{:>9.2f}'.format(15.556))
print('{:>38}'.format('Cheque a Prazo...: '),'{:>9.2f}'.format(15.556))
print('{:>38}'.format('Crediário........: '),'{:>9.2f}'.format(15.556))
print('{:>38}'.format('Boleto Bancário..: '),'{:>9.2f}'.format(15.556))


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
nome = 'Maicon'
idade = 30
print(f'Olá {nome}, seja bem vindo! Você nasceu em {date.today().year - idade} e tem {idade} ano(s).' +
    f' (Python 3.7 e maior)')

"""
Exemplo de print() mudando o kwargs "end" que determina o caractere de final de linha.
O valor default do end é "\n", e é por isso que sempre que acionamos o print('alguma_coisa') é impresso em uma nova
linha. Para mudar isso, basta personalizar o valor de "end", como podemos ver no exemplo abaixo.
"""
for letra in nome:
    print(letra, end=' ')



"""
Algumas funções para String:

- title()  (coloca as iniciais de cada palavra em maiscula)
- upper()
- lower()
- strip() (remove espaços vazio no início e no final da string, semelhante ao trim() de outras linguagens)
"""

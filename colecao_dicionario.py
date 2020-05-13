"""
Dicionários

- O que chamaos de Dicionários em Python, em algumnas linguagens são conheciados por mapas.
- São coleções do tipo Chave/Valor
- São representandos por chaves: {}
- Assim como lista e tuplas, podem ter vários tipos de dados: int, str, boolean, lista, tupla, dicionario, etc.
  Esses tipos de dados podem ser usados tanto na Chave quanto no valor
- É possível criar dicionários tridimencionaris (dicionários dentro de dicionários)
"""


# Criando um dicionário na forma mais comum
dicionario = {'Nome': 'Maicon Saraiva', 'Idade': 29, 'Sexo': 'Masculino', 'Cidade': 'Caculé'}
print(dicionario)
print(type(dicionario))  # Resultado: dict

# Outra forma de criar um dicionário (menos usada)
pessoa = dict(Nome='Maicon', Idade=29, Sexo='Masculino', Cidade='Caculé', UF='BA' )


"""
Acessando elementos
"""

# Forma 1: Acessando via chave, da mesma forma que em uma lista ou tupla
print(dicionario['Nome'])  # Resultado: 'Maicon Saraiva'

"""
Obs: Se tentarmos acessar uma chave que não existe, será gerada uma exception "KeyError"
  No exemplo abaixo, a chave não existe, então será gerada uma exception
  print(dicionario['Sobrenome'])
"""

# Usando o método "get()" não é gerada uma exception. Mesmo que a chave não existe não dá erro,
# apenas o resultado "None" é retornado.
print(dicionario.get('Sobrenome'))  # Resultado: None

# A recomendação é utilizar o get() quando queremos verificar se uma chave existe, e fazer determinada ação (sem
# precisar fazer os devidos tratamentos de uma exception)
if (dicionario.get('Sobrenome') == None):
    print('A chave "Sobrenome" NÃO existe')
else:
    print('A chave "Sobrenome" existe.')

# Obs: Como o tipo "None" é considerado sempre como False, poderiamos representar o código acima da seguinte forma:
if dicionario.get('Sobrenome'):
    print('A chave "Sobrenome" existe.')  # Neste caso o True veio pra cima
else:
    print('A chave "Sobrenome" NÃO existe')


# O método get() possui também um parâmetro para retornar um valor default, caso a chave não seja encontrada.
sobrenome = dicionario.get('Sobrenome', 'Sobrenome não encontrado')
print(sobrenome)

# Outro exemplo. Considerando que "pessoa" sempre vai ser do brasil, eu posso seguir o exemplo abaixo:
print(f'A pessoa "{pessoa["Nome"]}" mora no país: {pessoa.get("Pais", "Brasil")}')


"""
Verificando se uma chave está no dicionário
"""
print('Pais' in pessoa)  # Resultado: False

print('Idade' in pessoa)  # Resultado: True

chaveexiste = 'Nome' in dicionario
if chaveexiste:
    print(' A chave "Nome" existe sim, dentro do dicionário "dicionario" ')


# Exemplo de dicionário onde a chave é a geolocalização (valores fictícios)
locais = {
    (38.6589, 39.6917): 'Caculé',
    (38.6000, 39.5000): 'Licínio de Almeida',
}

print(locais.get((38.6000, 39.5000)))  # Resultado: Licínio de Almeida

"""
Adicionar elementos em um dicionário
"""

# Forma 1: Basta atribuir o novo elemento que ele será criado automáticamente
pessoa['cpf'] = '046.528.575-94'
pessoa['sobrenome'] = 'Saraiva'

# Forma 2: Usando o método: update()
pessoa.update({'rg': '13872329-08'})

print(pessoa)

# Alterando o valor de uma chave já existente:
pessoa['Nome'] = 'Glenda'
pessoa['sobrenome'] = 'Lima'
print(pessoa)

"""
Removendo elementos de uma lista
"""

# Forma 1: Usando o pop(). É a mais comum
removido = pessoa.pop('Sexo')  # A chave e valor de "Sexo" foram removidos
print(pessoa)
print(removido)  # O conteúdo removido (apenas o valor) pode ser armazenando em uma variável (tal como é feito com listas)

# OBS 1: Nessa forma 1, sempre precisamos informar a chave, e ela precisar estar correta, caso contrário, gera um KeyError
# OBS 2: Ao usarmos o pop('') o valor do elemento removido é sempre retornado, por isso podemos caputa-lo se necessário.


# Forma 2: usando o comando del ...
del pessoa['Idade']

# OBS 1: Se a chave não existir é gerado também um KeyError
# OBS 2: Com esse método não é possível capturar o valor do elemento que está sendo deletado.


"""
Exemplo de uso
Imagine que você tem um comércio eletrônico, onde tem um carrinho de compras no qual o usuário/comprador adiciona produtos.

Carrinho de Compras:
  Item 1:
    nome,
    quantidade,
    valor
  Item 2:
    nome,
    quantidade,
    valor
"""

# Criamos uma lista
carrinho = []

# Produto 1
carrinho.append({
    'nome': 'Teclado USB Abnt Multilaser',
    'quantidade': 2,
    'valor_unitario': 22.80
})

# Produto 2
carrinho.append({
    'nome': 'Mouse Gamer',
    'quantidade': 2,
    'valor_unitario': 35.80
})

print(carrinho)

# Imprime o nome do produto 0
print(carrinho[0]['nome'])

"""
Outros métodos de dicionários:
"""
# copy(): Semelhante à lista, esse método permite a cópia de um dicionário.
# Obs: assim como em listas, o dicionário tem o Deepcopy e Shallowcopy. Então cuidado ao criar cópias de dicionários
pessoa2 = pessoa.copy()

# clear(): Limpa todos o conteúdo (seria usado para eevaziar o carrinho)
pessoa.clear()

print('pessoa:', pessoa)  # Resultado: {}
print('pessoa2:', pessoa2)  # Resultado: Todo o valor que continha em pessoa antes do clear()


# {}.fromkeys. Forma não usual de criação de dicionários
empresa = {}.fromkeys('nome', 'Sismais Tecnologia')

# .keys(): Retorna uma lista com as chaves de um dicionário
print(pessoa2.keys())

# .values(): Retorna uma lista com os valores de um dicionário
print(pessoa2.values())

# .items() retorna uma lista com tuplas contendo a chave e valor do item. Ex: [(chave1, valor2), (chave2, valor2), (chave3, valor3)]
print(pessoa2.items())

# No exemplo abaixo criamos várias chaves e todas com o valor 'não definido'
empresa = {}.fromkeys(['fantasia', 'cnpj', 'ie', 'edereco'], 'não definido')
print(empresa)

# Iterando em dicionários
print('Imprimindo dados de pessoa:')

# iterando apenas na chave e acessando o valor pela variável "chave"
print('{:<20}'.format('  Chave  ') + '  Valor')
for chave in pessoa2:
    print('{:.<20}'.format(chave.title()) + f': {pessoa2[chave]}')

# Itegrando com chave e valor em variáveis próprias
for chave, valor in pessoa2.items():
    print('{:.<20}'.format(f'Chave "{chave}"') + f': Valor: {valor}')

for valor in pessoa2.values():
    print('Iterando apenas sobre os valores. Valor: ', valor)





# Operações em dicionários: Soma, Valor Máximo, Valor Mínimo, Tamanho

print(len(pessoa2))  # Resultado: 6

"""
O parâmetro **kwargs  (Keyword Arguments)

- Semelhante ao "*args" o "**kwargs" (com dois asteriscos) permite usarmos tantos parâmetros quanto precisarmos.
  Mas diferente do *args que coloca os valores em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados.
  Esses parâmetros nomeados são transformados em um dicionários.

- Ele é definido sempre por 2 (dois) asteriscos: **.
  O nome usado poderia ser qualquer um, ex: "**parametros" porém, por convenção, a comunidade
  também adotou  o uso do nome "kwargs"


Nas nossas funcções podemos ter (nesta mesma ordem):

- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios);
- **kwargs
"""


# Exemplo
def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é: {cor}')


# Resultado: {'maicon': 'Azul', 'glenda': 'Rosa', 'glauber': 'Amarelo'}
cores_favoritas(maicon='Azul', glenda='Rosa', glauber='Amarelo')

# Obs: Lembrando que os parâmetros *args e **kwargs são opcionais:
# Resultado: {}
cores_favoritas()

# Exemplo mais complexo:
def cumprimento_especial(**kwargs):
    if 'sismais' in kwargs and kwargs['sismais'] == 'Maxpró ERP':
        return 'Yes! Muito bem!'
    else:
        return 'Resposta errada :/'


print(cumprimento_especial(sismais='Maxpró ERP'))


# Exemplo com as combinações de parâmetros possíveis:
def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos de idade.')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


print('{:-^48}'.format('-'))
minha_funcao(29, 'Maicon')
print('{:-^48}'.format('-'))
minha_funcao(21, 'Glenda', 4, 5, 3, solteiro=False)
print('{:-^48}'.format('-'))
minha_funcao(10, 'Glauber', solteiro=True, eu='Não', voce='Vai')
print('{:-^48}'.format('-'))
minha_funcao(8, 'João', 9, 4, 3, freefire=True, celular='Motorola', programador='Não', horas_jogando=258.50)

###############################################################################
"""
A importância de manter a ordem dos parâmetros
"""

##########################################################
# Função com ordem CORRETA:
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, *args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='Saraiva', nome='Maicon', cargo='CTO'))
# Resultado: [1, 2, 3, 'Geek', {'sobrenome': 'Saraiva', 'nome': 'Maicon', 'cargo': 'CTO'}]

##########################################################
# Função com a ordem INCORRETA DOS PARÂMETROS: (trocamos a ordem do *args e "instrutor"
def mostra_info_errada(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, *args, instrutor, kwargs]


print(mostra_info_errada(1, 2, 3, sobrenome='Saraiva', nome='Maicon', cargo='CTO'))
# Resultado: [1, 2, 3, {'sobrenome': 'Saraiva', 'nome': 'Maicon', 'cargo': 'CTO'}]
# O parâmetro "instrutor" ('Geek') foi ignorado.


###############################################################################
"""
Desempacotar com **kwargs
"""


def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} - {kwargs["sobrenome"]}'

# Uso clássico
print(mostra_nomes(nome='Maicon', sobrenome='Saraiva'))

# Uso com desempacotamento:

nomes = {'nome': 'Glenda', 'sobrenome': 'Lima'}

print(mostra_nomes(**nomes))






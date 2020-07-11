"""
Generators

Em aulas anteriores nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
- Tuple Comprehension, porque elas se chama Generators

Na verdade não existe o Tuple Comprehension, existe o objeto do tipo generators, que é o resultado da execução
do código semelhante ao list comprehension, porém usando () no lugar dde [].

Uma vantagem do Generator é que ele ocupa menos recursos da memória (tem melhor desempenho). (confirmar isso)

A recomendação é usar o Generator quando quisermos fazer uma verificação e não precisarmos dos dados resultados
do Comprehension. Assim após o uso ele será limpado da memória automáticamente.
"""

# List Comprehension comum
nomes = ['Carlos', 'Camila', 'caio', 'Cassio', 'Claudio', 'Julia']

# Retornando uma nova lista de nomes, somente das pessoas que tenha inicial igual a C (maiúscula ou minuscula).
res = [nome for nome in nomes if nome[0] in 'Cc']
print(res)  # ['Carlos', 'Camila', 'caio', 'Cassio', 'Claudio']


# Agora vamos fazer usando o objeto generators. Em termos de sintaxe, apenas trocamos o [] por parênteses ().

res = (nome for nome in nomes if nome[0] in 'Cc')
print(res)  # <generator object <genexpr> at 0x011D9300>
print(list(res))  # ['Carlos', 'Camila', 'caio', 'Cassio', 'Claudio']
print(list(res))  # []
"""
IMPORTANTE: Assim como o filter() e map(), depois que acessamos o conteúdo dentro de um objeto do tipo "generator" ele
é automaticamente excluído/limpo da memória. Por isso, ao tentar acessar a segunda vez, retorna uma lista vazia.
"""

# Quando usamos o generators dentro de uma função, não precisamos colocar um parênteses adicional.
numeros = [2, 4, 6, 8]

# Exemplo list comprehension:
print(all([numero % 2 == 0 for numero in numeros]))  # True
# Agora vamos usar o generators
print(all(numero % 2 == 0 for numero in numeros))  # True


# Vamos usar uma função da biblioteca sys para comparar o tamanho de ambos objetos
from sys import getsizeof

# getsizeof() retorna a quantidade de bytes em memória que o conteúdo ou objeto está ocupando
print(getsizeof('Maicon Saraiva'))  # 39

# List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com generator:
gen_comp = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória (em bytes):')
print(f'List Comprehension: {list_comp}')  # 4508
print(f'Set Comprehension: {set_comp}')  # 16492
print(f'Dict Comprehension: {dict_comp}')  # 20536
print(f'Generators: {gen_comp}')  # 56

# Mesmo depois de acessar os dados ele continua ocupando poucos bytes.
gen_comp = (x * 10 for x in range(1000))
print(f'Generator Expression: {getsizeof(gen_comp)}')  # 56
print(list(gen_comp))  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120...
print(f'Generator Expression: {getsizeof(gen_comp)}')  # 56

# Diferente dos demais Comprehensions, o Generator Expression mantém os dados de forma "bruta" na memória, e irá
# trata-los somente quando fizermos o acesso, ex: list(obj).
# E quando isso for feito, ele será destruído automaticamente. (Obs: Porém se nós atribuirmos o resultado à uma
# outra variável, então teremos criado outro objeto na memória)


# Obs: o objeto generator também é iterável

gen_comp = (x for x in range(50))
for x in gen_comp:
    print(x)

"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

De forma geral, ranges são utilizados para gerar sequências númericas de maneira consecutiva (intervalo exato)

Formas gerais:

Forma 1:
  range(valor_final, valor_inicial)

Obs: valor_inicial não é inclusive (não fará parte do loop, apenas o numero inferior a ele)

Forma 2:
No range podemos, suprimir o valor_inicial. Quando isso ocorre, por padrão o valor_inicial é "0" (zero),
e a passagem/increment é de "1" (um)
  range(valor_final)

Forma 3:
Range com especificação do "step" (intervalo de avanço)
Exemplo:
  range(valor_inicial, valor_final, intervalo)
Obs: Por padrão, o intervalo é "1". Se outro valor for especificado, então o range irá pular de acordo com esse valor.
  numeros = range(1, 11, 2)  # Resultado: 1, 3, 5, 7, 9

Forma 4:
Range semelhante à forma 3, só que com a inversão dos números.
"""

# Exemplo de range normal
for n in range(1, 11):
    print(f'Posição atual: {n}')  # Resultado: irá imprimir os números de 1 a 10 (o 11 não é considerado)

# Exemplo de range com valor inicial suprimido
for n in range(11):
    print(f'Posição atual === {n}')  # Irá imprimir de 0 a 10 (11 impressões), mas ainda assim, o 11 não será impresso.


# Exemplo de range com intervalo especificado
for n in range(1, 11, 2):
    print(f'Range com passo = 2. Posição atual: {n}')  # Resultado: 1, 3, 5, 7, 9

"""
# Range com inputs do usuário
inicio = int(input('Informe um valor INICIAL para o range: '))
fim = int(input('Informe um valor FINAL para o range: '))
intervalo = int(input('Informe um INTERVALO de avanço para o range (o padrão é 1): '))

print(f'### Range especificado pelo usuário: range({inicio}, {fim + 1}, {intervalo}) ###')
for n in range(inicio, fim+1, intervalo):
    print(f'Posição atual: {n}')
    
"""


# Exemplo de range inverso
for n in range(10, 0, -1):
    print(f'Posição: {n}')  # Resultado: Vai de 10 até 1, decrementando 1. Obs: (o "0" não é inclusivo, ou seja não conta)

# Convertendo um range em uma lista

# Errado:
lista = range(0, 11)  # Nesse exemplo, a variável "lista" será do tipo "range" e não uma lista de fato.

# Certo:
lista = list(range(0, 11))  # Agora sim, criamos uma lista à partir de um range: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
len() -> Retorna o tamanho de um iterável
  - Em uma string, retorna a quantidade de caracteres
  - Em uma lista, retorna a quantidade de elementos
  - O mesmo vale para, tupla, conjunto e dicionário
  - IMPORTANTE: Por debaixo dos panos, quando utilizamos a função len() o python faz o seguinte:
    (obj).__len__()
    Esse tipo de função é chamado de "Dunder" (dois underlines)
"""

# Exemplo Len
print(len('Maicon Saraiva'))  # 14
print('Maicon Saraiva'.__len__())  # 14

"""
abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
  Todo valor que for passado no parâmetro vai retornar sempre positivo, seja ele positivo ou negativo.
"""

# Exemplos
print(abs(-5))  # 5
print(abs(5))  # 5
print(abs(-5.80))  # 5.80
print(abs(5.80))  # 5.80

"""
sum() -> Soma os valores de um iterável.

O sum, pode opcionalmente, receber um segundo argumento, que irá representar o valor inicial da soma.
Por default, esse valor inicial é 0.
"""
numeros = [1, 2, 10, 55]
print(sum(numeros))  # 68
# Exemplo com valor inicial definido
print(sum(numeros, 10))  # 78

# Sum em um dicionário
dicionario = {'a': 2, 'b': 10, 'c': 22.7, 'e': 90, 'd': 70}
print(sum(dicionario.values()))  # 194.7


"""
round() -> Retorna um número arredondado para N digitos de precisão após a casa decimal.
Se a precisão não for informada, retorna o inteiro mais próximo da entrada.
"""

# Exemplos
print(round(10.2))  # 10
print(round(10.65))  # 11
print(round(-10.65))  # -11
print(round(10.2591, 2))  # 10.26
print(round(-10.2595, 2))  # -10.26
print(round(-10.2595, 3))  # -10.259
print(round(-10.25956, 3))  # -10.26


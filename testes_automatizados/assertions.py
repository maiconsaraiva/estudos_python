"""
Assertions (Afirmações / Checagens / Questionamentos)

Em Python, usamos a palavra reservada "assert" para realizar simples afirmações utilizadas nos testes.

Utilizamos o "assert" em uma expressão que queremos checar se é valida ou não.
Se a expressão for verdadeira, retorna None e se for falsa, levanta um erro do tipo AssertionError


Obs:
- Nós podemos específicar, opcionalmente, um segundo argumento, ou mesmo uma mensagem de erro personalizada.
- A palavra "assert" pode ser utilizada em qualquer função ou código nosso. Não precisa ser exlcusivamente nos testes.

IMPORTANTE:
Cuidado ao utilizar assert: Se um programa python for executado com o parâmetro "-O" nenhum assertion será validado.


O assert já foi muito utilizado para validações e tratamentos de erros, mas hoje em dia não é tão usado.

ToDo: Em que cassos hoje em dia é usado o assert?
"""


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'a e b precisam ser positivos'
    return a + b


print(soma_numeros_positivos(1, 2))  # 3

# print(soma_numeros_positivos(1, -2))  # AssertionError: a e b precisam ser positivos


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doce',
        'batata frita',
        'cachorro quente',
        'hamburguer'
    ], '"comida" precisa ser fast food'
    return f'Eu estou comendo {comida}'


print(comer_fast_food('pizza'))  # Eu estou comendo pizza

print(comer_fast_food('arroz'))  # AssertionError: "comida" precisa ser fast food

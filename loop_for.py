"""
Loop -> É uma estrutura de repetição. Utilizamos para iterar sobre sequências ou sobre valores iteráveis.
No Python, um loop pode ser feito de duas formas:
  - For
  - While

For no Delphi:
var i : Integer;
begin
  for i := 0 to Objeto.Count-1 then
  begin
    PrintLN('Objeto atual: '+Objeto[i]);
  end;
end;

No Python a "iteração" (loop) pode ser feita sobre:
- String
  nome = 'Maicon Saraiva'  # A iteração é feita nos caracteres que compõem a string.
- Lista
  lista = [1, 2, 3, 4, 50, 200]
- Range
  intervalo = range(1, 10)  # O range é um intervalo, neste exemplo ele vai de 1 a 10.
"""

# Exemplo do for em String
print('1 ---------------------')
nome = 'Maicon Saraiva'
for letra in nome:
    print(letra)

# Exemplo do for com lista
print('2 ---------------------')
lista = [1, 2, 3, 4, 50, 200]
for numero in lista:
    print(numero)

# Exemplo do for com range
print('3 ----------------------')
intervalo = range(1, 10)
for numero in intervalo:
    print(numero)
"""
# IMPORTANTE: O valor final do range (neste caso o "10") não é incluso. Ou seja a contagem vai até 9.
No for acima o resultado dos prints vai ser:
1
2
3
4
5
6
7
8
9

"""

"""
# For com acesso ao índice (chave/valor), semelhante à outras linguagens (como o Delphi).
Para fazer esse tipo de for, basta usar o "for i in enumerate(variavel_ou_range)"
"""
print('4 ---------------------')
for i, _ in enumerate(nome):
    print(nome[i])

# No exemplo abaixo, eu crio uma lista com chave na posição "0" e valor na posição "1"
print('5 ---------------------')
for lista_caracteres in enumerate(nome):
    print(f'Índice/Chave: {lista_caracteres[0]}  |  Valor:  {lista_caracteres[1]} ')


# Exemplo de for iterando no índice e também no valor, mas em variáveis distintas.
print('6 ---------------------')
for i, letra in enumerate(nome):
    print(f'{nome[i]} = {letra}')  # Temos 2 formas de acessar os caracteres dentro da string no qual estamos iterando

"""
Quando não precisamos de um valor (chave ou valor), podemos descarta-lo usando o "-" (underline).
No exemplo abaixo, o índice (que foi descartado usando o "_")
"""
print('7 ---------------------')
for _, letra in enumerate(nome):
    print(letra)

# Exemplo usando o range com variável e input
print('7 ---------------------')
qtde = 6  # int(input('Quantas vezes esse loop deve rodar? '))
"""
É importante lembrar que o final do range não é considerado, então de acordo com o contexto da pergunta ao usuário,
o valor capturado na variável "qtde" dever receber + 1 no final do range.
"""
print('8 ---------------------')
for n in range(1, qtde + 1):
    print(f'Imprimindo: {n}')  # Vai imprimir exatamente a qtde de vezes que o usuário informou.

"""
Exemplo de for usando a multiplicação de strings
"""
print('9 ---------------------')
nome = 'Maicon'
for valor in range(1, 11):
    print((nome + ' ') * valor)  # Cada passagem no for imprime 'Maicon' * valor
"""
O Resultado será este abaixo:
Maicon
Maicon Maicon
Maicon Maicon Maicon
Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon
Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon Maicon
"""

# Exemplo de um for dentro de outro for:
print('10 ---------------------')
nome = 'Maicon'
# A estrutura abaixo vai repetir 5 vezes o código executado anteriormente
for x in range(1, 6):
    print(f'Vez N° {x}')
    for valor in range(1, 11):
        print((nome + ' ') * valor)


# Aplicando em uma situação real. Supondo que uma empresa fature 50.000 por mês atualmente.
# Se ela tiver um crescimento de 10% ao mês, quanto ela estará faturando em 12 meses?

meses = range(2, 13) # Começa a partir do mês 2, e vai até o 12° mês.
faturamento = 50000
for mes in meses:
    faturamento = faturamento + (faturamento * 0.1)

print(faturamento)




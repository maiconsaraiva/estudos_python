"""
Tipo de Dados Numerico (Inteiros)

- No python o campo do tipo Numerico/Inteiro não tem limite de tamanho. (É um dos motivos dele ser tão usado para
  cálculos cientificos)
  Ex: 123456789012345678901233456789012345678901234567890  # Este é um número válido

"""

# Módulo (obtém o resto de uma divisão
num = 5 % 2 # Resultado 1

""""
O Mod (módulo) é utilizado para obter o resto da divisão entre dois números:
  Num1 % Num2
No Python ele é implementado da seguinte forma: 5 % 2 
Em algumas linguagens como o Delphi, a implementação é assim: 5 Mod 2 
pode ser utilizado também para verificar se um núero é par ou impar.
Para fazer isso, basta fazer o Mod (%) dele por 2. 
  - O resultado do Mod de qualquer número ímpar por 2, será sempre 1
  - O resultado do Mod de qualquer número par por 2, será sempre 0
  
Exemplos:
  5 % 2 # Resultado: 1 (5 dividido por 2 é igual a 2.5, se considerarmos números inteiros, seria 4, e sobra 1)
  6 % 2 # Resultado: 0  
"""

# Exemplo de laço (loop) com Mod
num = 0
while num <= 1000000:
    if (num % 2) == 0:
        print(f"###################### - {num} é par.")
    else:
        print(f"====================== - {num} é ímpar.")
    num += 1

""" Observando o exemplo acima, podemos perceber que uma utilidade interessante é quando queremos fazer um loop,
e dentro dele queremos fazer implementações alternativas. Exemplo: Uma Grid/Tabela com cor "zebrada".
"""

# Divisão
# 5 / 2 = 2.5

# Divisão já convertendo o resultado para um número inteiro (com barras duplas)
# 5 // 2 = 2
# É equivalente a: int(5 / 2)

# Multiplicação
# 5 * 2 = 10

# Potência (X elevado a Y)
# 5 ** 5 = 25
# 2 ** 10 = 1024
# 2 ** 100 = 1267650600228229401496703205376

"""
Ao preencher uma constante ou variável em Python, nas versões mais novas existe um facilitador
para visualização dos separadores de milhar
Exemplo, na variável abaixo olhando rapidamente não dá pra saber se o número é 1 milhão, ou 100 milhões ou 1 bilhão
  num = 100000000
Mas na atribuição abaixo (que o Python entende perfeitamente), eu posso passar o valor para a variável
usando uma formatação amigável pra mim (programador)
  num = 100_000_000 # 100 milhões, mais rápido para saber não é?
"""

"""
Incremento e decremento em valores númericos
  num = 1
  num += 1  # O resultado é: 2
  num = 3
  num -= 1  # O resultado é: 2
"""

""" 
No Python, um cálculo sobre a própria variável pode ser feita das seguintes formas:
Multiplicação clássica:
  num = 5;
  num = num * 5 # Resultado: 25
Multiplicação fácil
  num = 5
  num *= 5 # Resultado: 25
Exemplos com os demais operadores:
  # Divisão
  num = 5
  num /= 2 # Resultado: 2.5 (é o mesmo que: num = num / 5 )
  
  #Divisão com cast para inteiro
  num = 5
  num //= 2 # Resultado: 2.5 (é o mesmo que: num = num // 2)
  
  # Soma e subtração
  num = 5
  num -= 1 # Resultado: 4
  num +=5  # Resultado: 9
  
  # Potência
  num = 5
  num **= 5 # Resultado: 3125  (5 elevado à quinta potência, é o mesmo que: num = num ** 5 )     
"""








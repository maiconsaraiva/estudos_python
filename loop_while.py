"""
 While = O While é uma forma de loop que difere um pouco do for.

Forma geral:

while expressao_booleana:
    //Codigos dentro do loop

Obs: No exemplo acima, o programa só irá sair do loop se "expressao_booleana" for true
"""

# Exemplo prático
idade = 1
while idade < 18:
    idade += 1  # Faz um incremento na variável. Quando ela atingir o número 18, então sairá do loop.
    if idade < 18:
        print(f'Idade ainda não é 18: {idade}')
    else:
        print(f'Ok. idade é igual a 18. Iremos sair do loop agora!')

"""
IMPORTANTE: No "while" é importante tratar do critério de saída, caso contrário, podemos criar um loop infinito.

Exemplo de loop infinito:

idade = 1
while idade = idade:
  print(f'"idade" sempre será igual a "idade". Por tanto, loop infinito. Valor de idade: {idade}')
  
Exemplo 2:

continuar = True
while continuar:
    print('Estou continuando...')

No exemplo acima, se eu não definir o valor de "continuar" para "false" em algum momento, ele ficará em loop infinito.   

"""


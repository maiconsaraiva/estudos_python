"""
Tipo Float (conhecido também como: tipo real, ou tipo decimal)

Importante: O separador decimal na programação é sempre o . (ponto) e não a , (vírgula).
            Isso vale para toda linguagem e em qualquer lugar do mundo.
            No Brasil, por convenção usa-se a , (vírgula) como separador decimal. Mas, na programação continua sendo
            o "." (ponto). Porém, na apresentação de dados ao usuário, pode ser utilizada a vírgula.

            # Errado (quando se quer atribuir um float):
            variavel = 1, 4 # O Python irá entender que você está criando uma variável do tipo Tupla, e não um Float.
            print(variavel) # Resultado: (1,4)
            type(variavel) # Resultado: tuple (Tipo de dados Tupla)

            # Correto:
            variavel = 1.4
            print(variavel) # Resultado: 1.4
            type(variavel) # Resultado: float

"""

# Converter Float para Int
v_float = 1.4
print(int(v_float))  # Resultado: 1
# Obs: Ao converter valores do tipo Float para Int perdemos os valores decimais. Cuidado ao usar essa conversão

# Podemos trabalhar com números complexos:

"""
 Todo: Verificar
 
 O cálculo abaixo resulta estranhamento o resultado 0.43999999999999995, precisamos analisar o por que.
 num = 1.44
 num = num - 1  # Resultado: 0.43999999999999995, o correto seria: 0.44
 
 Resposta:
 
"""



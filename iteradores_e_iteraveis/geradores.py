"""
Generators (Geradores)

- Todo generator é um iterador, mas nem todo iterador é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada: yield
- Generators podem ser criados com Expressões Geradoras

Diferenças entre Funções e Generator Functions (Funções Geradoras)


| Funções                        | Generator Funcions
---------------------------------------------------------------------
| - Utilizam return              | - Utilizam yield
| - Retorna uma vez              | - Podem utilizar yield múltiplas vezes
| - Quando executada, pode ou    | - Quando executada, retorna um generator
|     não retornar um valor      |
|                                |


Obs: Uma Generator Function não é um generator, ela gera um generator. Ela gera um generator.
"""


# Exemplo de Generator Function
def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        # quando o yield é acionado ele retorna o valor, e aguarda o next() para continuar
        yield contador
        contador = contador + 1


gen = conta_ate(5)
print(gen)  # <generator object conta_ate at 0x0150B530>
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
# print(next(gen))  # StopInteration


print('Usando o for:')
gen = conta_ate(10)
for num in gen:
    print(num)


# Transformando o retorno em uma lista, o next() já é acionado todas as vezes:
lista = list(conta_ate(6))  # [1, 2, 3, 4, 5, 6]
print(lista)

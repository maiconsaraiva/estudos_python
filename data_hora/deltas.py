"""
Trabalhando com deltas de data e hora
"""

import datetime

hoje = datetime.datetime.now()

aniversario = datetime.datetime(2021, 7, 23)

# Ao calcular a diferença abaixo, obtermos um objeto do tipo DateTime TimeDelta
diferenca = aniversario - hoje

print(type(diferenca))  # <class 'datetime.timedelta'>
print(repr(diferenca))  # datetime.timedelta(days=345, seconds=3183, microseconds=128160)
print(diferenca)  # 345 days, 0:52:39.362057
print(f'Faltam {diferenca.days} dias, {diferenca.seconds // 60 // 60} horas.')


# Outro exemplo
data_venda = datetime.datetime.now()

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto) # 3 days, 0:00:00

vencimento_boleto = data_venda + regra_boleto

print(vencimento_boleto)  # 2020-08-14 23:10:26.677389

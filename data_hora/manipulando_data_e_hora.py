"""
Manipulando Data e Hora

Diferente de algumas linguagens como o Delphi, o Python não tem um Tipo DateTime. A data e hora no Python são tratados
como objetos. E é em cima dos objetos que trabalhamos com data hora.

Python tem um módulo builtin para se trabalhar com Data e Hora: datetime.

Algumas constantes:

datetime.MINYEAR
datetime.MAXYEAR

Classes:

datetime
"""

import datetime
# print(dir(datetime))

# Retorna a data e hora atuais
print(datetime.datetime.now())  # 2020-08-11 22:12:22.891512

# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))  # datetime.datetime(2020, 8, 11, 22, 13, 13, 131155)


inicio = datetime.datetime.now()

inicio.replace(year=2019, month=7, day=10, hour=21, minute=15, microsecond=200000)
print(inicio)

# é possível acessar facilmente os elementos individuais que compõem a data e hora
print(inicio.minute)
print(inicio.hour)



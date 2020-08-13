"""
Métodos de Data e Hora


#Com o now() podemos específicar o timezone.
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

"""
import datetime
import locale

print(locale.getlocale())


# Define o locale (internacionalização) para o formato do windows)
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


# Mudanças ocorrendo à meia noite: combine()
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())

print(manutencao)
print(type(manutencao))
print(repr(manutencao))

# weekday retorna um índice contendo o dia da semana (começando em "0"), sendo:
# 0 = Segunda-feira (Monday, 6 = Domingo (Sunday)
print(manutencao.weekday())

# Formatando Data/Hora com strftime() (String Format Time)
# Códigos de formatos de Data e Hora no Python:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
print(manutencao.strftime('%A, %d de %B de %Y'))  # quinta-feira, 13 de agosto de 2020
print(manutencao.strftime('%x'))  # 13/08/2020


# Método strptime() - Permite transformar uma string em um datetime
nascimento = datetime.datetime.strptime('23/07/1990', '%d/%m/%Y')

print(nascimento.year)
print(nascimento.month)
print(nascimento.day)


# Trabalhando somente com Hora:

hora_almoco = datetime.time(12, 30, 0)
print(hora_almoco.__str__())  # 12:30:00



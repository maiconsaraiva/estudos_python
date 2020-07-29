"""
Forçando Tipos de Dados com Decoradores
"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte
    return decorador


@forca_tipo(str, int)  # Usando o decorator desta forma estamos forçando o tipo de dado de cada parâmetro
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Maicon', 3)

repete_msg('Maicon', '3')  # Não dá erro, pois é forçada uma conversão para int() dentro de "forca_tipo"

repete_msg('Maicon', '3.3')  # ValueError: invalid literal for int() with base 10: '3.3'

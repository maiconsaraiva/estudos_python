"""
Exemplo de módulo que será testado com unittest
"""


def comer(comida, eh_saudavel):
    if eh_saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'a gente só vive uma vez.'
    return f'Estou comendo {comida} porque {final}'


def dormir(num_horas):
    if num_horas > 8:
        return 'Puts! Dormi muito!'
    else:
        return 'Continuo cansado após dormir por 4 horas. :('

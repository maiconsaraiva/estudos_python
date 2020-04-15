"""
Saindo de loops "for" ou "while" com Breaks

O break no Python funciona da mesmas forma que nas linguagens C, Java, Delphi, etc.

Utilizamos o break para sair do loop a qualquer momento (independente da condição estabelecida)
"""

# Exemplo
emoji_sorriso = '\U0001F603'
continuar = True
while continuar:
    if input('Deseja executar o break agora? (escreva = "sim" para sair) ') == 'sim':
        print('Ok. Saindo do break!!! '+emoji_sorriso)
        break
    else:
        print('Ok. Continuando...')


# Outro exemplo

print('#### Conteúdo com restrição de idade ####')
emoji_piscada = '\U0001F609'
idade = 0
while idade < 18:
    idade = int(input('Qual a sua idade?'))
    if idade >= 18:
        print('Ok, conteúdo liberado! '+emoji_piscada)
        break
    else:
        print('Conteúdo bloqueado!')


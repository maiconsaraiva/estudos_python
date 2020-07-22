"""
Sistema de Arquivos e Navegação

Para fazer uso e manipulação de arquivos do sistema operacional, usamos o módulo os.
"""

import os

# Obtém o caminho absoluto atual
print(os.getcwd())

# Mudar de diretório
os.chdir('..')
print(os.getcwd())  # Vai mostrar o diretório acima

# Verifica se um diretório é absoluto ou relativo
print(os.path.isabs('C:/Dev/Curso/Curso/estudos_python/arquivos/'))

"""
OBS PARA USUÁRIOS WINDOWS:
Se você estiver usando Windows, terá que ter cuidados ao verificar diretórios, o diretório deverá ter a barra
invertida.
Ex:
os.path.isabs(C:\\Dev\\Curso')
"""

# Podemos identificar o sistema operacional
print(os.name)  # Resultados: "posix" (Linus e Mac), "nt" (windows)
# print(os.uname())  # AttributeError: module 'os' has no attribute 'uname'
# O Windows não vai ter a função uname(). Em substituição podemos usar o sys
import sys
print(sys.platform)

# pegar o diretorio atual e adicionar uma outra pasta (join)
res = os.path.join(os.getcwd(), 'arquivos')
print(res)  # C:\Dev\Curso\estudos_python\arquivos
os.chdir(res)

# Verificar se um diretório ou arquivo existe
print(os.path.exists(res + '/outra_pasta'))  # False

# Listar diretórios e/ou arquivos
print(os.listdir())



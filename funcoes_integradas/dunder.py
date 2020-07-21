"""
Dunder Name e Dunder Main

Dunder -> Duble underline

Em Python, são utilizados dunder para criar funções, atributos, propriedades e etc., utilizando Double under para não
gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:
int main() {
  return 0:
}

# Na linguagem Java, temos um programa da seguinte forma:
public static void main(String[] args){
}

# Em Python, se executarmos um arquivo/módulo diretamente na linha de comando, internamente, o Python atribuirá a variável
__name__ o valor __main__ indicando que este é o módulo de execução principal.

Para entender o uso que podemos fazer desses métodos pense no seguinte cenário:
1. Temos um arquivo com funções, e um código print(ALGUMA_COISA), que não está dentro de uma função (está livre);
2. Vamos supor que, se dermos o import desse arquivo, não queremos executar esse print. Vamos querer que ele seja
   executado somente quando executarmos o arquivo diretamente.
   Mas ao dar o import, o código automaticamente é acionado.
3. Para resolver isso, podemos fazer o uso do __name__ e __main__ para checar se o arquivo está sendo executado
diretamente (como programa principal).
Ex:
def minha_funcao(x):
    return x

# O código abaixo é uma verificação, e checa se o arquivo está sendo importado ou executado diretamente
# O print(ALGUMA_COISA) só vai ser executado se o programa for executado diretamente, ex: python este_arquivo.py
if __name__ = '__main__':
    print(ALGUMA_COISA)


# Quando o arquivo é importado, a propriedade __name__ irá retornar o próprio nome do arquivo, sem a extensão.
"""



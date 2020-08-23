"""

Garbage Collector
- O algoritmo utilizado pelo Garbage Collector do Python é chamado de "Reference Counting"
  Podemos saber qual o contador de referência existe em um objeto (ou seja, quantas variáveis estão
  apontando para um objeto em memória). Para isso utilizamos o método abaixo:
  import sys

  a = []
  b = a
  sys.getrefcount(a)
  #Podemos passar qualquer uma das variáveis que apontam para o objeto que desejamos obter o número de referências

- Diferentes linguagens de programação utilizam diferentes algoritmos para o Garbage Collector;
- Até mesmo diferentes implementações da linguagem Python utilizam diferentes implementações para o Garbage Collector:
  CPython, PyPy, IronPython, Stackless, Jython...
  Obs: A implementação padrão do Python é a CPython, que é o Python escrito na linguagem C.

"""

# Exemplo, verificando se duas variáveis apontam para o mesmo objeto
import sys

x = 10
y = x

print(id(y))
print(id(x))

if id(x) == id(y):
    print(f'x e y referenciam o mesmo endereço na memória.')


z = x + 1
print(id(x) == id(z))  # False. Neste caso aqui, criamos uma nova alocação na memória e z aponta para ela.

# Contanto as referências do objeto para o qual x faz referência.
# Note que o contador já está em 15. Provavelmente por baixo dos panos o python deve ter outras variáveis
# que apontam para o objeto int 10 na memória)
# Obs: o próprio argumento passado em getrefcount(x) faz também referência ao objeto na memória então ele
# faz parte do 15 retornado.
print(sys.getrefcount(x))  # 15


# No Python, se criarmos uma nova variável e também colocarmos o valor 10 (tal como feito com x), ele irá aproveitar
# o mesmo objeto já alocado na memória. Ou seja, agora, x e w referenciam o mesmo objeto na memoria, o Python reutiliza
# de forma inteligente valores já alocados em memoria, economizando espaço.
# Em outras linguagens, diferente do Python, são criados objetos diferentes nesse tipo de situação./
w = 10
print(id(x) == id(w))  # True
print(sys.getrefcount(x))  # 16

# Embora estejam apontando para o mesmo endereço da memória, eu posso simplesmente mudar o valor de um dos dois,
# e eles irão passar a referenciar a objetos diferentes na memória.
w += 2
print(f'x: {x}, w: {w}')  # x: 10, w: 12
print(id(x) == id(w))  # False

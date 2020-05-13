from collections import Counter

"""
Módulo Collections - Counter
https://docs.python.org/3.8/library/collections.html#collections.Counter
https://docs.python.org/3.8/library/collections.html#counter-objects

Collections -> É conhecido por High-performance Container Datetypes (Tipos de dados de containers de alta performance)

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter, que é parecido com um
           dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de 
           ocorrências desse elemento.
"""

# Exemplo de utilização. Primeiramente é preciso importar o collections "from collections import Counter"

lista = [1, 1, 2, 3, 2, 3, 1, 1, 2, 24, 5, 5, 45, 66, 66, 43, 34]

res = Counter(lista)

print(type(res))  # Resultado: collections.Counter
print(res)  # Resultado: Counter({1: 4, 2: 3, 3: 2, 5: 2, 66: 2, 24: 1, 45: 1, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2
lista = ['A', 'B', 'b', 'A', 'A', 'C', 'D', 'E', 'E', 2, 2, 4, 4.5, 4.5, 3, 2, 4, 3, False, False, True]
lista = Counter(lista)
print(lista)

# Exemplo 3
print(Counter('Geek University'))  
# Resultado: Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

texto = """
Eu pretendo usar um sistema Web (acessível pelo navegador). Por que usaria um sistema Desktop como o Maxpró ERP?

Os sistemas desktop ainda dominam o mercado, pois eles são superiores aos Web em termos de recursos e praticidade, 
os sistemas desktops são mais robustos (estáveis) e não dependem da internet para funcionar!

Clique aqui e Veja as Vantagens de um ERP Desktop em relação à um ERP em Nuvem.

Por ser um sistema Desktop, O Maxpró possui inúmeras vantagens como: agilidade, velocidade de acesso, segurança, alta 
compatibilidade com hardwares, independência de internet, práticidade de uso, entre outros quesitos. Além disso, possui 
também um módulo Web direcionado para os gestores das empresas (que pode ser acessível pelo navegador, e configurado 
para ser acessível de qualquer local).

No Brasil sabemos que a internet ainda está em um nível baixo em comparação com outros países, e isso pode ser uma 
grande barreira para softwares totalmente Web, principalmente se tratando de grandes empresas, ou mesmo pequenas mas 
com fluxo alto de informações, a exemplo de supermercados, lojas de conveniência, papelarias, etc.
Nós estamos torcendo para a internet no Brasil melhorar, mas até lá, vamos sempre investir no desenvolvimento do Maxpró
da melhor forma possível, tornando-o uma excelente escolha para sua empresa.
"""

palavras = texto.split()
res = Counter(palavras)
# print(res)

# Imprimindo as 5 palavras que tem mais ocorrências
print(res.most_common(5))  # Resultado: [('de', 10), ('um', 7), ('para', 6), ('em', 5), ('e', 5)] 

# Quantas vezes a palavra "sistema" é repetida no texto acima?


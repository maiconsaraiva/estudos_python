"""
Escrevendo um iterador Customizado

Vamos fazer um iterador mais ou menos parecido com o range()


Em resumo para criar um iterador customizavel basta implementar os métodos __iter__ e __next__
"""


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        """o método especial __iter__ é usado para transformar um objeto em um iterator"""
        return self

    def __next__(self):
        """o método especial __next__ também é usado para transformar um objeto em um iterator"""
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 10)

print(next(con))  # 1
print(next(con))  # 2
print(next(con))  # 3

for n in Contador(1, 10):
    print(n, end=' | ')   # 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

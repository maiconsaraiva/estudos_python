"""
POO - Métodos Mágicos.

Recapitulando: Métodos mágicos são todos os métosos que usam o Dunder (Duble Underscore), antes do nome do método.

Nós conseguimos implementar todos os métodos builtins do Python como métodos mágicos para utilizarmos da forma
que precisarmos.

Todos esses métodos mágicos que usamos como funções builtins herdam da classe object.


"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} - escrito por: {self.autor}'

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    def __del__(self):
        print(f'O livro {self.titulo} do autor {self.autor} foi deletado da memória.')

    def __add__(self, other):
        return f'Concatenando: "{self.titulo}" e "{other.titulo}" '

    def __mul__(self, other):
        """Multiplicacao. o other tem que ser inteiro"""
        if not isinstance(other, int):
            raise ValueError(f'argument "other" must be integer type: {other}')
        msg = ''
        for _ in range(other):
            msg += ' | '+str(self)
        return msg


livro1 = Livro('Instinto do Sucesso', 'Não sei', 50)
livro2 = Livro('Biografia de Steve Jobs', 'Não sei', 500)

print(livro1)  # "Instinto do Sucesso"
"""
O método __repr__ serve para implementarmos uma descrição desejada para nossa classe.
Quando damos um print(livro1) por exemplo, em vez de mostrar um endereço da memória, como:
<__main__.Livro object at 0x00B66148>



Semelhante ao método __repr__ temos o método __str__. Ambos fazem praticamente a mesma coisa, a diferença maior é que:
o __repr__ geralmente é usado para exibir detalhes para outros desenvolvedores., e o __str__ é usado para exibir dados
para o usuário da aplicação.

O __str__ geralmente retorna uma string com um ou mais atributos que nos digam "quem é" a instância.


Obs: Se por caso os dois métodos estiverem implementados, ao usar algo como:
print(livro1)
O __str__ irá prevalecer sobre o __repr__

Neste caso, é possível acessar o __repr__ da seguinte forma: repr(livro1)
"""
print(repr(livro1))


"""
Além dos exemplos acima, outra aplicabilidade para os métodos mágicos na classe, são a implementação de métodos que são
built-in do python. A exemplo do len().
Como já estudamos esse método tem comportamentos diferentes a depender do tipo de dado, em uma string
"len('Uma string')" ele retorna a quantidade de caracteres, já em um iteravel (lista, tupla, dict) é retornada a
quantidade de elementos existentes.

Nós podemos implementar dentro da nossa classe o método mágico __len__ quando for acionado um len(NossaClasse) podemos
retornar o dado desejado. No caso da classe Livro() acima, nós retornamos a quantide de páginas que o livro tem, mas
poderia ser qualquer outra informação (respeitando o tipo de dado esperado para o len() que é inteiro).

"""
print(len(livro1))  # 50
print(len(livro2))  # 500

"""
Outro exemplo: o uso do del: "del nome_variavel_ou_atributo_ou_objeto"
Geralmente, fazemos a exclusão do item da memória.
Se dermos um "del livro1" ele será excluído da memória, e não será mais possível acessa-lo.
Porém, podemos implementar o método mágico __del__ para fazer algum tratamento adicional, quando isso for feito.
No exemplo da classe Livro() acima, nós damos um print() com a mensagem de que o objeto foi excluído da memória.

"""
del livro2  # O livro Biografia de Steve Jobs do autor Não sei foi deletado da memória.


"""
É possível implementar também um método que permite a concatenação de duas instâncias.
Exemlo: se fizermos algo como: livro1 + livro2
Teremos uma Exception. Mas se por algum motivo, quisermos permitir essa operação, podemos implementar o método
mágico __add__(self, outro)
"""
print(livro1 + livro2)  # Concatenando: "Instinto do Sucesso" e "Biografia de Steve Jobs"

# Outros exemplos:

# __mul__ (multiplicando)
print(livro1 * 3)  # | Instinto do Sucesso | Instinto do Sucesso | Instinto do Sucesso
print(livro1 * 10.5)  # ValueError: argument "other" must be integer type: 10.5

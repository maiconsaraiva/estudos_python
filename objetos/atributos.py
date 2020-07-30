"""
Atributos

Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente
os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
  - Atributos de Instância;
  - Atributos de Classe;
  - Atributos Dinâmicos;


# Atributos de Instância: Declarados dentro do método construtor.

# Em java, uma class lampada, incluindo seus atributos, ficaria mais ou menos:

public class Lampada() {
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

# Atributos Publicos e Atributos Privados
Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é publico (não existe atributo privado).
Caso queiramos demonstrar que um determinado atributo deve ser tratado como privado, ou seja, que só pode ser
acessado ou alterado diretamente por dentro da própria classe, utiliza-se o "__" (duplo underline) no início do seu
nome. Isso é conhecido também como Name Mangling.

# Em Python a declaração é semelhante, porém mais simples (veja mais abaixo)
"""


class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, unidade, valor):
        self.nome = nome
        self.unidade = unidade
        self.valor = valor


# Classes com atributos de instâncias privados
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def get_senha(self):
        return self.__senha


acesso = Acesso('maicon.saliver@gmail.com', '123')

print(acesso.email)   # maicon.saliver@gmail.com
# print(acesso.__senha)  # AttributeError: 'Acesso' object has no attribute '__senha'

# Note que no teste acima, o atributo "__senha" não é acessível. Mas por que não é, já que o Python não tem a
# a definição de atributo privado?
# R: Embora ele não tenha essa definição, ele possui sim um mecanismo de segurança, que impede o acesso direto ao nome
# do atributo (e assim funciona como se fosse uma variável privada).
# Ainda assim o Python permite o acesso à este atributo, mas ele é acessível de forma diferente.
# Esse atributo publicamente é exposto da seguinte forma: _NomeDaClasse__nome_do_atributo
# E é essa convenção que recebe o nome "Name Mangling"
# Exemplo:
print(acesso._Acesso__senha)
# Temos acesso, mas por convenção não devemos fazer. Inclusive o Pycharm exibe uma advertência,
# quando tentamos acessa-lo.


# Se quisermos expor o a variável privada externamente de alguma forma, uma das maneiras recomendas, é usar um método
# que retorne o valor desse atributo
print(acesso.get_senha())


"""
Atributos de Classe

São atributos que são declarados diretamente na classe, ou seja, fora do construtor.
Geralmente, já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja,
ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os
atributos de classe todas as instâncias terão o mesmo valor para este atributo.

Em outras linguagens, como no Java, os atributos de classe são chamados de atributos estáticos.

Podemos dizer que um atributo de classe é uma constante dentro de uma classe.
Inclusive, não precisamos instanciar uma classe para fazer acesso ao atributo de classe.


Obs: Embora possamos fazer uma analogia do atributo de classe a uma constante, um atributo de classe pode ser alterado
a qualquer momento. Então podemos dizer também que um atributo de classe é também como uma variável global encapsulada
dentro da classe.
"""

p1 = Produto(nome='Teclado', valor=22, unidade='UN')
p2 = Produto(nome='Mouse', valor=14, unidade='UN')


# Vamos refatorar a classe produto
class Produto:

    percentual_imposto = 5  # 5% de imposto

    def __init__(self, nome, unidade, valor):
        self.nome = nome
        self.unidade = unidade
        self.valor = valor
        self.valor_com_imposto = valor * (1 + (Produto.percentual_imposto/100))


p3 = Produto('Monitor', 'UN', 1200)

print(f'Nome: {p3.nome}, Preço: {p3.valor_com_imposto}')  # Nome: Monitor, Preço: 1260.0

# Acessando o Atributo de Classe sem precisar criar uma instância
print(Produto.percentual_imposto)

# Alterando o valor do atributo de classe
Produto.percentual_imposto = 6
p4 = Produto('Monitor', 'UN', 1200)
print(f'Nome: {p4.nome}, Preço: {p4.valor_com_imposto}')  # Nome: Monitor, Preço: 1272.0

# Uma observação curiosa, é que podemos fazer acesso e também alterar o atributo de classe pela instância.
print(p4.percentual_imposto)  # 6
# E também conseguimos alterar o valor desse atributo de classe (embora não seja recomendado)
p4.percentual_imposto = 7
print(Produto.percentual_imposto)  # 6 (não foi alterado)
print(p4.percentual_imposto)  # 7 (embora seja um atributo e classe, foi alterado exclusivamente para
# essa instância. não é recomendado usar desta forma)


"""
Atributos Dinâmicos

Um atributo dinâmico nada mais é do que um atributo de instância que pode ser criado em tempo de execução.

Obs:
- O atributo de instância será exclusivo da instância que o criou.
- Assim como podemos criar um atributo dinamicamente, podemos excluir também.
"""

p3.peso_bruto = 10
print(p3.peso_bruto)  # 10
print(type(p3.peso_bruto))  # <class 'int'>
# print(type(p1.peso_bruto))  # AttributeError: 'Produto' object has no attribute 'peso_bruto'


# Imprimindo um dict com todos os atributos de instância e atributos dinâmicos (não inclui atributos de classe)
print(p3.__dict__)
# {'nome': 'Monitor', 'unidade': 'UN', 'valor': 1200, 'valor_com_imposto': 1260.0, 'peso_bruto': 10}

# Excluindo um atributo dinamicamente.

del p3.peso_bruto
del p3.unidade  # Podemos deletar não só atributos dinâmicos, mas também atributos de classe.
print(p3.__dict__)   # {'nome': 'Monitor', 'valor': 1200, 'valor_com_imposto': 1260.0}


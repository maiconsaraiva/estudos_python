"""
Por que testar nosso código?

Testamos o código para ver se o comportamento funciona da forma que queremos.
A automação de testes permite que configuremos os testes que queremos fazer toda vez que queremos liberar alguma,
versão nova do nosso programa. Esse procedimento evita termos que testar tudo manualmente, toda vez que algo é
modificado.

Listando alguns motivos:

- Reduzir bugs no código existente;
- Garantem que bugs que foram corrigidos anteriormente não se repitam;
- Testes garantem que novos recursos da sua aplicação não "quebrem" (afetem) recursos já existentes;
- Garantem que a refatoração que costumamos fazer não traga novos bugs;
- O Teste Automatizado acelera muito o processo de testes;


Motivo pelo qual algumas pessoas não gostam de testes:

- Requerem tempo e mais código, afinal criamos mais código para executar esses testes;
- Pode ser meio chato de se fazer;

Para facilitar o trabalho nos testes automatizados o Python e outras linguagens possuem módulos e frameworks que
aceleram esse desenvolvimento.

Além das ferramentas existe uma metodologia de desenvolvimento chamada TDD - Test Driven Development (Desenvolvimento
Guiado por Testes), que diz que já devemos ir desenvolvendo os testes conforme vamos desenvolvendo nosso código.

Com o TDD são utilizados estágios de desenvolvimento:
01. Escreve primeiramente o teste;
02. Escreve o código minimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
03. Refatora o código para realizar a funcionalidade e testa novamente;
04. Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento TDD são quase um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor;

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f'{self.__nome} está miando...')


felix = Gato('Félix')

felix.miar()

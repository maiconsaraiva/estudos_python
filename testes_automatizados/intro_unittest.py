"""
Introdução ao Unittest
https://docs.python.org/3/library/unittest.html

Unittest -> Testes Unitários
Testcase -> Casos de teste para sua unidade

Obs: Testes unitários não são específicos da linguagem Python.

O que é teste unitário?
R: É a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser:
    - Funções
    - Métodos
    - Classes
    - Módulos
    - etc.

O objeto é garantir que cada unidade atende à sua especificação, e consequentemente o projeto completo também funcione
como esperado.

O módulo Unittest é um módulo altamente recomendado do Python.

Para criar nossos testes, criamos classes que herda de unittest.TestCase, e a partir de então, ganhamos todos os
"assertions" presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

Por convenção, todos os testes em um test case, devem ter seu nome iniciado com "test_"

# Para executar os testes com unittest:
python nome_do_modulo.py

# Para executar os testes com unittest no modo verbose:
python nome_modulo -v


# Docstrings nos testes

Podemos acrescentar (e é recomendado) docstrings nos nossos testes. Quando isso é feito, um exemplo de vantagem é que,
ao executar o teste no movo verbose "-v", esses docstrings são exibidos.
Exemplo:
    python testes.py -v

    test_comer_pizza (__main__.AtividadesTestes)
    Testando o retorno com comida ruim (pizza) ... ok
    test_comer_saudavel (__main__.AtividadesTestes)
    Testando o retorno com comida saudável ... ok
    test_dormindo_muito (__main__.AtividadesTestes)
    Testando o retorno dormindo muito ... ok
    test_dormindo_pouco (__main__.AtividadesTestes)
    Testando o retorno dormindo pouco ... ok
    ----------------------------------------------------------------------
    Ran 4 tests in 0.002s



"""

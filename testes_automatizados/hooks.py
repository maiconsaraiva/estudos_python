"""
Unittest - Antes e Após Hooks

Hooks -> São os teste em si, ou seja a execução dos testes.

Quando falamos antes e após o hooks, estamos falando de executar algo antes e/ou após os testes.

O Unittest tem dois métodos para executar esses eventos antes e após hooks:

- setUp() -> É a execução antes de cada método de teste. É útil para criarmos instâncias de objetos e outros dados;
- tearDown() -> É executado ao final de cada método de teste. É útil para excluir dados ou fechar conexões com bancos
de dados.
"""
import unittest

class ModuloTest(unittest.TestCase):

    def setUp(self):
        # Configurações do setup()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes dos testes
        # tearDown() vai rodar depois dos testes
        pass

    def test_segundo(self):
        pass

    def test_terceiro(self):
        pass

    def tearDown(self):
        # Configuraões do tearDown()
        # o tearDown() ser criado em qualquer ordem. Mesmo que ele seja criado no início da classe, por exemplo.
        # ele será executado por último.
        pass

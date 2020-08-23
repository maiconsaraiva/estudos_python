"""
Módulo que implementa os testes com unittest
"""
import unittest
from atividades import comer, dormir


class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma.'
        )

    def test_comer_pizza(self):
        """Testando o retorno com comida ruim (pizza)"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente só vive uma vez.'
        )

    def test_dormindo_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormindo_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Puts! Dormi muito!'
        )


if __name__ == '__main__':
    unittest.main()


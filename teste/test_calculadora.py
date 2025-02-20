import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../modulo_calculadora")))
import calculadora

class TesteCalculadora(unittest.TestCase):

    def test_somar(self):
        resultado = calculadora.somar(3,2)
        self.assertEqual(resultado,5)

    def test_subtrair(self):
        resultado = calculadora.subtrair(3,1)
        self.assertEqual(resultado,2)
    
    def test_multiplicar(self):
        resultado = calculadora.multiplicar(3, 1)
        self.assertEqual(resultado, 3)

    def test_dividir(self):
        resultado = calculadora.dividir(3, 1)
        self.assertEqual(resultado, 3)

if __name__=='__main__':
    unittest.main()
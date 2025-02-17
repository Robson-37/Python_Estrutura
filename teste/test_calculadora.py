import unittest
from modulo_calculadora import calculadora 

class TesteCalculadoda(unittest.TestCase):

    def test_somar(self):
        resultado = calculadora.soma(3,2)
        self.assertEqual(resultado,6)

    def test_subtrair(self):
        resultado = calculadora.subtrair(3,1)
        self.assertEqual(resultado,1)
    
    #def test_mutiplicar(self):
        #self.assertEqual(mutiplicacao(3,1),3)
    #def test_subtrair(self):
        #self.assertEqual(divisao(3,1),3)

if __name__=='__main__':
    unittest.main()
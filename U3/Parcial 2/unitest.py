import unittest
from ClaseCasa import Casa
from ClaseDepto import Dpto

class TestImporteVenta(unittest.TestCase):
    def test_ImporteCasa(self):
        casa = Casa("Rivadavia", "Guemes", 10, 10)
        esperado = 10 * 15 * (10 * 1.80 * 20000)
        self.assertAlmostEqual(casa.impoVenta(), esperado)
    
    def test_ImporteDpto(self):
        depto = Dpto("Capital", "Mitre", 10, 2, 10, 5, 3)
        esperado = 10 * 15 * (2 * 17000)
        self.assertEqual(depto.importe(), esperado)

if __name__ == '__main__':
    unittest.main()
import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filtra_caixas_indisponiveis = getattr(undertest, 'filtra_caixas_indisponiveis', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       caixas = [0,1,2,3,4,5,6]
       filtra_caixas_indisponiveis(caixas,3)
       assert caixas == [3,4,5,6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))

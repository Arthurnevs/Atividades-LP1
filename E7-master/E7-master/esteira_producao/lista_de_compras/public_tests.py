#!/usr/bin/env python
import unittest
import sys
import imp

undertest = __import__(sys.argv[-1].split(".py")[0])
adiciona_item = getattr(undertest, 'adiciona_item', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
       lista = ['acucar', 'leite', 'paes', 'queijo']
       adiciona_item('cafe', lista)
       assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
        

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))

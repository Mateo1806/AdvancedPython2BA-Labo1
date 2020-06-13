# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018
#modifié

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(0), 1) #cas initial qui permet d'avoir un etalon, c'est toujours vrai
        self.assertEqual(utils.fact(5), 120) #deux valeurs qui se comparent pour creer une règle
        pass
    
    def test_roots(self):
        self.assertEqual(utils.roots(1, 0, 1), ()) #cas initial qui permet d'avoir un etalon, c'est toujours vrai
        self.assertEqual(utils.roots(1,2,-15), (-5,3))        
        pass
    
    def test_integrate(self):
        self.assertAlmostEqual(utils.integrate('x ** 2 - 1', -1, 1), -1.333, 3) #cas initial qui permet d'avoir un etalon, c'est toujours vrai
        self.assertAlmostEqual(utils.integrate('x ** 2',-2,1), -3,3 ) 
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())

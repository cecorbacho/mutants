import unittest, os
from mutants.models import human



class TestHumans(unittest.TestCase):

    def test_human(self):
        human_t = human.Human(dna='{"dna": ["ATBBGA","CABBGC","TTBBGT","AGBBGG","CBBBTA","TBBBTG"]}')
        human_check = human_t.is_mutant()
        self.assertEqual(human_check,False)

    def test_mutant(self):
        human_t = human.Human(dna='{"dna": ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]}')
        mutant_check = human_t.is_mutant()
        self.assertEqual(mutant_check,True)


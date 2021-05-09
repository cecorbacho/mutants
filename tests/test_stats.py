import unittest, os
from mutants.models import stat_dna_verification



class TestStats(unittest.TestCase):

    def test_stats(self):
        stats = stat_dna_verification.StatDnaVerification(5, 3)
        self.assertEqual(stats.ratio, 1.67)

    def test_type(self):
        stats = stat_dna_verification.StatDnaVerification(5, 4)
        self.assertEqual(type(stats.ratio), float)



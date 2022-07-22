import unittest
from main import *

# Importei como main porque joguei o codigo DNA.py nela
# Fiz os testes mas apresentaram erro de strand que não consegui resolver, imagino que seja algo bobo pois estava nervoso


class DNAtest(unittest.TestCase):

    def setUp(self):
        self.createComplement = DNA.createComplement(self)
        self.findMatchesWithLeftShift = DNA.findMatchesWithLeftShift(self, other=None, shift=None)
        self.findMatchesWithRightShift = DNA.findMatchesWithRightShift(self, other=None, shift=None)
        self.findMaxPossibleMatches = DNA.findMaxPossibleMatches(self, other=None)
        self.countMatchesWithLeftShift = DNA.countMatchesWithLeftShift(self, other=None, shift=None)
        self.countMatchesWithRightShift = DNA.countMatchesWithRightShift(self, other=None, shift=None)
        self.isValid = DNA.isValid(self)
        self.letterCount = DNA.letterCount(self, ch=None)
        self.matches = DNA.matches(self, c1=None, c2=None)

    # teste CreateComplement
    def test_createComplement(self):
        self.assertEqual(str(self.createComplement("TCTCGTA")), "TCTCGTA")

    # teste findMatchesWithLeftShift
    def test_findMatchesWithLeftShift(self):
        self.assertEqual(str(self.findMatchesWithLeftShift), "TCaT")

    # teste findMatchesWithRightShift
    def test_findMatchesWithRightShift(self):
        self.assertEqual(str(self.findMatchesWithRightShift), "tcaT")

    # teste findMaxPossibleMatches
    def test_findMaxPossibleMatches(self):
        self.assertEqual(self.findMaxPossibleMatches, 3)

    # teste countMatchesWithLeftShift
    def test_countMatchesWithLeftShift(self):
        self.assertEqual(self.countMatchesWithLeftShift, 3)

    # teste countMatchesWithRightShift
    def test_countMatchesWithRightShift(self):
        self.assertEqual(self.countMatchesWithRightShift, 3)

    # teste isValid
    def test_isValid(self):
        self.assertEqual(self.isValid, True)

    # teste letterCount
    def test_letterCount(self):
        self.assertEqual(self.letterCount, 3)

    # teste matches
    def test_matches(self):
        self.assertEqual(self.matches, True)


if __name__ == '__main__':
    unittest.main()




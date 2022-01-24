import unittest
from translator import frenchToEnglish
from translator import englishToFrench


class Testtranslator(unittest.TestCase): 
    def test_french_To_English(self): 
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)
        self.assertEqual(frenchToEnglish('Je vous remercie'), 'Thank you.')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')


class Testtranslator2(unittest.TestCase): 
    def test_english_To_French(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Thank you'), 'Je vous remercie')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
        

unittest.main()
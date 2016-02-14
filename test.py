import unittest
import numLib

class NumLibTesting(unittest.TestCase):
    def test_numToWords(self):
            self.assertEqual(numLib.numToWords(1000001), 'one million one')
            self.assertEqual(numLib.numToWords(0), 'zero')
            self.assertEqual(numLib.numToWords(1), 'one')
            self.assertEqual(numLib.numToWords(11), 'eleven')
            self.assertEqual(numLib.numToWords(25), 'twenty five')
            self.assertEqual(numLib.numToWords(50), 'fifty')
            self.assertEqual(numLib.numToWords(75), 'seventy five')
            self.assertEqual(numLib.numToWords(100), 'one hundred')
            self.assertEqual(numLib.numToWords(1000001), 'one million one')
            self.assertEqual(numLib.numToWords(114), 'one hundred fourteen')
            self.assertEqual(numLib.numToWords(150), 'one hundred fifty')
            self.assertEqual(numLib.numToWords(164), 'one hundred sixty four')
            self.assertEqual(numLib.numToWords(1234), 'one thousand two hundred thirty four')
            self.assertEqual(numLib.numToWords(10000), 'ten thousand')
            self.assertEqual(numLib.numToWords(10050), 'ten thousand fifty')
            self.assertEqual(numLib.numToWords(250000), 'two hundred fifty thousand')
            self.assertEqual(numLib.numToWords(500000), 'five hundred thousand')
            self.assertEqual(numLib.numToWords(256186), 'two hundred fifty six thousand one hundred eighty six')
            self.assertEqual(numLib.numToWords(46250), 'fourty six thousand two hundred fifty')
                  
if __name__ == '__main__':
    unittest.main()
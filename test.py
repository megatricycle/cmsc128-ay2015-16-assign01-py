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
            
    def test_wordsToNum(self):
        self.assertEqual('one million one', 1000001)
        self.assertEqual('zero', 0)
        self.assertEqual('one', 1)
        self.assertEqual('eleven', 11)
        self.assertEqual('twenty five' , 25)
        self.assertEqual('fifty', 50)
        self.assertEqual('seventy five', 75)
        self.assertEqual('one hundred', 100)
        self.assertEqual('one hundred fourteen', 114)
        self.assertEqual('one hundred fifty', 150)
        self.assertEqual('one hundred sixty four', 164)
        self.assertEqual('one thousand two hundred thirty four', 1234)
        self.assertEqual('ten thousand', 10000)
        self.assertEqual('ten thousand fifty', 10050)
        self.assertEqual('two hundred fifty thousand', 250000)
        self.assertEqual('five hundred thousand', 500000)
        self.assertEqual('two hundred fifty six thousand one hundred eighty six', 256186)
        self.assertEqual('fourty six thousand two hundred fifty', 46250)
                  
if __name__ == '__main__':
    unittest.main()
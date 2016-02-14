# numLib
numLib, a library for trivial number functions

## How to use
Paste numLib.py to your python project directory and import it.
```python
import numLib

print numLib.numToWords(1) ## one
print numLib.wordsToNum('one') ## 1
print numLib.wordsToCurrency('one', 'PHP') ## PHP1
print numLib.numberDelimited(50000, ',', 3) ## 50,000
```

## Testing
This library was developed with Test-Driven Development in mind. Run `python test.py` to ensure the program correctness.

## API
### numToWords(input)
Converts a given integer into word form.
### wordsToNum(input)
Converts a given number in word form to integer.
### wordsToCurrency(input, prefix)
Converts a given number in word form to integer and prefixes a currency value.
### numberDelimited(input, delimiter, offset)
Converts a given integer to a delimited version with offset.

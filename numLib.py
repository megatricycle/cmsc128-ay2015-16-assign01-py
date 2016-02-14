##############################################
# numLib, a library for trivial number functions
# Peter Bernard M. Rupa
##############################################

def numToWords(input):
    x = input
    
    # define keywords
    numberKeywords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    firstTensKeywords = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    tensKeywords = [None, 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    result = []
    
    while x >= 0:
        if x >= 1000000:
            # append to result the millionth number + million
            result.append(numberKeywords[x / 1000000])
            result.append('million')
            
            # remove first digit
            x -= x / 1000000 * 1000000
            
        elif x >= 10000:
            # append to result the thousandth number + thousand
            result.append(numToWords(x / 1000));
            
            result.append('thousand');
            
            # remove first digit
            x -= x / 1000 * 1000;
            
        elif x >= 1000:
            # append to result the thousandth number + thousand
            result.append(numberKeywords[x / 1000]);
            result.append('thousand');
            
            # remove first digit
            x -= x / 1000 * 1000;
            
        elif x >= 100:
            # append to result the hundreth number + hundred
            result.append(numberKeywords[x / 100]);
            result.append('hundred');
            
            # remove first digit
            x -= x / 100 * 100;
            
        elif x >= 20:
            # append to result the word form of x
            result.append(tensKeywords[x / 10]);
            
            # remove first digit
            x -= x / 10 * 10;
            
        elif x >= 10:
            # append to result the word form of x
            result.append(firstTensKeywords[x - 10]);
            
            # remove first digit
            x -= x / 10 * 10;
            break;
            
        elif x >= 0:
            # ones form
            if x != 0 or len(result) == 0:
                result.append(numberKeywords[x]);
            break;
    
    # stringify list
    return ' '.join(result)
    
def wordsToNum(input):
    return
    
def wordsToCurrency(input, prefix):
    return
    
def numberDelimited(input, delimiter, offset):
    return
###########################################################
# numLib, a library for trivial number functions
# Peter Bernard M. Rupa
###########################################################

###########################################################
# numToWords
#   - converts a given integer to its word form in english
# 
# parameters:
#  input (integer)
#
# return value: (string)
###########################################################

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
            result.append(numToWords(x / 1000))
            
            result.append('thousand')
            
            # remove first digit
            x -= x / 1000 * 1000
            
        elif x >= 1000:
            # append to result the thousandth number + thousand
            result.append(numberKeywords[x / 1000])
            result.append('thousand')
            
            # remove first digit
            x -= x / 1000 * 1000
            
        elif x >= 100:
            # append to result the hundreth number + hundred
            result.append(numberKeywords[x / 100])
            result.append('hundred')
            
            # remove first digit
            x -= x / 100 * 100
            
        elif x >= 20:
            # append to result the word form of x
            result.append(tensKeywords[x / 10])
            
            # remove first digit
            x -= x / 10 * 10
            
        elif x >= 10:
            # append to result the word form of x
            result.append(firstTensKeywords[x - 10])
            
            # remove first digit
            x -= x / 10 * 10
            break
            
        elif x >= 0:
            # ones form
            if x != 0 or len(result) == 0:
                result.append(numberKeywords[x])
            break
    
    # stringify list
    return ' '.join(result)
    
###########################################################
# wordsToNum
#   - converts a given number in its word form to integer
# 
# parameters:
#  input (string)
#
# return value: (integer)
###########################################################
    
def wordsToNum(input):
    # define keywords
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',' fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tensNumbers = [None, 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    
    # split by words
    words = input.split(' ')
    
    result = []
    
    # iterate per word
    for i in range(0, len(words)):
        # if "ones" word
        if (numbers.count(words[i]) > 0):
            # if previous is a "tens" word
            if (i > 0 and tensNumbers.count(words[i - 1]) > 0):
                result[-1] += numbers.index(words[i])
            else:
                result.append(numbers.index(words[i]))
                
        # if "tens" word
        elif (tensNumbers.count(words[i]) > 0):            
            result.append(tensNumbers.index(words[i]) * 10)
        
        # modifiers
        elif (words[i] == 'hundred'):
            result[-1] *= 100
        
        elif (words[i] == 'thousand'):
            # case hundred thousand
            if (len(result) > 1 and result[len(result) - 2] >= 100 and result[len(result) - 2] < 1000):
                result[len(result) - 2] += result[-1]
                result[len(result) - 2] *= 1000
                result = result[:-1]
                
            else:
                result[-1] *= 1000
        
        elif (words[i] == 'million'):
            result[-1] *= 1000000
    
    # get the sum of all items in the result list
    total = 0
    
    for num in result:
        total += num
    
    return total
    
###########################################################
# wordsToCurrency
#   - converts the given number in word form to integer and prefixes a currency value
# 
# parameters:
#  input (string)
#  prefix (string)
#
# return value: (string)
###########################################################
    
def wordsToCurrency(input, prefix):
    return prefix + str(wordsToNum(input))
    
###########################################################
# numberDelimited
#   - converts the given integer to a delimited version, with a given offset
# 
# parameters:
#  input (integer)
#  delimiter (string)
#  offset (integer)
#
# return value: (string)
###########################################################
    
def numberDelimited(input, delimiter, offset):
    # reverse input string
    x = str(input)[::-1]
    
    result = ''
    
    for i in range(0, len(x)):
        # add delimiter if index is divisible by offset
        if(i % offset == 0 and i != 0):
            result += delimiter + x[i]
            
        else:
            result += x[i]
    
    # reverse result string
    result = result[::-1]
    
    return result



def makeNumberPretty(number):
    return  ("{:,}".format(number))

def numberToWord(numberValue):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if numberValue < 0:
        return "minus "+numberToWord(-numberValue)

    if numberValue < 20:
        return  units[numberValue] 

    if numberValue < 100:
        return  tens[numberValue // 10]  +units[int(numberValue % 10)] 

    if numberValue < 1000:
        return units[numberValue // 100]  +"hundred " +numberToWord(int(numberValue % 100))

    if numberValue < 1000000: 
        return  numberToWord(numberValue // 1000) + "thousand " + numberToWord(int(numberValue % 1000))

    if numberValue < 1000000000:    
        return numberToWord(numberValue // 1000000) + "million " + numberToWord(int(numberValue % 1000000))
    
    if numberValue < 1000000000000:    
        return numberToWord(numberValue // 1000000000) + "billion " + numberToWord(int(numberValue % 1000000000))

    return numberToWord(numberValue // 1000000000000)+ "trillion "+ numberToWord(int(numberValue % 1000000000000))

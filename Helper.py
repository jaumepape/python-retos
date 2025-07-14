def isArmstrong(integer):
    digitsCount = len(str(integer))
    result = 0
    for digit in str(integer):
        result = result + int(digit) ** digitsCount
    if result == integer:
        return True
    else:
        return False

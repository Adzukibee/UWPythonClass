
# -- data code -- #
fltValue1 = None  # first argument
fltValue2 = None  # second argument

# -- Processing Code -- #
def CalculateValues(value1, value2):
    fltAdd = value1 + value2
    fltSub = abs(value1 - value2)
    fltMul = value1 * value2
    fltDiv = value1 / value2
    return fltAdd, fltSub, fltMul, fltDiv

# -- Presentation -- #
fltValue1 = float(input('Enter the first value: '))
fltValue2 = float(input('Enter the second value: '))
fltAdd, fltSub, fltMul, fltDiv = CalculateValues(fltValue1, fltValue2)
print('The Sum of %.2f and %.2f is %.2f' % (fltValue1, fltValue2, fltAdd))
print('The Difference of %.2f and %.2f is %.2f' % (fltValue1, fltValue2, fltSub))
print('The Product of %.2f and %.2f is %.2f' % (fltValue1, fltValue2, fltMul))
print('The Quotient of %.2f and %.2f is %.2f' % (fltValue1, fltValue2, fltDiv))
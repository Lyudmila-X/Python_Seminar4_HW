# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def degree(digit, deg):
    indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }
    degrees = ""
    temp = str(deg)
    for char in temp:
        degrees += indexes[char] or ""
    return str(digit) + degrees

k = int(input("Please enter the degree of the polynomial: "))
d = k+1
coefficients = [randint(0, 101) for i in range(d)]
# coefficients = [0, 1, 2, 0, 1, 12] - для проверки нестандартных коэффициентов
formula = ""
for i in range(d):
    if coefficients[i] != 0:
        if k==0:
            formula = formula + str(coefficients[i])
        elif k==1 and coefficients[i] ==1:
            formula = formula + "x"
        elif k!=1 and coefficients[i] ==1:
            formula = formula + str(degree("x", k))
        elif k==1 and coefficients[i] !=1:
            formula = formula + str(coefficients[i]) + "*" + "x"
        else:
            formula = formula + str(coefficients[i]) + "*" + str(degree("x", k))
        k-=1
        if i < d-1: 
            formula = formula + "+"
    else:
        k-=1
formula = formula + "=" + "0"
data = open('file.txt', 'wb')
data.write(formula.encode('utf-8'))
data.close

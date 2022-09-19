# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь(БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

n = int(input("Please input the number of decimal places you want to display: "))
count = 0
pinum = 0
k = 0
while (count - n) <0 or k<50:
    count = len(str(pinum%1))-2
    oop = (1/16**k)*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6)))
    pinum = pinum + (1/16**k)*((4/(8*k+1))-(2/(8*k+4))-(1/(8*k+5))-(1/(8*k+6)))
    k+=1
print (round(pinum,n))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

seq = [int (el) for el in (input("Please enter the sequence elements using a space: ").split(" "))]
print (seq)
lenseq = len(seq)
for i in range(lenseq-1):
    print (f"i = {i}")
    for j in range(lenseq-1, i, -1):
        print(j)
        if seq[i] == seq[j]:
            seq.pop(j)
            lenseq-=1
        
print (seq)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def polynomial_split (data: str):
    data = data[:data.find("=")]
    arr = data.split("+")
    return arr

def poly_mono_dict (arr):
    slovar = {}
    for item in arr:
        if "x" in item:
            if "*" in item:
                slovar[item[item.find("x"):]] = int(item[:item.find("*")])
            else:
                slovar[item[item.find("x"):]] = 1
        else:
            slovar["0"] = int(item)
    return slovar

data1 = open("file1.txt", "rb")
data2 = open("file2.txt", "rb")
arr1 = polynomial_split(str(data1.read().decode('utf-8')))
arr2 = polynomial_split(str(data2.read().decode('utf-8')))
poly1 = poly_mono_dict(arr1)
poly2 = poly_mono_dict(arr2)
poly3 = poly1.copy()
poly3.update(poly2)
res = {}
for key in poly3:
    try:
        res[key]= poly1[key] + poly2[key]
    except KeyError:
        res[key] = poly3[key]

fin_string = ''
for key in res:
    if key == '0':
        fin_string = fin_string + str(res[key])
    elif res[key] ==1:
        fin_string = fin_string + str(key)+ "+"
    else:
        fin_string = fin_string + str(res[key]) + "*" + str(key)+ "+"
fin_string= fin_string + "=" + "0"

result = open("result.txt", "wb")

result.write(fin_string.encode('utf-8'))
data1.close
data2.close
result.close

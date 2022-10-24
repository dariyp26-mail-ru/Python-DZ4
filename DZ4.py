# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8

def poly(nameFile):
    openFile = open(nameFile, 'r', encoding='utf8')
    polynom01 = openFile.read()
    openFile.close

    polynom1 = polynom01.replace('-', '+-').replace(' ', '').split('+')

    if polynom1[0] == '':
        del polynom1[0]

    print(polynom1)

    for i in polynom1:
        if 'x^2' in i:
            if i == 'x^2':
                i = '1'
            elif i == '-x^2':
                i = '-1'
            result[0] += int(i.replace('x^2', ''))
        elif 'x' in i:
            if i == 'x':
                i = '1'
            elif i == '-x':
                i = '-1'
            result[1] += int(i.replace('x', ''))
        else:
            result[2] += int(i)


result = [0, 0, 0]
znak = ['+', '+', '+']
poly('polynomial1.txt')
poly('polynomial2.txt')
print(result)
for i in 0, 1, 2:
    if result[i] < 0:
        znak[i] = '-'

format = '{0}x^2+{1}x+{2} '.format(result[0],result[1],result[2]).replace('+-', '-').replace('0x^2', '').replace('1x^2', 'x^2').replace('+0x', '').replace('1x', 'x').replace('+0', '')

print(format)

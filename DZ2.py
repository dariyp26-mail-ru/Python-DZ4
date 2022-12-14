# Задача 2. В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»

""" data = open('ice.txt', 'w', encoding='utf8')
data.write('«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»\n«Сливочное», «Вафелька», «Сладкоежка»')
data.close() """

with open('ice.txt', 'r', encoding='utf8') as unknown:
    assortment = set(unknown.readline().rstrip().split(', '))
    current = set(unknown.readline().rstrip().split(', '))
    print(f'Закончилось:', *assortment - current)
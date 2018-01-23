'''Определить четверть координатной плоскости по координатам x и y. Применить минимум два разных подхода в указании условий'''

x = int(input('X: '))
y = int(input('Y: '))
if x > 0:
    if y > 0:
        print('1 quart')
    elif y == 0:
        print('on +X line')
if y < 0:
    if x > 0:
        print('2 quart')
    elif x == 0:
        print('on -Y line')
if x < 0:
    if y < 0:
        print('3 quart')
    elif y == 0:
        print('on -X line')
if y > 0:
    if x < 0:
        print('4 quart')
    elif x == 0:
        print('on +Y line')
if x == 0 and y == 0:
    print('Center of corrdinates')
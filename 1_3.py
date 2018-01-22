import math

a = float(input('Введите длину одного из катетов: '))
b = float(input('Введите другой: '))
c = math.pow(a, 2) + math.pow(b, 2)
print('Гипотенуза прямоугльного |_\ =', math.sqrt(c))



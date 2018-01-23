'''3. Проверить, что хотя бы одно из чисел a или b оканчивается на 0.'''

a = int(input('Введите число A: '))
#b = int(input('Введите число B: '))

if (a >= 10) and (a % 10 == 0):
    print("ноль, естЬ! {}".format(a))
else:
    print("Без нулей {}".format(a))



'''
if (a >= 10) and (a % 10 == 0):
    print(" ноль, естЬ! {}".format(a))
else:
    print("A Без нулей {}".format(a))
'''
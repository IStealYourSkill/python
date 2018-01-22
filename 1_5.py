import math

a = int(input('Сколько минут прошло с начала суток: '))
h = math.floor(a/60)
m =  a - h * 60
d = math.floor(h/24)
z = d * 24 - h
print(d, 'day', abs(z),':', m)



#a = int(input('Сколько минут прошло с начала суток: '))
#h = math.floor((1439 - a)/60)
#m =  1439 - (h * 60) - a

#print(h, m)

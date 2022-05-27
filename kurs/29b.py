"""29В 1500 баллов"""

"""l = float(input("Расстояние между а и б "))
d = float(input("Расстояние между а и светофором "))
v = float(input("Скорость машины "))
g = int(input("Время зеленого "))
r = int(input("Время красного "))"""

l, d, v, g, r = map(int, input().split())

s = 0
z = 0
f = 0

t = d/v

while t>=s:
    s+=g
    if s>t:
        z = 1
        break
    s+=r
    if s>=t:
        f = 1
        break

if z==1:
    t = l/v
    print(t)

if f ==1:
    s = t
    while s>0:
        s-=g
        s-=r
    t = d/v + abs(s) + (l-d)/v
    print(t)




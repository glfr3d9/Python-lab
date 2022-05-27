"""16С 1800 баллов"""

print("Размер до ")
a = float(input())
b = float(input())
print("Размер после ")
x= int(input())
y= int(input())


if a>x and b>y:
    if a%x == 0 and b%y==0:
        print(int(a), int(b))
    elif a%x!=0 and b%y==0:
        a = x*(b//y)
        print(a,b)
    elif a%x == 0 and b%y!=0:
        b = y * (a//x)
        print(int(a), int(b))

    elif a%x!=0 and b%y!=0:
        while a%x!=0:
            a-=1
        if a <= 0:
            print(0, 0)
        b = y * a//x
        print(int(a), int(b))
else:
    print(0, 0)

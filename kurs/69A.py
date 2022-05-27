"""69А 1000 баллов"""

n = int(input())
a = []

for i in range(n):
    a.append([int(j) for j in input().split()])
x = 0
y = 0
z = 0
count = 0
while count<n:
    for i in range (len(a)):
        x+=a[i][0]
        y+=a[i][1]
        z+=a[i][2]
        count+=1
if x == 0 and y==0 and z ==0:
    print("YES")
else:
    print("NO")


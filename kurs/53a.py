"""53А 1100 баллов"""

a = input()
n = int(input())

d = []
f = []

for i in range(n):
  d.append(input().lower())

for i in range(len(d)):
  s = d[i]
  k = 0
  lenght = len(d[i])
  if (len(a)<lenght):
    lenght = len(a)

  for j in range(lenght):
    if a[j] == s[j]:
      k+=1

  if k == len(a):
    f.append(d[i])

if len(f)==0:
  print(a)
else:
  l = f[0]
  for i in range(len(f)):
    if f[i] < l:
      l = f[i]
  print(l)
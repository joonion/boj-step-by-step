n = int(input())
a = [*map(int, input().split())]
v = int(input())
c = 0
for i in range(n):
    if a[i] == v:
        c += 1
print(c)
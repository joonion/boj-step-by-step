a = sorted(list(map(int, input().split())))
s = set(a)
if len(s) == 1:
    print(10000 + a[0] * 1000)
elif len(s) == 2:
    print(1000 + a[1] * 100)
else:
    print(a[2] * 100)
h, m = map(int, input().split())
if m >= 45:
    print(h, m - 45)
else:
    h = (h - 1) % 24
    m = (m - 45) % 60
    print(h, m)
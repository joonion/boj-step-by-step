a, b = map(int, input().split())
c = int(input())
h = a + c // 60
m = b + c % 60
if m >= 60:
    h += 1
    m %= 60
print(h % 24, m)
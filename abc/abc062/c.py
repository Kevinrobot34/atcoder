h, w = map(int, input().split())

def split_into_two(x, y):
    if x % 2 == 0 or y % 2 == 0:
        return x*y//2, x*y//2
    else:
        if x > y:
            x, y = y, x
        return (y//2)*x, (y//2 + 1)*x

ans = h * w
for i in range(1, h//2+2):
    s0 = w*i
    s1, s2 = split_into_two(h - i, w)
    ans = min(ans, max(s0, s1, s2) - min(s0, s1, s2))

for i in range(1, w//2+2):
    s0 = h*i
    s1, s2 = split_into_two(h, w - i)
    ans = min(ans, max(s0, s1, s2) - min(s0, s1, s2))

print(ans)

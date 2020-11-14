n = int(input())
UNIT = 5
m = 24 * 60 // UNIT + 1
imos = [0] * (m + 1)

for _ in range(n):
    a, b = map(int, input().split('-'))
    a = a % 100 + (a // 100) * 60
    b = b % 100 + (b // 100) * 60
    imos[a // UNIT] += 1
    imos[(b + UNIT - 1) // UNIT] += -1

for i in range(m):
    imos[i + 1] += imos[i]

imos.append(0)
l = 0
while imos[l] == 0:
    l += 1

# print(imos)
for i in range(l + 1, len(imos)):
    if imos[i] > 0 and imos[i - 1] == 0:
        l = i
    if imos[i] == 0 and imos[i - 1] > 0:
        l_hm = f'{l * 5 // 60:02}{l * 5 % 60:02}'
        r_hm = f'{i * 5 // 60:02}{i * 5 % 60:02}'
        print(f'{l_hm}-{r_hm}')

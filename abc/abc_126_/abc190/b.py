n, s, d = map(int, input().split())
attack = 0
for _ in range(n):
    xi, yi = map(int, input().split())
    if xi < s and yi > d:
        attack += 1
ans = 'Yes' if attack > 0 else 'No'
print(ans)

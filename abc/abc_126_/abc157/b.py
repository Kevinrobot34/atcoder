a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())

for i in range(n):
    b = int(input())
    for r in range(3):
        for c in range(3):
            if a[r][c] == b:
                a[r][c] = 0

is_bingo = False
for i in range(3):
    if sum([a[i][j] for j in range(3)]) == 0:
        is_bingo = True
        break
    if sum([a[j][i] for j in range(3)]) == 0:
        is_bingo = True
        break

if sum([a[j][j] for j in range(3)]) == 0:
    is_bingo = True
if sum([a[j][2 - j] for j in range(3)]) == 0:
    is_bingo = True

ans = 'Yes' if is_bingo else 'No'
print(ans)

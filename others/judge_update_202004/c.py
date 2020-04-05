from itertools import permutations
a = list(map(int, input().split()))


def check(b):
    for i in range(3):
        for j in range(1, a[i]):
            if b[i][j] <= b[i][j - 1]:
                return False
    for j in range(a[1]):
        if b[0][j] >= b[1][j]:
            return False
    for j in range(a[2]):
        if b[1][j] >= b[2][j]:
            return False

    return True


n = sum(a)
ans = 0
for perm in permutations(range(1, n + 1)):
    b = [perm[:a[0]], perm[a[0]:a[0] + a[1]], perm[a[0] + a[1]:]]
    if check(b):
        ans += 1

print(ans)

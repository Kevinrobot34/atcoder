n, m = map(int, input().split())

relation = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    relation[x][y] = relation[y][x] = True


def check(target_people):
    for i in target_people:
        for j in target_people:
            if i == j:
                continue

            if not relation[i][j]:
                return False
    return True


ans = 1
for bit in range(1 << n):
    target_people = []
    for i in range(n):
        if (bit >> i) & 1:
            target_people.append(i)

    if check(target_people):
        ans = max(ans, len(target_people))

print(ans)

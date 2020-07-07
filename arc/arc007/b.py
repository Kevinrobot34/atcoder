n, m = map(int, input().split())
case = list(range(n + 1))

for _ in range(m):
    disk = int(input())
    idx = case.index(disk)
    case[0], case[idx] = case[idx], case[0]

print(*case[1:], sep='\n')

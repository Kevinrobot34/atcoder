h, n = map(int, input().split())
magic = [tuple(map(int, input().split())) for _ in range(n)]
magic.sort(key=lambda x: x[0] / x[1], reverse=True)
print(*magic, sep='\n')

ans = (h // magic[0][0]) * magic[0][1]
h %= magic[0][0]

magic.sort(key=lambda x: ((h + x[0] - 1) // x[0]) * x[1])

print(ans)

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
info.sort()

cnt = 0
idx = -1
while cnt < k:
    idx += 1
    cnt += info[idx][1]

print(info[idx][0])

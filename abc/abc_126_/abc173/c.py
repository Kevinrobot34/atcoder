h, w, k = map(int, input().split())
c = [input() for _ in range(h)]

ans = 0
for bit_h in range(1 << h):
    for bit_w in range(1 << w):
        cnt = 0
        for i in range(h):
            for j in range(w):
                if (bit_h >> i) & 1 == 1 or (bit_w >> j) & 1 == 1:
                    continue
                if c[i][j] == '#':
                    cnt += 1
        if cnt == k:
            ans += 1

print(ans)

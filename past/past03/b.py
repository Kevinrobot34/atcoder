n, m, q = map(int, input().split())
cnt = [0] * m
is_solved = [[False] * m for _ in range(n)]

for _ in range(q):
    query = input()
    if query[0] == '1':
        _, i = map(int, query.split())
        i -= 1
        ans = sum(n - cnt[j] for j in range(m) if is_solved[i][j])
        # print(cnt)
        # print(*is_solved, sep='\n')
        print(ans)
    else:  # query[0] == '2':
        _, i, j = map(int, query.split())
        i -= 1
        j -= 1
        is_solved[i][j] = True
        cnt[j] += 1

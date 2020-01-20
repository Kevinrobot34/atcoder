n, m = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(n)]
checkpoints = [list(map(int, input().split())) for _ in range(m)]

def dist(si, cj):
    return abs(students[si][0] - checkpoints[cj][0]) + abs(students[si][1] - checkpoints[cj][1])

ans = []
for i in range(n):
    ans_i = 0
    for j in range(1, m):
        if dist(i, ans_i) > dist(i, j):
            ans_i = j
    ans.append(ans_i+1)

print(*ans, sep='\n')

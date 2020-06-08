from collections import deque
h, w = map(int, input().split())
grid = [['@'] * (w+2)] + [[] for i in range(h)] + [['@'] * (w+2)]
for i in range(1, h+1):
    grid_i = input()
    grid[i].append('@')
    for j in range(w):
        if grid_i[j] == 's':
            si, sj = i, j+1
            grid[i].append('@')
        elif grid_i[j] == 'g':
            gi, gj = i, j+1
            grid[i].append('.')
        else:
            grid[i].append(grid_i[j])
    grid[i].append('@')

# print(si, sj)
# print(gi, gj)
# print('\n'.join([''.join(grid_i) for grid_i in grid]))

queue = deque([(si, sj, 2)])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = False
while queue:
    ci, cj, cc = queue.popleft()
    if ci == gi and cj == gj:
        ans = True
        break

    for k in range(4):
        ni = ci + dx[k]
        nj = cj + dy[k]
        if grid[ni][nj] == '.':
            grid[ni][nj] = cc
            queue.append((ni, nj, cc))
        elif grid[ni][nj] == '#' and cc > 0:
            for k2 in range(4):
                nni = ni + dx[k2]
                nnj = nj + dy[k2]
                if grid[nni][nnj] == '.':
                    grid[nni][nnj] = cc-1
                    queue.append((nni, nnj, cc-1))
                elif isinstance(grid[nni][nnj], int) and grid[nni][nnj] < cc-1:
                    grid[nni][nnj] = cc-1
                    queue.append((nni, nnj, cc-1))
                elif grid[nni][nnj] == '#' and cc > 1:
                    for k3 in range(4):
                        nnni = nni + dx[k3]
                        nnnj = nnj + dy[k3]
                        if grid[nnni][nnnj] == '.':
                            grid[nnni][nnnj] = cc-2
                            queue.append((nnni, nnnj, cc-2))
        elif isinstance(grid[ni][nj], int) and grid[ni][nj] < cc:
            grid[ni][nj] = cc
            queue.append((ni, nj, cc))

if ans:
    print("YES")
else:
    print("NO")

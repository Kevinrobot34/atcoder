from itertools import combinations


def simple_ccw(pa, pb, pc):
    # Simple Counterclockwise test
    ax, ay = pa
    bx, by = pb
    cx, cy = pc

    vx, vy = bx - ax, by - ay
    wx, wy = cx - ax, cy - ay
    return vx * wy - vy * wx == 0


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

is_parallel = False
for pi, pj, pk in combinations(points, 3):
    if simple_ccw(pi, pj, pk):
        is_parallel = True
        break

ans = 'Yes' if is_parallel else 'No'
print(ans)

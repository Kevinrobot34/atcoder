n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

def main():
    for cx in range(101):
        for cy in range(101):
            for xi, yi, hi in info:
                if hi > 0:
                    h = abs(xi - cx) + abs(yi - cy) + hi
                    break

            success = True
            for xi, yi, hi in info:
                if hi != max(h - abs(xi - cx) - abs(yi - cy), 0):
                    success = False
                    break

            if success:
                print(cx, cy, h)
                return

main()

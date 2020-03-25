l, h = map(int, input().split())
n = int(input())
for _ in range(n):
    a = int(input())
    if a < l:
        ans_i = l - a
    elif a <= h:
        ans_i = 0
    else:
        ans_i = -1

    print(ans_i)

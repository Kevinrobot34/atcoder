n = int(input())
a = list(map(int, input().split()))
a_set = set()

for ai in a:
    while ai % 2 == 0:
        ai = ai >> 1
    a_set.add(ai)

ans = len(a_set)
print(ans)

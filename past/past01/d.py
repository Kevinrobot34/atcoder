from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]

if len(set(a)) == n:
    print('Correct')
else:
    cnt = Counter(a)
    x = cnt.most_common(1)[0][0]
    y = list(set(list(range(1, n + 1))) - set(a))[0]
    print(x, y)

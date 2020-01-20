from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
a.sort()


i = bisect_left(a, a[-1]/2)
if i > 0:
    if abs(a[-1]/2 - a[i]) < abs(a[-1]/2 - a[i-1]):
        print(a[-1], a[i])
    else:
        print(a[-1], a[i-1])
else:
    print(a[-1], a[i])

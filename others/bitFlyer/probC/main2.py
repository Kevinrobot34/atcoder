import bisect

n, d = map(int, input().split())
x = list(map(int, input().split()))

print(d)
print(x)
ans = 0

for i in range(n):
    j_max = bisect.bisect_right(x, x[i]+d)
    print('i:{} {}'.format(i, x[i])
    for j in range(i+1, j_max):
        print('j: ', j, x[j])
# for j in range(n):
#     k1 = bisect.bisect_right(x, x[j]+d)
#     i = bisect.bisect_right(x, x[j]-d)
#     for a in range(j-i):
#         k2 =
#     print(i, j, k)
#     print('j-k:{}'.format(x[j+1:k]))
#     print('i-j:{}'.format(x[i:j]))
#     ans += (j-i) * (k-j-1)

print(ans)

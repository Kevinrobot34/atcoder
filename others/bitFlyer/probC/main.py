import bisect

n, d = map(int, input().split())
x = list(map(int, input().split()))

#print(d)
#print(x)
ans = 0

#y = [bisect.bisect_right(x, x[i]+d) if x[i]+d < x[-1] else n for i in range(n)]
y = []
a = 0
for i in range(n):
    while a < n and x[i] + d >= x[a]:
        a += 1
    y.append(a)

z = [0]
for i in range(n):
    z.append(z[-1]+y[i])

for i in range(n):
    #j_max = bisect.bisect_right(x, x[i]+d)
    j_max = y[i]
    #print('i:[{}] {}'.format(i, x[i]))

    #ans += sum(y[i+1: j_max]) - y[i]*(j_max-i-1)
    ans += z[j_max] - z[i+1] - y[i]*(j_max-i-1)
    #for j in range(i+1, j_max):
        #print('   j:[{}] {}'.format(j, x[j]))
        #k1 = bisect.bisect_right(x, x[i]+d)
        #k2 = bisect.bisect_right(x, x[j]+d)
        #k1 = y[i]
        #k2 = y[j]
        #print('      k1:[{}]'.format(k1))
        #print('      k2:[{}]'.format(k2))
        #print('      ', x[k1:k2])
        #ans += k2-k1

print(ans)

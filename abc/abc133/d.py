n = int(input())
a = list(map(int, input().split()))

m = (n-1) // 2
s = sum(a) // 2
x = [sum([a[(0+1 + j*2)%n] for j in range(m)]), sum([a[(1+1 + j*2)%n] for j in range(m)])]
ans = []
for i in range(n):
    index = i % 2
    ans.append(s - x[index])
    x[index] = x[index] - a[(i+1 + 0*2)%n] + a[(i+1 + m*2)%n]

print(" ".join([str(a*2) for a in ans]))

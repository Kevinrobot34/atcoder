n, q = map(int, input().split())

othello = [0] * (n+1)

for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    othello[l] += 1
    othello[r] -= 1

for i in range(n):
    othello[i+1] += othello[i]

print(''.join([str(othello[i] % 2) for i in range(n)]))

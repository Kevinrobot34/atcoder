n = int(input())

k = 55555
eratos = [0 for i in range(k+1)]
prime = []
prime_bool = {}
for i in range(2, k+1):
    if eratos[i] == 1:
        prime_bool[i] = 0
        continue
    prime.append(i)
    prime_bool[i] = 1
    for j in range(2, k+1):
        if i * j > k:
            break
        eratos[i*j] = 1

ans = []
m = 11
while len(ans) < n:
    if prime_bool[m] == 1 and m % 5 == 1:
        ans.append(m)

    m += 2

print(" ".join([str(a) for a in ans]))

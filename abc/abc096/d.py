n = int(input())

eratos = [0 for i in range(55555*5+1)]
prime = []
prime_bool = {}
for i in range(2, 55555*5+1):
    if eratos[i] == 1:
        prime_bool[i] = 0
        continue
    prime.append(i)
    prime_bool[i] = 1
    for j in range(2, 55555+1):
        if i * j > 55555*5:
            break
        eratos[i*j] = 1

ans = [2, 3, 5, 7, 11] + [0] * (n-5)

index = 5
for i in range(5, n):
    ans[i] = prime[index]
    while prime_bool[sum(ans[i+1-5:i+1])] == 1:
        index += 1
        ans[i] = prime[index]
    index += 1

print(" ".join([str(a) for a in ans]))

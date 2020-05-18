k = int(input())
fibo = [1] * (k + 2)
for i in range(2, k + 2):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[k + 1], fibo[k])

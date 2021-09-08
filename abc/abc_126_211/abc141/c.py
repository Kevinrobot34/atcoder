n, k, q = map(int, input().split())
a_sum = [0] * n
for i in range(q):
    a_i = int(input())
    a_i -= 1
    a_sum[a_i] += 1

# print(a_sum)
for i in range(n):
    if k - (q - a_sum[i]) > 0:
        print("Yes")
    else:
        print("No")

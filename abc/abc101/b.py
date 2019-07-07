n_s = input()
n = int(n_s)

s = 0
for i in range(len(n_s)):
    s += (n // (10**i)) % 10

if n % s == 0:
    print("Yes")
else:
    print("No")

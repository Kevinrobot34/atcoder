n = int(input())

m = n
f = 0
while m > 0:
    f += m % 10
    m = m // 10

if n % f == 0:
    print("Yes")
else:
    print("No")

n = int(input())

ans = []
b = 1
while n > 0:
    if n % (b * 2) == 1:
        ans.append(b)
    b *= 2
    n //= 2

print(len(ans))
print(*ans, sep='\n')

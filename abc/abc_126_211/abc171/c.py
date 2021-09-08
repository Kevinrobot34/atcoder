n = int(input())
n -= 1
ans = []
while True:
    # print(n)
    ans.append(chr(ord('a') + n % 26))
    n //= 26
    if n == 0:
        break
    else:
        n -= 1
ans = ans[::-1]
ans = ''.join(ans)
print(ans)

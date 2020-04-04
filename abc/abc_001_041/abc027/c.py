n = int(input())

n_bit = n.bit_length()
# print(n_bit)

if n_bit % 2 == 0:
    tak = 'left'
    aok = 'right'
else:
    tak = 'right'
    aok = 'left'

m = 1
cnt = 0
while m <= n:
    if cnt % 2 == 0:
        if tak == 'left':
            m = 2 * m
        else:
            m = 2 * m + 1
    else:
        if aok == 'left':
            m = 2 * m
        else:
            m = 2 * m + 1
    cnt += 1

# print(cnt)
ans = 'Aoki' if cnt % 2 == 1 else 'Takahashi'
print(ans)

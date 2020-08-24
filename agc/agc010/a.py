n = int(input())
a = list(map(int, input().split()))

n_odd = sum(ai % 2 for ai in a)
n_even = (n - n_odd) + n_odd // 2

if n_even > 0:
    if n_odd % 2 == 0:
        ans = 'YES'
    else:
        ans = 'NO'
else:
    if n_odd % 2 == 0:
        ans = 'NO'
    else:
        ans = 'YES'
print(ans)

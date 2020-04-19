n = int(input())

if n % 10 == 7:
    ans = 'Yes'
elif (n % 100) // 10 == 7:
    ans = 'Yes'
elif n // 100 == 7:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)

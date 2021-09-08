n = int(input())
if n % 10 in [2, 4, 5, 7, 9]:
    ans = 'hon'
elif n % 10 == 3:
    ans = 'bon'
else:
    ans = 'pon'
print(ans)

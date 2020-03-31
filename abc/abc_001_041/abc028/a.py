n = int(input())
if n < 60:
    ans = 'Bad'
elif n < 90:
    ans = 'Good'
elif n < 100:
    ans = 'Great'
else:
    # n == 100
    ans = 'Perfect'

print(ans)

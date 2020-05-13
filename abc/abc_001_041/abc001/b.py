m = int(input())

if m < 100:
    ans = '00'
elif 100 <= m <= 5000:
    ans = f'{m//100:02d}'
elif 6000 <= m <= 30000:
    ans = f'{m//1000 + 50:02d}'
elif 35000 <= m <= 70000:
    ans = f'{(m//1000 - 30)//5 + 80:02d}'
elif 70000 < m:
    ans = '89'

print(ans)

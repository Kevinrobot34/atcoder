x = int(input())

if 400 <= x < 600:
    ans = '8'
elif 600 <= x < 800:
    ans = '7'
elif 800 <= x < 1000:
    ans = '6'
elif 1000 <= x < 1200:
    ans = '5'
elif 1200 <= x < 1400:
    ans = '4'
elif 1400 <= x < 1600:
    ans = '3'
elif 1600 <= x < 1800:
    ans = '2'
elif 1800 <= x < 2000:
    ans = '1'

print(ans)

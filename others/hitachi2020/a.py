s = input()

ans = 'No'
for i in range(5):
    if s == 'hi' * (i + 1):
        ans = 'Yes'
        break
print(ans)

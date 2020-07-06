n = int(input())
cnt = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
for _ in range(n):
    si = input()
    cnt[si] += 1

print(f'AC x {cnt["AC"]}')
print(f'WA x {cnt["WA"]}')
print(f'TLE x {cnt["TLE"]}')
print(f'RE x {cnt["RE"]}')

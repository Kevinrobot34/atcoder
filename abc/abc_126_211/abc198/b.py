n = input().rstrip('0')
ans = 'Yes' if all(n[i] == n[len(n) - 1 - i] for i in range(len(n))) else 'No'
print(ans)

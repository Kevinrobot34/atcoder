n = int(input())
ng_list = [int(input()) for _ in range(3)]
ng_list.sort()

if n in ng_list:
    ans = "NO"
else:
    if ng_list[0] + 1 == ng_list[1] and ng_list[1] + 1 == ng_list[2]:
        ans = "NO"
    else:
        ans = "Yes"

print(ans)

n = int(input())

ans = "" if n!= 0 else "0"
while n != 0:
    if n % 2 == 0:
        ans = "0" + ans
    else:
        ans = "1" + ans
        n -= 1 # (-2)進数を右シフトを `n // (-2)` で出来るように1引いておく

    n = n // (-2) # (-2)進数を右シフト
print(ans)

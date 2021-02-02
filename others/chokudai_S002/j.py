def main():
    import sys
    input = sys.stdin.readline

    def get_divisor(n: int) -> list:
        divisor = []
        for i in range(1, n + 1):
            if i * i > n:
                break
            if n % i == 0:
                divisor.append(i)
                if n // i != i:
                    divisor.append(n // i)
        return divisor

    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in range(n)]

    cand = set(get_divisor(ab[0][0]) + get_divisor(ab[0][1]))
    ans = 1
    for ci in cand:
        if ci < ans:
            continue
        if all(aj % ci == 0 or bj % ci == 0 for aj, bj in ab):
            ans = max(ans, ci)
    print(ans)


main()

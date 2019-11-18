import sys
input = sys.stdin.readline


def query(a, b):
    if b > a:
        a, b = b, a
    # a <= b
    ab = a * b


q = int(input())
for i in range(n):
    a, b = map(int, input().split())
    ans_i = query(a, b)
    print(ans_i)

q, l = map(int, input().split())

queries = [input() for _ in range(q)]

size = 0
queue = []
is_safe = True
for s in queries:
    if s.startswith('Push'):
        _, n, m = s.split()
        n = int(n)
        m = int(m)
        if size > l - n:
            print('FULL')
            is_safe = False
            break
        queue.append((n, m))
        size += n
    elif s.startswith('Pop'):
        _, n = s.split()
        n = int(n)
        if size < n:
            print('EMPTY')
            is_safe = False
            break
        size -= n
        while queue and n >= queue[-1][0]:
            n0, _ = queue.pop()
            n -= n0

        if n > 0:
            n0, m0 = queue.pop()
            n0 -= n
            queue.append((n0, m0))
    elif s.startswith('Top'):
        if size == 0:
            print('EMPTY')
            is_safe = False
            break
        print(queue[-1][1])
    else:
        print(size)

if is_safe:
    print('SAFE')

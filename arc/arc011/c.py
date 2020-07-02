from heapq import heappush, heappop


def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n
    prev_node = [-1] * n  # previous node

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        dist2v, v_from = heappop(heap)
        if dist[v_from] < dist2v:
            continue
        for cost, v_to in graph[v_from]:
            dist_cand = dist2v + cost
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                prev_node[v_to] = v_from
                heappush(heap, (dist[v_to], v_to))
    return dist, prev_node


first, last = input().split()
n = int(input())
words = [input() for _ in range(n)]
words.append(first)
words.append(last)
words = sorted(list(set(words)))

n_words = len(words)
i_first = words.index(first)
i_last = words.index(last)
m = len(first)
graph = [[] for _ in range(n_words)]
for i in range(n_words):
    for j in range(i + 1, n_words):
        cnt = 0
        for k in range(m):
            if words[i][k] != words[j][k]:
                cnt += 1
        if cnt == 1:
            graph[i].append((1, j))
            graph[j].append((1, i))

INF = float('inf')
dist, prev_node = dijkstra(graph, n_words, i_first, INF)
if dist[i_last] == INF:
    print(-1)
elif dist[i_last] == 0:
    print(0)
    print(first)
    print(last)
else:
    ans = [i_last]
    while ans[-1] != i_first:
        ans.append(prev_node[ans[-1]])
    ans = ans[::-1]
    print(dist[i_last] - 1)
    for ans_i in ans:
        print(words[ans_i])

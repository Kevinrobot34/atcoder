from dataclasses import dataclass
from collections import deque
from typing import List
import sys
sys.setrecursionlimit(10**8)

n = int(input())
c = [list(input()) for _ in range(n)]
di = [+1, 0, -1, 0]
dj = [0, +1, 0, -1]


INF = float('inf')


@dataclass
class Edge:
    v_to: int
    cap: int
    rev: int


class Network:
    def __init__(self, n: int):
        self.n: int = n  # number of nodes
        self.graph: List[List[Edge]] = [[] for _ in range(n)]
        self.level: List[int] = [-1] * n

    def add_edge(self, v_from: int, v_to: int, cap: int):
        self.graph[v_from].append(
            Edge(v_to=v_to, cap=cap, rev=len(self.graph[v_to])))
        self.graph[v_to].append(
            Edge(v_to=v_from, cap=0, rev=len(self.graph[v_from]) - 1))

    def bfs(self, s: int, t: int):
        # search if shortest augmenting path exists
        self.level = [-1] * self.n
        queue = deque([s])
        self.level[s] = 0
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.cap > 0 and self.level[e.v_to] < 0:
                    self.level[e.v_to] = self.level[v] + 1
                    queue.append(e.v_to)
        return self.level[t] != -1

    def dfs(self, v: int, t: int, f: int) -> int:
        # search if shortest augmenting path exists
        if v == t:
            return f
        for e in self.it[v]:
            if e.cap > 0 and self.level[v] < self.level[e.v_to]:
                if (d := self.dfs(e.v_to, t, min(f, e.cap))) > 0:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
        return 0

    def max_flow(self, s: int, t: int) -> int:
        flow = 0
        while self.bfs(s, t):
            *self.it, = map(iter, self.graph)
            while (f := self.dfs(s, t, INF)) > 0:
                flow += f
        return flow

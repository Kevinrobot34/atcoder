# グラフ
## グラフの基本
グラフの頂点集合を$`V`$、辺の集合を$`E`$とする

### グラフの種類と用語
* 頂点(vertex, node)
* 辺(edge)
#### 無向グラフ
* 頂点の次数(degree)
#### 有向グラフ
* 頂点の入次数(in-degree)、出次数(out-degree)
#### 木
* 直径

### グラフの表現の仕方
* 隣接リスト
    * メモリが$`O(|V|+|E|)`$かかる。
* 隣接行列
    * メモリが$`O\left(|V|^2\right)`$かかる。ワーシャルフロイド(時間計算量$`O\left(|V|^3\right)`$)が使えるくらいの問題じゃないと使えない。


## 最短経路
### Dijkstra法
負の辺が存在しないグラフに対して、単一始点最短路問題を$`O(|E|\log|V|)`$で解けるアルゴリズム。
辺の数が多くないか注意してから使おう。

```python
from heapq import heappush, heappop
def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n

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
                heappush(heap, (dist[v_to], v_to))
    return dist
```

次の簡易的な実装だと$`O\left(|V|^2\right)`$。$`|V| \leq 10^3`$ で $`|E| = O\left(|V|^2\right)`$とかだとこっちの方が早かったりする
```python
def dijkstra(edge_adj: list, node: int, start: int) -> list:
    inf = float('inf')
    dist = [inf] * node
    used = [False] * node

    dist[start] = 0
    while True:
        v = -1
        for i in range(node):
            if not used[i] and (v == -1 or dist[v] > dist[i]):
                v = i

        if v == -1:
            break

        used[v] = True
        for i in range(node):
            if dist[i] > dist[v] + edge_adj[v][i]:
                dist[i] = dist[v] + edge_adj[v][i]

    return dist
```

問題
* [ABC035 D - トレジャーハント]( https://atcoder.jp/contests/abc035/tasks/abc035_d )
    * 有向グラフでは、辺を逆にすれば「単一**終点**最短経路問題」を解ける
* [ABC132 E - Hopscotch Addict (500点)]( https://atcoder.jp/contests/abc132/tasks/abc132_e )
    * 頂点の持ち方を工夫する
* [ABC164 E - Two Currencies (500点)]( https://atcoder.jp/contests/abc164/tasks/abc164_e )
    * 頂点の持ち方を工夫する
* [ARC064 E - Cosmic Rays (600点)]( https://atcoder.jp/contests/arc064/tasks/arc064_c )
    * $`O(V^2)`$のdijkstra
* [ARC025 C - ウサギとカメ]( https://atcoder.jp/contests/arc025/tasks/arc025_3 )
    * WarshallFloydに見せかけたDijkstraな問題
* [第２回日経コン D - Shortest Path on a Line (600点)]( https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d )
    * 辺の張り方を工夫する
* [soundhound2018-summer-qual D - Saving Snuuk (400点)]( https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d )
* https://yukicoder.me/problems/no/807


### 01-BFS
グラフの辺の重みが0か1のみの場合の最短経路問題を解くのに使える手法。

Reference
* [01-BFSのちょっと丁寧な解説]( https://betrue12.hateblo.jp/entry/2018/12/08/000020 )

問題
* [ABC077 D - Small Multiple (700点)]( https://atcoder.jp/contests/abc077/tasks/arc084_b )
    * 01-BFSなどを使うグラフの最短経路問題にまで落とし込むのが難しい
* [ARC005 C - 器物損壊！高橋君]( https://atcoder.jp/contests/arc005/tasks/arc005_3 )
* [ARC061 E - すぬけ君の地下鉄旅行  (600点)]( https://atcoder.jp/contests/arc061/tasks/arc061_c )


### Bellman-Ford法
単一始点最短路問題を$`O(|V| |E|)`$で解けるアルゴリズム。
$`\text{dist}[i]=`$(頂点$`i`$までの最短路)とした時、

```{latex}
\text{dist}[i] = \min \{ \text{dist}[j] + \text{cost}_{j\to i}  \:| \: (j, i) \in E  \}
```

が成り立つことを利用した手法。
負の辺が存在していても問題なく、また負の閉路の検出にも使える。
```python
def bellman_ford(n: int, edge: list):
    INF = float('inf')
    d = [INF] * n
    d[0] = 0
    for i in range(n):
        update = False
        for v_from, v_to, cost in edge:
            if d[v_from] != INF and d[v_to] > d[v_from] + cost:
                d[v_to] = d[v_from] + cost # 緩和
                update = True
    return d, update
```
問題
* [ABC061 D - Score Attack (400点)]( https://atcoder.jp/contests/abc061/tasks/abc061_d )
* [ABC137 E - Coins Respawn (500点)]( https://atcoder.jp/contests/abc137/tasks/abc137_e )

### Warshall-Floyd法
全点対最短路問題を$`O(|V|^3)`$で解けるアルゴリズム。
グラフを表す隣接行列を更新し、全点間の最短経路が入った行列にする。
$`d[i][j] = `$($`i`$から$`j`$への最短経路の長さ)として、初期化は
* $`d[i][i] = 0`$
* $`d[i][j] =\text{INF}~`$ ($`i`$と$`j`$の間に辺がないとき)
* $`d[i][j] = \text{cost}[i][j]`$

```python
def warshall_floyd(d, next_node):
    # d        : nxn adjacent matrix
    # next_node: node after i on the shortest path of (i,j)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    next_node[i][j] = next_node[i][k]
```

問題
* [ABC012 D - バスと避けられない運命]( https://atcoder.jp/contests/abc012/tasks/abc012_4 )
* [ABC022 C - Blue Bird]( https://atcoder.jp/contests/abc022/tasks/abc022_c )
    * 良問
* [ABC051 D - Candidates of No Shortest Paths (400点)]( https://atcoder.jp/contests/abc051/tasks/abc051_d )
* [ABC073 D - joisino's travel (400点)]( https://atcoder.jp/contests/abc073/tasks/abc073_d )
* [ABC143 E - Travel by Car (500点)]( https://atcoder.jp/contests/abc143/tasks/abc143_e )
* [ARC035 C - アットコーダー王国の交通事情]( https://atcoder.jp/contests/arc035/tasks/arc035_c )


### 経路復元
最短経路の長さを更新するときに、直前もしくは直後にどの点を通ったかといった情報も更新・保持するようにすればよい。

#### 経路復元 with dijkstra
```python
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
```

#### 経路復元 with Warshall-Floyd
経路復元付きWarshall-Floydのコードは上のWarshal-Floydの説参照。

* Warshall-Floyd法の経路復元
    * http://zeosutt.hatenablog.com/entry/2015/05/05/045943
    * [ABC051 D - Candidates of No Shortest Paths (400点)]( https://atcoder.jp/contests/abc051/tasks/abc051_d )が参考になる

問題
* [ABC051 D - Candidates of No Shortest Paths (400点)]( https://atcoder.jp/contests/abc051/tasks/abc051_d )

### 最短経路数
最短経路を求める時、どんな手法でも最短経路の配列の緩和処理をしていくはず。
緩和処理する際に、最短経路数も適宜更新するようにすればOK。
* $`\text{num}[i] ~=~`$(スタート地点から$`i`$までの最短経路の数)
* 初期化
    * $`\text{num}[v_{\rm start}] ~=~ 1`$
    * $`\text{num}[v_{\rm others}] ~=~ 0`$ （なんでもいい）

* http://drken1215.hatenablog.com/entry/2018/02/09/003200

Dijkstraの場合
```python
def dijkstra(graph: list,
             n: int,
             v_s: int,
             INF: int = float('inf'),
             MOD: int = 10**9 + 7) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n  # length of the shortest paths
    num = [0] * n     # number of the shortest paths

    dist[v_s] = 0
    num[v_s] = 1
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        _, v_from = heappop(heap)
        for v_to in graph[v_from]:
            dist_cand = dist[v_from] + 1
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                num[v_to] = num[v_from]
                heappush(heap, (dist[v_to], v_to))
            elif dist_cand == dist[v_to]:
                num[v_to] += num[v_from]
                num[v_to] %= MOD
    return dist, num
```
問題
* [ABC021 C - 正直者の高橋くん]( https://atcoder.jp/contests/abc021/tasks/abc021_c )


## 最小全域木
問題
* [ABC065 D - Built? (500点)]( https://atcoder.jp/contests/abc065/tasks/arc076_b )
    * 最小全域木を作る問題を少しひねってある良問。

### プリム法

### クラスカル法
対象のグラフを構成する辺をコストでソートし、小さい方から見ていく。
今見ている辺を追加することで閉路ができなければ、最小全域木の一辺として使う。
閉路ができるかどうかの判定にをUnionFindを使うことで高速に処理ができる。
結局辺のソートの部分に一番時間がかかり、$`|E| \leq |V|^2`$なので$`O(|E|\log |E|) = O(|E| \log |V|)`$で最小全域木のコストが求まる。
```python
def kruskal(n: int, edge: list) -> int:
    # edge[node] = (v_from, v_to, cost)
    edge.sort(key=itemgetter(2)) # Sort edges by its cost
    uf = UnionFind(n)
    ans = 0
    for v_from, v_to, cost in edge:
        if not uf.same(v_from, v_to):
            ans += cost
            uf.unite(v_from, v_to)
    return ans
```
* UnionFindについては[こちら]( #Union-Find木 )


## ネットワークフロー
### 最大流・最小カット
二部グラフの最大二部マッチング問題と関連がある。

与えられるネットワークは以下
* 有向グラフ $`G=(V, E)`$
* 各辺$`e \in E`$に対して **容量(capacity)** $`c(e) \geq 0`$が決まっている
* 始点(source): $`s \in V`$
* 終点(sink): $`t \in V ~ (s \neq t)`$


#### 最大流
* **s-tフロー**
    * 各辺$`e \in E`$に対し、(データ/水/etcを)流す量$`f(e)`$が定義されており、以下を満たす
        * 容量を超えない
            ```{latex}
            0 \leq f(e) \leq c(e)
            ```
        * 始点と終点以外は、湧き出しはない
            ```{latex}
            \forall v \in V \backslash\{s, t\}, ~ \sum_{e=*v}f(e) = \sum_{e=v*}f(e)
            ```
    * **フローの流量**
        ```{latex}
        |f| = \sum_{e=s*}f(e) - \sum_{e=*s}f(e)
        ```

最大流は$`\max |f|`$


#### 最小カット
* **s-tカット**
    * 頂点集合の分割$`V ~=~ S ~\bigsqcup~ T`$であって、$`s \in S`$ と $`t \in T`$ なるもののこと
    * カットの**容量(capacity)**
        * 始点を含む集合から終点を含む集合への流量の和
            ```{latex}
            c(S, T) = \sum_{e=vw,~ v \in S,~ w \in T} c(e)
            ```

最小カットは$`\min c(S, T)`$


#### 最大流・最小カット定理
最大流と最小カットは一致するという定理。

* 弱双対性: 任意のフローと任意のカットに対して、 $`|f| \leq c(S, T)`$
    ```{latex}
    \begin{align*}
    |f|
    &= \left( \sum_{e=s*}f(e) ~-~ \sum_{e=*s}f(e) \right) + 0 \\
    &= \left( \sum_{e=s*}f(e) ~-~ \sum_{e=*s}f(e) \right) + \left( \sum_{e=v*,~ v\in S\backslash \{s\}} f(e) ~-~ \sum_{e=*v,~ v\in S\backslash \{s\}} f(e) \right) \\
    &= \sum_{e=v*,~ v\in S} f(e) ~-~ \sum_{e=*v,~ v\in S} f(e) \\
    &= \sum_{e=vw,~ v\in S,~ w\in T} f(e) ~-~ \sum_{e=wv,~ v\in S,~ w\in T} f(e) \\
    &\leq \sum_{e=vw,~ v\in S,~ w\in T} c(e) ~-~ \sum_{e=wv,~ v\in S,~ w\in T} 0 \\
    &= c(S, T)
    \end{align*}
    ```
* 強双対性: あるフローとあるカットをうまく取ると$`|f| = c(S, T)`$





### 最小費用流
二部グラフの重み付き最大二部マッチング問題と関連がある。


### References
* [ネットワークフロー入門スライド by hosさん]( http://hos.ac/slides/20150319_flow.pdf )
* [実世界で超頻出！二部マッチング (輸送問題、ネットワークフロー問題）の解法を総整理！‬ - Qiita]( https://qiita.com/drken/items/e805e3f514acceb87602 )
* [PFN R&D blog - 乱択アルゴリズム紹介(最小カット)]( https://tech.preferred.jp/ja/blog/randomized-min-cut/ )


## トポロジカルソート
DAGについて、$`O(|V| + |E|)`$でトポロジカルソートした結果を取得できる。
以下の実装(`topological_sort`)はKahnの方法([参考]( https://ja.wikipedia.org/wiki/トポロジカルソート ))。

DAG上のDPとかやるときにあると便利。

またトポロジカルソートができることと、グラフがDAG(有向非巡回グラフ、Directed Acyclic Graph)であることは同値。以下の`is_dag`ように判定可能。

```python
from collections import deque
def topological_sort(graph: list, n_v: int) -> list:
    # graph[node] = [(cost, to)]
    indegree = [0] * n_v # 各頂点の入次数
    for i in range(n_v):
        for c, v in graph[i]:
            indegree[v] += 1

    cand = deque([i for i in range(n_v) if indegree[i] == 0])
    res = []
    while cand:
        v1 = cand.popleft()
        res.append(v1)
        for c, v2 in graph[v1]:
            indegree[v2] -= 1
            if indegree[v2] == 0:
                cand.append(v2)

    return res

def is_dag(graph: list, n_v: int):
    ts = topological_sort(graph, n_v)
    return len(ts) == n_v
```
* topological_sortの計算量は、indegreeの計算で$`O(|V|)`$、順番に辺を見て実際にtopological_sortする部分で$`O(|E|)`$、の合計$`O(|V| + |E|)`$

問題
* [ABC087 D - People on a Line (400点)]( https://atcoder.jp/contests/abc087/tasks/arc090_b )
* [ABC139 E - League (500点)]( https://atcoder.jp/contests/abc139/tasks/abc139_e )
    * トポロジカルソートじゃなくても大丈夫だが、トポロジカルソートちっくに書いても解ける。

## 木 / 根付き木
閉路のない連結なグラフのこと。

いくつかの大事なテクニックがある
* オイラーツアー
* LCA
* ReRooting


問題
* [ABC067  D - Fennec VS. Snuke (400点)]( https://atcoder.jp/contests/abc067/tasks/arc078_b )
    * 良問。競プロっぽい。言い換えが大事。
* [ABC133 E - Virus Tree 2 (500点)]( https://atcoder.jp/contests/abc133/tasks/abc133_e )
    * 数え上げ
* [ABC138 D - Ki (400点)]( https://atcoder.jp/contests/abc138/tasks/abc138_d )
    * 木の上でimos法的なことをする
* [ABC146 D - Coloring Edges on Tree (400点)]( https://atcoder.jp/contests/abc146/tasks/abc146_d )
* [ABC 148 F - Playing Tag on Tree (600点)]( https://atcoder.jp/contests/abc148/tasks/abc148_f )
* [ABC152 F - Tree and Constraints (600点)]( https://atcoder.jp/contests/abc152/tasks/abc152_f )
* [ABC165 F - LIS on Tree (600点)]( https://atcoder.jp/contests/abc165/tasks/abc165_f )
    * その名の通り、木上でLISをやる
    * 木上といいつつ、「巻き戻し」というテクニックを使うだけなので木DPとはちょっと違うか
* [ARC030 B - ツリーグラフ]( https://atcoder.jp/contests/arc030/tasks/arc030_2 )
* [ARC045 C - エックスオア多橋君]( https://atcoder.jp/contests/arc045/tasks/arc045_c )
* [日立コン2020 C - ThREE (600点)]( https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_c )
    * 構築系
    * 木が二部グラフとして見ることができる、というのがポイント
* [東京海上日動コン2020 D - Knapsack Queries on a tree (700点)]( https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_d )
    * 木の上で、半分全列挙を使ったナップザック問題を解く問題

### 木の基本的性質
* `(辺数) = (頂点数) - 1`
* 二部グラフとして捉えることができる

### LCA
https://en.wikipedia.org/wiki/Lowest_common_ancestor
実装方法はいくつかあり、
* ダブリング
    ```python
    class Tree():
        def __init__(self, n, graph, v_root):
            self.n = n  # number of nodes
            self.graph = graph  # adjacent list of graph
            self.v_root = v_root  # root node

            self.logn = (self.n - 1).bit_length()
            self.parent = [[-1] * self.n for _ in range(self.logn)]
            self.depth = [0] * self.n
            self.dist = [0] * self.n

            self.init()

        def init(self):
            self.dfs(self.v_root, -1, 0, 0)
            # doubling
            for k in range(self.logn - 1):
                for v in range(self.n):
                    if self.parent[k][v] != -1:
                        self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

        def dfs(self, v, v_par, depth, dist):
            self.parent[0][v] = v_par
            self.depth[v] = depth
            self.dist[v] = dist
            for v_next, d in self.graph[v]:
                if v_next == v_par:
                    continue
                self.dfs(v_next, v, depth + 1, dist + d)

        def lca(self, u, v):
            if self.depth[u] > self.depth[v]:
                u, v = v, u

            # go to parents of v until same depth as u
            diff = self.depth[v] - self.depth[u]
            for k in range(diff.bit_length()):
                if diff & (1 << k):
                    v = self.parent[k][v]
            if u == v:
                return u
            # binary search
            # for k in reversed(range(self.logn)):
            for k in range(self.depth[u].bit_length() - 1, -1, -1):
                if self.parent[k][u] != self.parent[k][v]:
                    u = self.parent[k][u]
                    v = self.parent[k][v]
            return self.parent[0][u]
    ```

* EulerTour + RMQ
    * RMQで最小値の値だけでなくそのindexを返すようにする必要がある
        * `(値, index)`をSegmentTreeの要素として、最初の要素の大小で比較するようにしておけば良い
    * https://www.creativ.xyz/abc014d-431/

    ```python
    class Tree():
        def __init__(self, n, graph, v_root):
            self.n = n  # number of nodes
            self.graph = graph  # adjacent list of graph
            self.v_root = v_root  # root node

            # euler tour
            self.first_idx = [2 * self.n] * self.n
            self.euler_tour = []
            self.euler_depth = []
            self.euler_tour_dfs(self.v_root, -1, 0)

            # Segment Tree for LCA
            depth_list = [(di, i) for i, di in enumerate(self.euler_depth)]
            INF = (2 * self.n, -1)
            operation_func = lambda a, b: a if a[0] < b[0] else b
            self.st_rmq = SegmentTree1(2 * self.n - 1, INF, operation_func) # Abstract Segment Tree
            self.st_rmq.build(depth_list)

        def euler_tour_dfs(self, v, v_par, depth):
            self.first_idx[v] = len(self.euler_tour)
            self.euler_tour.append(v)
            self.euler_depth.append(depth)
            for v_next in self.graph[v]:
                if v_next == v_par:
                    continue
                self.euler_tour_dfs(v_next, v, depth + 1)
                self.euler_tour.append(v)
                self.euler_depth.append(depth)

        def depth(self, v):
            return self.euler_depth[self.first_idx[v]]

        def lca(self, u, v):
            u_idx, v_idx = self.first_idx[u], self.first_idx[v]
            if u_idx > v_idx:
                u_idx, v_idx = v_idx, u_idx
            _, idx = self.st_rmq.query(u_idx, v_idx + 1)
            return self.euler_tour[idx]

        def dist(self, u, v):
            lca_uv = self.lca(u, v)
            return self.depth(u) + self.depth(v) - 2 * self.depth(lca_uv)
    ```



問題
* [ABC014 D - 閉路]( https://atcoder.jp/contests/abc014/tasks/abc014_4 )
* [ABC133 F - Colorful Tree (600点)]( https://atcoder.jp/contests/abc133/tasks/abc133_f )
    * LCAに更にもう一捻りしてあるので難しそう
* [F - 根付き木のみさわさん]( https://tenka1-2015-final-open.contest.atcoder.jp/tasks/tenka1_2015_final_f )


### Euler Tour
木を深さ優先探索したとき、行きと帰りの両方で頂点を数えたリストを用いて、木に対する操作を配列に対する操作に帰着させる手法。
頂点に対する操作と、辺に対する操作とでちょっと変わる(beetさんのブログ参照)

参考
* https://topcoder.g.hatena.ne.jp/iwiwi/20111205/1323099376
* https://www.npca.jp/works/magazine/#2015 の「木に対する一般的なテク達」
* http://beet-aizu.hatenablog.com/entry/2019/07/08/174727


```python
first_idx = [2 * n] * n
euler_tour = []
euler_depth = []
def dfs(v, par, depth):
    first_idx[v] = len(euler_tour)
    euler_tour.append(v)
    euler_depth.append(depth)
    for v_next in graph[v]:
        if v_next == par:
            continue
        dfs(v_next, v, depth + 1)
        euler_tour.append(v)
        euler_depth.append(depth)
```

### 木DP
根付き木上で（**根を固定して**）考えるDPのこと。
根付き木なので、根以外のある頂点に隣接する頂点は１つは親で他全てが子ということになる。

* `dp[i] := (頂点1を根とする根付き木において)頂点iを根とする部分木についての何か`
* ある頂点`i`の`dp[i]`は、その子にあたる頂点`j_1, ..., j_k`を根とする部分木についての値`dp[j_1], ..., dp[j_k]`から計算できるという状況
  <img title='tree.png' src='/attachments/289ddb21-98c6-450e-931c-2b3183b4da75' width="362" data-meta='{"width":362,"height":164}'>
    * さらにもう一歩進めて考えると
        * 頂点`i`の**子**`j_1, ..., j_k`の部分木についての結果(`dp[j_1], ..., dp[j_k]`)をmergeする処理
        * mergeした結果に頂点`i`自身を追加する処理
    * 具体例：「根付き木において根から最も遠い点までの距離を求める」
        * `dp[i] := 頂点iを根とする部分木について、iから最も遠い点までの距離`
        * `dp[i] = max(dp[j_1], ..., dp[j_k]) + 1`
            * `max`の部分が子の部分木をmergeする処理
            * `+1`の部分が頂点`i`自身を追加する処理


#### 全方位木DP / ReRooting
任意の頂点を根とした全ての場合について木DPを行いたい時に使うのが全方位木DP/ReRootingと呼ばれるテクニック。

根を一つ固定して普通に木DPをするのに$`O(N)`$の計算料がかかるので、全ての頂点を根として同様の作業をするとナイーブには全体で$`O(N^2)`$かかる。
しかし、一度根を一つ固定して普通に木DPし、その情報を適切に再利用することで、全頂点を根としたときの結果を$`O(N)`$で求めることができる。

ポイントはいくつかある
* 根付き木においては、根以外の頂点に隣接する頂点はただ一つの親と、複数の子からなる
* `dp[v][i] = (頂点vから出るi番目の有向辺に関する部分木のDPの値)`
    * 頂点`v`を根とする根付き木に注目した時には、`dp[v][i]`全ての情報が必要で、これらをmergeすれば結果を得られる
* 一度適当な頂点`v_0`を根として固定し木DPをすると、
    * `v==v_0` : `{dp[v][i] | i = 1,2, ..., }`の**全てが求まる**
    * `v!=v_0` : `{dp[v][i] | i = 1,2, ..., }`のうち、**`i=(vの親に対応するindex)`なる１つ以外**全てが求まる
* 上記を踏まえて２回DFSをする
    * まず適当な頂点`v_0`を根として木DPをおこなう
    * また`v_0`を根とした根付き木上をDFSする
        * 各頂点で唯一まだ求まっていない`dp[v][i] : i=(vの親に対応するindex)`を伝播させていき、頂点`v`を根とした根付き木だった場合の値を計算する


References
* [【全方位木DP】明日使える便利な木構造のアルゴリズム]( https://qiita.com/keymoon/items/2a52f1b0fb7ef67fb89e )
* [木DPと全方位木DPを基礎から抽象化まで解説【競技プログラミング】]( https://algo-logic.info/tree-dp/ )

問題
* [ABC160 F - Distributing Integers]( https://atcoder.jp/contests/abc160/tasks/abc160_f )
* [EDPC V - Subtree]( https://atcoder.jp/contests/dp/tasks/dp_v )


### 木の直径
木において、2つの頂点の距離の最大値を **木の直径** という。

性質
*

求め方
1. 全方位木DP
    * 全頂点を根とした根付き木の深さの最大値を求めるイメージ
    * シンプルだけど全方位木DPしないといけなくて少し大変
2. LCA的な考え方の木DP
    * 参考 : [ARC022 解説]( https://www.slideshare.net/chokudai/arc022 )
3. Double-Sweep
    * 適当な頂点`x`を根とし、`x`から最も遠い頂点を探しその一つを`y`とする
    * `y`を根とし、`y`から最も遠い頂点を探しその一つを`z`とする
    * `(y, z)` の距離は直径となっている
        * 「どの頂点を根としても、根から最も遠くにある頂点 x は必ず直径の端点になる」という性質を利用したもの

問題
* [ABC019 D - 高橋くんと木の直径]( https://atcoder.jp/contests/abc019/tasks/abc019_4 )
* [ARC022 C - ロミオとジュリエット]( https://atcoder.jp/contests/arc022/tasks/arc022_3 )


## その他
問題
* [ABC108 D - All Your Paths are Different Lengths (700点)]( https://atcoder.jp/contests/abc108/tasks/arc102_b )
* [ABC131 E - Friendships (500点)]( https://atcoder.jp/contests/abc131/tasks/abc131_e )

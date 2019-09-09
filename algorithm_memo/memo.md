競技プログラミングのメモ \
基本的に蟻本([Amazonのリンク]( https://www.amazon.co.jp/dp/4839941068/ref=cm_sw_em_r_mt_dp_U_ZTWrDb9R924BK ))に書かれているアルゴリズムの実装や関連問題をメモしている。

# コンテストサイト
* [AtCoder]( http://atcoder.jp )
    * my account : https://atcoder.jp/users/Kevinrobot34
        * AtCoder Problems : https://kenkoooo.com/atcoder/#/user/Kevinrobot34
        * AtCoder Scores: http://atcoder-scores.herokuapp.com/?user=Kevinrobot34
    * 過去の自分の解答 : https://github.com/Kevinrobot34/atcoder
    * [YouTube - AtCoder Live]( https://www.youtube.com/channel/UCtG3StnbhxHxXfE6Q4cPZwQ )
        * コンペの後、問題解説生放送をやってる。
        * 1.5倍速くらいで見ると、コスパよく勉強になる。
* [Codeforces]( https://codeforces.com )
    * my account : https://codeforces.com/profile/Kevinrobot34
* [AOJ]( http://judge.u-aizu.ac.jp/onlinejudge/ )
    * my account : http://judge.u-aizu.ac.jp/onlinejudge/user.jsp?id=Kevinrobot34#0


# 入出力
基本的に競技プログラミングは**標準入力**から特定のフォーマットの入力を受け取り、
**標準出力**から特定のフォーマットに従って出力をする。

**C++** \
標準入出力はcstdioの`scanf()`と`printf()`か、iostreamの`cin`と`cout`を使う。
前者の方が早いらしい。
```cpp
#include<cstdio>
int n;
scanf("%d", &n); // 整数
char s[10], c;
scanf("%s", s);  // 文字列
scanf("%c", &c); // 文字

#include<iostream>
using namespace std;
int n;
cin >> n;
```

**python** \
標準入力からの入力の受け取りには、組み込み関数の[input()]( https://docs.python.org/ja/3/library/functions.html#input )を使う。
> input([prompt])
> （略）この関数は入力から 1 行を読み込み、文字列に変換して (末尾の改行を除いて) 返します

標準出力は当然`print()`
```python
# 文字列
s = input()

# 整数１つ
n = int(input())
# 整数複数
a, b = map(int, input().split())
# 整数をリストで
x = list(map(int, input().split()))

# m行の入力
m = int(input())
table = [list(map(int, input().split())) for _ in range(m)]
```

多くの行から読み込みが必要な場合、`input()`は遅いらしい。そのような時には以下のように代わりに`sys.stdin.readline`を使うようにしておくと早くなる。
```python
import sys
input = sys.stdin.readline
```



## リダイレクト
毎回テストデータを手入力していると面倒。適宜**リダイレクト**すると良い。 \
`test.txt`というファイルにテストデータを保存しておいて、
```
# C/C++
$ ./a.out < test.txt
# python
$ python hoge.py < test.txt
```
とすると、`test.txt`の内容を標準入力として入力しファイルを実行することができる。



# 基本的なデータ構造
## 文字列
**C++** \
http://vivi.dyndns.org/tech/cpp/string.html

**python** \
pythonのstringはimmutableだぞっ。
https://qiita.com/Amtkxa/items/a03dabe050d8c648f098


## 配列

### sort
$O(N\log N)$でソート済み配列を取得する。

**C++** \
https://cpprefjp.github.io/reference/algorithm/sort.html \
https://qiita.com/a4rcvv/items/7cd217cc5fafef700dff

**python** \
https://docs.python.org/ja/3.7/howto/sorting.html
pythonのソートは`sorted(a)`と`a.sort()`がある。
共通点は、
* ともにデフォルトでは昇順ソート。`reverse=True`とパラメーターすると降順になる。
* `key`パラメーターにlambda式などを入れると、比較の仕方を変えられる。

で、違いは
*  `sorted(a)`は新たにソートされたリストを返すが、`a.sort()`は`a`をインプレースにソート済みのものに変更しNoneを返す。
* `a.sort()`はリストにのみ定義されている。


```python
a = [5, 2, 3, 1, 4]
print(sorted(a)) # [1, 2, 3, 4, 5]
print(a)         # [5, 2, 3, 1, 4]

a.sort() # return None
print(a) # [1, 2, 3, 4, 5]

b = [5, 2, 3, 1, 4]
print(sorted(a, reverse=True)) # [5, 4, 3, 2, 1]
```

## deque
double-ended queueのことで、**stackとqueueを一般化したもの**。\
発音は「デック」らしい。内部的には双方向連結リストとして実装されているらしい(要出典)。

**C++** \
https://cpprefjp.github.io/reference/deque/deque.html

**python** \
https://docs.python.org/ja/3/library/collections.html#collections.deque \
`append(i)`, `appendleft(i)`, `pop()`, `popleft()`, が$O(1)$で出来る。
* > list オブジェクトでも(dequeと)同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします。
* listでもlast要素のpop（つまりただの`.pop()`）であれば$O(1)$。https://wiki.python.org/moin/TimeComplexity

```python
from collections import deque
dq = deque([5, 6, 7, 8])
dq.pop() # 8
len(dq) # 3
dq # deque([5, 6, 7])

dq.appendleft(4)
dq # deque([4, 5, 6, 7])

# 一応添字のアクセスもできる
dq[1] # 5
```


## stack
LIFO(Last In First Out)なコンテナ。
DFSの実装などに使える。再帰関数でも同様な動作。

**C++** \
https://cpprefjp.github.io/reference/stack.html \
dequeをラップしているっぽい。

**python** \
stackはない。dequeをよしなに使うとよい。 \
listの`append(hoge)`と`pop()`を使うことでも実装可能([参考：リストをスタックとして使う]( https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-stacks ))。


## queue
FIFO(First In First Out)なコンテナ。待ち行列とも。
BFSの実装などに使える。

**C++** \
https://cpprefjp.github.io/reference/queue/queue.html \
dequeをラップしているっぽい。


**python** \
queueはない（`queue.Queue`は並行実行のためのmoduleで、純粋なデータ型ではない）。dequeをよしなに使うのが良さそう（[参考：リストをキューとして使う]( https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-queues )）。


## priority_queue
優先度付きキュー。挿入された順番通りにpopするのではなく(FIFOではなく)、優先度の高い要素から先に取り出すようになっているキュー。 \
[二分ヒープ]( https://ja.wikipedia.org/wiki/二分ヒープ )を用いて実現している。

**C++** \
https://cpprefjp.github.io/reference/queue/priority_queue.html

**python** \
https://docs.python.org/ja/3/library/heapq.html \
(実装は https://github.com/python/cpython/blob/master/Lib/heapq.py )
pythonのheapは二分min-heapなことに注意。つまり、
* `heap[k] <= heap[2*k+1]` かつ `heap[k] <= heap[2*k+2]`
* `heap[0]`が最小値

```python
from heapq import heappush, heappop
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
print(h)
# [(1, 'write spec'), (3, 'create tests'), (5, 'write code'), (7, 'release product')]
heappop(h)
# (1, 'write spec')
print(h)
# [(3, 'create tests'), (7, 'release product'), (5, 'write code')]
```

問題
* [ABC062 D - 3N Numbers (500点)]( https://atcoder.jp/contests/abc062/tasks/arc074_b )
* [ABC123 D - Cake 123 (400点)]( https://atcoder.jp/contests/abc123/tasks/abc123_d )
    * priority_queueの使い方・挙動を理解するのに良い問題。別解も多くて勉強になる。


## set
**C++** \
https://cpprefjp.github.io/reference/set/set.html

**python** \
https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset


## map/dict
**C++** \
https://cpprefjp.github.io/reference/map/map.html

**python** \
https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict
* `key in dict`と書くと早い。`key in dict.keys()`とかやってると$O(N)$になるので注意。



# 探索
## 全探索
競プロでは文字通りの全列挙で解ける問題もしばしば出題されるので、DFS・BFS・bit使って全列挙などパッと書けるようになるのが大事。
また完全な意味での全列挙でなくても、「ある変数$x$を固定するとそれ以外の変数については最適なパターンが決まるので、変数$x$について全探索する」的な解法もしばしばある。

問題
* [ABC062 C - Chocolate Bar (400点)]( https://atcoder.jp/contests/abc062/tasks/arc074_a )
* [ABC080 C - Shopping Street (300点)]( https://atcoder.jp/contests/abc080/tasks/abc080_c )
* [ABC099 C - Strange Bank (300点)]( https://atcoder.jp/contests/abc099/tasks/abc099_c )
* [ABC099 D - Good Grid (400点)]( https://atcoder.jp/contests/abc099/tasks/abc099_d )
* [ABC104 C - All Green (300点)]( https://atcoder.jp/contests/abc104/tasks/abc104_c )
    * bitを使った全探索（各問題を全部解くor全く解かない）
* [ABC107 C - Candles (300点)]( https://atcoder.jp/contests/abc107/tasks/arc101_a )
* [ABC112 C - Pyramid (300点)]( https://atcoder.jp/contests/abc112/tasks/abc112_c )
* [ABC128 D - equeue (400点)]( https://atcoder.jp/contests/abc128/tasks/abc128_d )


### DFS - 深さ優先探索
実装方法
* 再帰関数
* stack

問題
* [ABC054 C - One-stroke Path (300点)]( https://atcoder.jp/contests/abc054/tasks/abc054_c )
    * グラフをdfsで全探索するいい練習問題
* [ABC119 C - Synthetic Kadomatsu (300点)]( https://atcoder.jp/contests/abc119/tasks/abc119_c )
* [ABC114 C - 755 (300点)]( https://atcoder.jp/contests/abc114/tasks/abc114_c )
* [ABC126 D - Even Relation (400点)]( https://atcoder.jp/contests/abc126/tasks/abc126_d )


### BFS - 幅優先探索
実装方法
* queue

問題
* [AGC033 A - Darker and Darker (300点)]( https://atcoder.jp/contests/agc033/tasks/agc033_a )
* [ABC088 D - Grid Repainting (400点)]( https://atcoder.jp/contests/abc088/tasks/abc088_d )


## 二分探索
https://qiita.com/drken/items/97e37dd6143e33a64c8c

**C++** \
https://cpprefjp.github.io/reference/algorithm/lower_bound.html \
https://cpprefjp.github.io/reference/algorithm/upper_bound.html

**python** \
https://docs.python.org/ja/3/library/bisect.html

* `bisect.bisect_left(a, x)`
  * 昇順ソート済みlist`a`の中で、`a[index] >= x`という条件を満たす最小の`index`を返す
* `bisect.bisect_right(a, x)`
  * 昇順ソート済みlist`a`の中で、`a[index] > x`という条件を満たす最小の`index`を返す
  * `bisect.bisect`のalias

```python
from bisect import bisect_left, bisect_right
#    0 1 2 3 4 5 6 7 8 9
a = [1,1,1,3,3,3,3,4,4,4]

bisect_left(a, 0), bisect_right(a, 0) #  0,  0
bisect_left(a, 1), bisect_right(a, 1) #  0,  3
bisect_left(a, 2), bisect_right(a, 2) #  3,  3
bisect_left(a, 3), bisect_right(a, 3) #  3,  7
bisect_left(a, 4), bisect_right(a, 4) #  7, 10
bisect_left(a, 5), bisect_right(a, 5) # 10, 10
```

問題
* lower_bound / bisect_leftなど使ってソート済み配列を二分探索するタイプの問題
    * [ABC077 C - Snuke Festival (300点)]( https://atcoder.jp/contests/abc077/tasks/arc084_a )
    * [ABC119 D - Lazy Faith (400点)]( https://atcoder.jp/contests/abc119/tasks/abc119_d )
    * [ABC138 E - Strings of Impurity (500点)]( https://atcoder.jp/contests/abc138/tasks/abc138_e )
* 自分でループ書くタイプの二分探索するタイプの問題
    * [ABC063 D - Widespread (400点)]( https://atcoder.jp/contests/abc063/tasks/arc075_b )


## 半分全列挙




# アルゴリズム
## 累積和
数列$a_0, a_1, ..., a_{N-1}$がある時に、$\sum_{i=l}^r a_i$を計算する問題を考える。
ナイーブに足し算をすると$O(N)$かかりうる。
しかしあらかじめ$b_0 = 0, ~~ b_{n+1} = \sum_{j=0}^{n} a_j = b_n + a_n$という数列を用意しておくと、
$\sum_{i=l}^r a_i = b_{r+1} - b_l$と$O(1)$で計算できる。

pythonicに書くと、`sum(a[l:r])` が `b[r] - b[l]` で計算できると言うこと。
そう考えると、`b[r] = sum(a[:r])` と分かりやすくて良い。

```python
#id  0  1  2  3  4   5   6   7   8   9
a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
b = [0] * (len(a) + 1)
for i in range(len(a)):
    b[i+1] = b[i] + a[i]

print(b[:7]) # [0, 1, 4, 9, 16, 25, 36]

# sum(a[3:6])
print(b[6] - b[3]) # 27
```

問題
* [ABC084 D - 2017-like Number (400点)]( https://atcoder.jp/contests/abc084/tasks/abc084_d )
* [ABC098 C - Attention (300点)]( https://atcoder.jp/contests/abc098/tasks/arc098_a )
* [ABC106 D - AtCoder Express 2 (400点)]( https://atcoder.jp/contests/abc106/tasks/abc106_d )
* [ABC122 C - GeT AC (300点)]( https://atcoder.jp/contests/abc122/tasks/abc122_c )


## しゃくとり法
問題
* [ABC124 D - Handstand (400点)]( https://atcoder.jp/contests/abc124/tasks/abc124_d )
* [ABC130 D - Enough Array (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_d )
    * 典型的なしゃくとり法
* [ABC098 D - Xor Sum 2 (500点)]( https://atcoder.jp/contests/abc098/tasks/arc098_b )


## いもす法
https://imoz.jp/algorithms/imos_method.html

問題
* [ABC080 D - Recording (400点)]( https://atcoder.jp/contests/abc080/tasks/abc080_d )


## 座標圧縮
問題
* [ABC113 C - ID (300点)]( https://atcoder.jp/contests/abc113/tasks/abc113_c )


## Run-length圧縮


## 繰り返し二乗法・ダブリング




# 動的計画法
## DP
いろんなパターンがある。それぞれの詳細については別途記載。
* ナップザック
* [LIS - 最長増加部分列]( https://github.com/Kevinrobot34/atcoder/blob/master/algorithm_memo/LIS.md )

問題
* フィボナッチ数列の延長
  * [ABC129 C - Typical Stairs (300点)]( https://atcoder.jp/contests/abc129/tasks/abc129_c )
* ナップザック問題系
    * [ABC032D - ナップサック問題]( https://atcoder.jp/contests/abc032/tasks/abc032_d )
    * [ABC060 D - Simple Knapsack (400点)]( https://atcoder.jp/contests/abc060/tasks/arc073_b )
* LIS (Longest Increasing Subsequence)系
    * [ABC006 D - トランプ挿入ソート]( https://atcoder.jp/contests/abc006/tasks/abc006_4 )
    * [ABC134 E - Sequence Decomposing (500点)]( https://atcoder.jp/contests/abc134/tasks/abc134_e )
* その他
  * 体感難しい順
  * [ABC135 D - Digits Parade (400点)]( https://atcoder.jp/contests/abc135/tasks/abc135_d )
  * [ABC118 D - Match Matching (400点)]( https://atcoder.jp/contests/abc118/tasks/abc118_d )
  * [ABC122 D - We Like AGC (400点)]( https://atcoder.jp/contests/abc122/tasks/abc122_d )
  * [ABC104 D - We Love ABC (400点)]( https://atcoder.jp/contests/abc104/tasks/abc104_d )
  * [ABC082 D - FT Robot (500点)]( https://atcoder.jp/contests/abc082/tasks/arc087_b )
  * [ABC132 F - Small Products (600点)]( https://atcoder.jp/contests/abc132/tasks/abc132_f )


## bitDP
整数の2進数表記を用いて、サイズNの部分集合を全列挙するなどして行うDPのこと。 \
例
* 巡回セールスマン問題(TSP)

問題
* [JOI Flag]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0559 )
* [ABC113 D - Number of Amidakuji (400点)]( https://atcoder.jp/contests/abc113/tasks/abc113_d )


## 桁DP
http://drken1215.hatenablog.com/entry/2019/02/04/013700

問題
* [Zigzag Numbers]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0570 )
* xor系
  * 2進数表記で、桁ごとに考えると良いことが多い
  * [ABC117 D - XXOR (400点)]( https://atcoder.jp/contests/abc117/tasks/abc117_d )
  * [ABC129 E - Sum Equals Xor (500点)]( https://atcoder.jp/contests/abc129/tasks/abc129_e )
      * http://drken1215.hatenablog.com/entry/2019/06/10/150000




# グラフ
## 最短経路
### Dijkstra法
負の辺が存在しないグラフに対して、単一始点最短路問題を$O(|E|\log|V|)$で解けるアルゴリズム。
辺の数が多くないか注意してから使おう。

```python
from heapq import heappush, heappop
def dijkstra(graph: list, node: int, start: int) -> list:
    # graph[node] = [(cost, to)]
    inf = float('inf')
    dist = [inf] * node

    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, thisNode = heappop(heap)
        for NextCost, NextNode in graph[thisNode]:
            dist_cand = dist[thisNode] + NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode], NextNode))
    return dist
    # dist = [costs to nodes]
```

問題
* 変形Dijkstra
    * [ABC132 E - Hopscotch Addict (500点)]( https://atcoder.jp/contests/abc132/tasks/abc132_e )
        * 良問
    * https://yukicoder.me/problems/no/807


### Bellman-Ford法
単一始点最短路問題を$O(|V| |E|)$で解けるアルゴリズム。
$\text{dist}[i]=$(頂点$i$までの最短路)とした時、
$$ \text{dist}[i] = \min \\{ \text{dist}[j] + \text{cost}_{j\to i} ~|~ (j, i) \in E  \\} $$
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
* [ABC137 E - Coins Respawn (500点)]( https://atcoder.jp/contests/abc137/tasks/abc137_e )

### Warshall-Floyd法
全点対最短路問題を$O(|V|^3)$で解けるアルゴリズム。

問題
* [ABC073 D - joisino's travel (400点)]( https://atcoder.jp/contests/abc073/tasks/abc073_d )


### 経路復元



## 最小全域木
問題
* [ABC065 D - Built? (500点)]( https://atcoder.jp/contests/abc065/tasks/arc076_b )
    * 最小全域木を作る問題を少しひねってある良問。

### プリム法

### クラスカル法
対象のグラフを構成する辺をコストでソートし、小さい方から見ていく。
今見ている辺を追加することで閉路ができなければ、最小全域木の一辺として使う。
閉路ができるかどうかの判定にをUnionFindを使うことで高速に処理ができる。
結局辺のソートの部分に一番時間がかかり、$E\leq V^2$なので$O(|E|\log |E|) = O(|E| \log |V|)$で最小全域木のコストが求まる。
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


## トポロジカルソート
DAGについて、$O(|V| + |E|)$でトポロジカルソートした結果を取得できる。
以下の実装(`topological_sort`)はKahnの方法([参考]( https://ja.wikipedia.org/wiki/トポロジカルソート ))。


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
* topological_sortの計算量は、indegreeの計算で$O(|V|)$、順番に辺を見て実際にtopological_sortする部分で$O(|E|)$、の合計$O(|V| + |E|)$

問題
* [ABC087 D - People on a Line (400点)]( https://atcoder.jp/contests/abc087/tasks/arc090_b )
* [ABC139 E - League (500点)]( https://atcoder.jp/contests/abc139/tasks/abc139_e )
    * トポロジカルソートじゃなくても大丈夫だが、トポロジカルソートちっくに書いても解ける。

## 木 / 根付き木
問題
* [ABC067  D - Fennec VS. Snuke (400点)]( https://atcoder.jp/contests/abc067/tasks/arc078_b )
    * 良問。競プロっぽい。言い換えが大事。
* [ABC133 E - Virus Tree 2 (500点)]( https://atcoder.jp/contests/abc133/tasks/abc133_e )
    * 数え上げ
* [ABC138 D - Ki (400点)]( https://atcoder.jp/contests/abc138/tasks/abc138_d )
    * 木の上でimos法的なことをする


### LCA
https://en.wikipedia.org/wiki/Lowest_common_ancestor

問題
* [ABC133 F - Colorful Tree (600点)]( https://atcoder.jp/contests/abc133/tasks/abc133_f )
    * LCAに更にもう一捻りしてあるので難しそう
* [F - 根付き木のみさわさん]( https://tenka1-2015-final-open.contest.atcoder.jp/tasks/tenka1_2015_final_f )


### Euler Tour
https://topcoder.g.hatena.ne.jp/iwiwi/20111205/1323099376


## その他
問題
* [ABC108 D - All Your Paths are Different Lengths (700点)]( https://atcoder.jp/contests/abc108/tasks/arc102_b )
* [ABC131 E - Friendships (500点)]( https://atcoder.jp/contests/abc131/tasks/abc131_e )



# 数学
## 約数
```python
def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            divisor.append(n // i)
    return divisor
```

### GCD / LCM
キーワード : GCD(最大公約数 - Greatest Common Divisor), LCM(最小公倍数 - Least Common Multiple), ユークリッドの互除法
```cpp
int GCD(int a, int b) { return b ? GCD(b, a % b) : a; }
int LCM(int a, int b) { return a * b / GCD(a, b) }
```
```python
def GCD(a:int , b: int) -> int:
    return a if b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int:
    return a * b // GCD(a, b)    
```
問題
* [ABC131 C - Anti-Divisor (300点)]( https://atcoder.jp/contests/abc131/tasks/abc131_c )
* [ABC125 C - GCD on Blackboard (300点)]( https://atcoder.jp/contests/abc125/tasks/abc125_c )
    * 複数の数に対するGCD


## 素数
### 素因数分解
```python
from collections import defaultdict
def factorize(n: int) -> dict:
    f = defaultdict(int)
    p = 2
    while n > 1:
        while n % p == 0:
            f[p] += 1
            n = n // p
        p += 1 if p == 2 else 2
    return f
```
問題
* [ABC052 C - Factors of Factorial (300点)]( https://atcoder.jp/contests/abc052/tasks/arc067_a )

### エラトステネスの篩
$n$までの素数を$O(n\log\log n)$で求められるアルゴリズム。
1. 2から$n$までの整数の配列を用意し全てTrueにする。
2. 小さい方から順に数字を見てTrueである数字は素数とみなす。その数字の倍数に対応する要素はFalseにする。
3. 2.を繰り返して行く。

オーダーは、$n$以下の素数の逆数和が$O(\log\log n)$であることから従う
（参考：[素数の逆数和が発散することの証明]( https://mathtrain.jp/primeinverse )）。
境界条件がちょっとだけ面倒なので、$n$ではなく大きな数字を入れておくとバグりにくいかも。
```python
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False
for i in range(2, n):
    if is_prime[i]:
        for j in range(2, n // i + 1):
            is_prime[i*j] = False
```

問題
* [ABC084 D - 2017-like Number (400点)]( https://atcoder.jp/contests/abc084/tasks/abc084_d )


## Combination
combinationの計算を効率よくやるには工夫が必要。\
階乗とその逆元の事前計算をしておくことで高速にcombinationができるようになる。
以下のFermatの小定理を使うことで、
「素数を法とする時(mod p の時)の$a$の逆元は$a^{p-2}$であることがわかる」ということがポイント。
> Fermatの小定理
> $p$を素数、$a$を$p$の倍数でない整数とする時、
> $$ a^{p-1} \equiv 1 ~\text{ (mod $p$)} $$
> [ $\Rightarrow$  $p$を素数、$a$を任意の整数とする時、$a^p \equiv a ~\text{ (mod $p$)}$ ]

http://drken1215.hatenablog.com/entry/2018/06/08/210000
```cpp
const int MAX = 510000;
const int MOD = 1000000007;
long long int fac[MAX], finv[MAX], inv[MAX];
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

long long int COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}
```
```python
MOD = 10**9 + 7
MAX = 2000 + 5
fact = [1 for _ in range(MAX)]
finv = [1 for _ in range(MAX)]
for i in range(2, MAX):
    fact[i] = fact[i - 1] * i % MOD
    finv[i] = pow(fact[i], MOD-2, MOD)

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD
```


問題
* [ABC110 D - Factorization (400点)]( https://atcoder.jp/contests/abc110/tasks/abc110_d )
* [ABC132 D - Blue and Red Balls (400点)]( https://atcoder.jp/contests/abc132/tasks/abc132_d )


## XOR
https://qiita.com/kuuso1/items/778acaa7011d98a3ff3a

XOR関連の問題はDPなどと合わせて出たり、数学の問題として出ることが多々ある。
XORの性質について知っていると便利なことも多い


| $a$ | $b$ | $a \bigoplus b$ |
| --- | --- | --------------- |
| 0   | 0   | 0               |
| 0   | 1   | 1               |
| 1   | 0   | 1               |
| 1   | 1   | 0               |

* $a$ xor $b$ $\leq a + b$
* $a  \bigoplus x \bigoplus x = a$
* 任意の偶数$n$について$n \bigoplus (n+1) = 1$

問題
* [ABC121 D - XOR World (400点)]( https://atcoder.jp/contests/abc121/tasks/abc121_d )



# データ構造
## Union-Find木
グループ分けを管理するためのデータ構造。以下の操作が「効率的」に行える。
* 同じグループかどうかの確認
* ２つのグループの併合

一番ナイーブな実装は以下。
```cpp
struct UnionFind {
    vector<int> par;
    UnionFind(int N) : par(N) {
        for (int i = 0; i < N; i++) par[i] = i;
    }
    int find(int x) {
        if (par[x] != x) par[x] = find(par[x]); // contraction
        return par[x];
    }
    void unite(int x, int y) {
        x = find(x);
        y = find(y);
        par[x] = y;
    }
    bool same(int x, int y) { return find(x) == find(y); }
};

UnionFind uf(5); // uf.par [0, 1, 2, 3, 4]
uf.unite(0, 1)   // uf.par [1, 1, 2, 3, 4]
uf.unite(1, 2)   // uf.par [1, 2, 2, 3, 4]
uf.find(0)       // uf.par [2, 2, 2, 3, 4]
```

```python
class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x]) # contraction
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.par[x] = y

    def same(self, x, y):
        return self.find(x) ==  self.find(y)

uf = UnionFind(5) # uf.par [0, 1, 2, 3, 4]
uf.unite(0, 1)    # uf.par [1, 1, 2, 3, 4]
uf.unite(1, 2)    # uf.par [1, 2, 2, 3, 4]
uf.find(0)        # uf.par [2, 2, 2, 3, 4]
```


更に上手に実装すると、
* rank of union (蟻本はこっち)
* size of union (今回はこっち)

を持つこともできる。(参考 : http://drken1215.hatenablog.com/entry/2019/03/03/224600) \
ポイントとしては、`par`という配列を
* 全て-1で初期化。
* rootのnodeについては、`-(size of union)`を保持する。（逆に負の数であればroot。）
* root以外のnodeについては、parentのidを保持する。（逆に正の数であればleaf。）
* (size of union)に簡単にアクセスできるようになったので、merge techniqueとして、サイズが大きなものに小さなものを結合するようにする。

という形で実装すること。

```python
class UnionFind():
    def __init__(self, n):
        self.par = [-1 for i in range(n)]

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # contraction
            return self.par[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            if self.par[x] > self.par[y]: # merge technique
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]
```

問題
* [ABC097 D - Equals (400点)]( https://atcoder.jp/contests/abc097/tasks/arc097_b )
* [ABC120 D - Decayed Bridges (400点)]( https://atcoder.jp/contests/abc120/tasks/abc120_d )
* [ABC126 E - 1 or 2 (500点)]( https://atcoder.jp/contests/abc126/tasks/abc126_e )
* [ABC131 F - Must Be Rectangular! (600点)]( https://atcoder.jp/contests/abc131/tasks/abc131_f )


## Segment Tree / BIT
問題
* [ABC136 F - Enclosed Points (600点)]( https://atcoder.jp/contests/abc136/tasks/abc136_f )



# 何とも言えないけど競プロっぽいやつ
うまく言語化できないけど、競プロっぽい問題はたくさんあるし、慣れないと解けない。
ちょっとずつこれらのまとめもしていきたい。

問題
* [AGC034 A - Kenken Race (400点)]( https://atcoder.jp/contests/agc034/tasks/agc034_a )
* [AGC034 B - ABC (600点)]( https://atcoder.jp/contests/agc034/tasks/agc034_b )
* [ABC092 D - Grid Components(500点)]( https://atcoder.jp/contests/abc092/tasks/arc093_b )
* [ABC135 E - Golf (500点)]( https://atcoder.jp/contests/abc135/tasks/abc135_e )
* [ABC136 D - Gathering Children (400点)]( https://atcoder.jp/contests/abc136/tasks/abc136_d )
  - 問題を細かく分解する、状況をよく整理して答えを書くなどが大事
* [JSC2019-qual C - Cell Inversion (500点)]( https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_c )



# Memo
**python関連**
* python3でTLEする場合はPyPy3に変えてみると通ることもある。
    * ただし再帰使って書いたDFSなどはpython3の方が早かったりもする
* python3でTLEする場合、多数行の読み込みが遅いだけのことがある。遅い`input()`の代わりに`sys.stdin.readline`を使おう。
    ```python
  import sys
  input = sys.stdin.readline
    ```
* pythonの謎の`RE`について。
    * 再帰関数を使っているならば可能性の一つとして、`RecursionError: maximum recursion depth exceeded in comparison` がある。
    * 対策は以下。
       ```python
      import sys
      sys.setrecursionlimit(10**6)
      ```
* PyPy3(2.4.0)では`math.log2`が使えない。


# Reference
* [AtCoder 版！蟻本 (初級編)]( https://qiita.com/drken/items/e77685614f3c6bf86f44 )
* [競技プログラミングを趣味にしよう]( https://trap.jp/post/152/ )
* [特集！知らないと損をする計算量の話]( https://qiita.com/drken/items/18b3b3db5735241465ef )

**Python関連**
* [Pythonで競技プログラミング]( https://qiita.com/knakajima3027/items/b871631b8997a6d67223 )
    * pythonの各種アルゴリズムなどがまとまってる
* [Pythonistaなら知らないと恥ずかしい計算量のはなし]( https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb )
    * PythonのList, Deque, Dictの計算量の話
* [Python_競技プログラミング高速化tips]( https://juppy.hatenablog.com/entry/2019/06/14/Python_競技プログラミング高速化tips_%28PythonでAtcoderをやる際に個 )

**C++関連**
* [Macで#include<bits/stdc++.h>を導入]( http://perogram.hateblo.jp/entry/2019/04/15/094647 )
    * Macだとそのままではcppで`#include<bits/stdc++.h>`は使えないが、自分で`/usr/local/include/bits/stdc++.h`を作ってしまえば使えるようになる。
    * https://gist.github.com/Kevinrobot34/cd95d23d6917c30a39df854481d7468e
* [AtCoder Programming Guide for beginners (APG4b)]( https://atcoder.jp/contests/APG4b/tasks )
    * C++を使った競技プログラミング入門
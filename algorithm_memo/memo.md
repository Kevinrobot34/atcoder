競技プログラミングのメモ \
基本的に蟻本([Amazonのリンク]( https://www.amazon.co.jp/dp/4839941068/ref=cm_sw_em_r_mt_dp_U_ZTWrDb9R924BK ))に書かれているアルゴリズムの実装や関連問題(主にAtCoder)をメモしている。

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

標準出力は当然`print()`
* １行に複数の数を空白区切で出力する時、`ans=[1, 2, 3, 4, 5]`として、
   ```python
   print(' '.join([str(ansi) for ansi in ans]))
   ```
   としても良いが、
   ```python
   print(*ans)
   ```
   の方がスマートな気がする。



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


## 平行二分探索木
**C++**
* set: https://cpprefjp.github.io/reference/set/set.html
* map: https://cpprefjp.github.io/reference/map/map.html

**python** \
そんなものはない。Treapを自分で実装しよう。


## ハッシュテーブル
**C++**
* unordered_map: https://cpprefjp.github.io/reference/unordered_map/unordered_map.html

**python**
* set: https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset
* dict: https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict
    * `key in dict`と書くと早い。`key in dict.keys()`とかやってると$O(N)$になるので注意。



# 探索
## 全探索
競プロでは文字通りの全列挙で解ける問題もしばしば出題されるので、DFS・BFS・bit使って全列挙などパッと書けるようになるのが大事。
また完全な意味での全列挙でなくても、「ある変数$x$を固定するとそれ以外の変数については最適なパターンが決まるので、変数$x$について全探索する」的な解法もしばしばある。

問題
* [ABC045 C - たくさんの数式 / Many Formulas (300点)]( https://atcoder.jp/contests/abc045/tasks/arc061_a )
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
    * [ABC030 C - 飛行機乗り]( https://atcoder.jp/contests/abc030/tasks/abc030_c )
    * [ABC077 C - Snuke Festival (300点)]( https://atcoder.jp/contests/abc077/tasks/arc084_a )
    * [ABC119 D - Lazy Faith (400点)]( https://atcoder.jp/contests/abc119/tasks/abc119_d )
    * [ABC138 E - Strings of Impurity (500点)]( https://atcoder.jp/contests/abc138/tasks/abc138_e )
* 自分でループ書くタイプの二分探索するタイプの問題
    * [ABC063 D - Widespread (400点)]( https://atcoder.jp/contests/abc063/tasks/arc075_b )
    * [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )


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
* [ABC130 E - Common Subsequence (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_e )
    * DPを二元累積和で高速化する
* [ABC075 D - Axis-Parallel Rectangle (400点)]( https://atcoder.jp/contests/abc075/tasks/abc075_d )
    * 二次元累積和


## しゃくとり法
https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
問題
* [ABC032 C - 列]( https://atcoder.jp/contests/abc032/tasks/abc032_c )
    * 典型的なしゃくとり法
* [ABC038 C - 単調増加]( https://atcoder.jp/contests/abc038/tasks/abc038_c )
    * 典型的なしゃくとり法
* [ABC124 D - Handstand (400点)]( https://atcoder.jp/contests/abc124/tasks/abc124_d )
* [ABC130 D - Enough Array (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_d )
    * 典型的なしゃくとり法
* [ABC098 D - Xor Sum 2 (500点)]( https://atcoder.jp/contests/abc098/tasks/arc098_b )


## いもす法
https://imoz.jp/algorithms/imos_method.html

問題
* [ABC035 C - オセロ]( https://atcoder.jp/contests/abc035/tasks/abc035_c )
* [ABC080 D - Recording (400点)]( https://atcoder.jp/contests/abc080/tasks/abc080_d )


## 座標圧縮
問題
* [ABC036 C - 座圧]( https://atcoder.jp/contests/abc036/tasks/abc036_c )
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
    * [ABC044 C - 高橋君とカード / Tak and Cards (300点)]( https://atcoder.jp/contests/abc044/tasks/arc060_a )
    * [ABC082 D - FT Robot (500点)]( https://atcoder.jp/contests/abc082/tasks/arc087_b )
    * [ABC104 D - We Love ABC (400点)]( https://atcoder.jp/contests/abc104/tasks/abc104_d )
    * [ABC118 D - Match Matching (400点)]( https://atcoder.jp/contests/abc118/tasks/abc118_d )
    * [ABC122 D - We Like AGC (400点)]( https://atcoder.jp/contests/abc122/tasks/abc122_d )
    * [ABC132 F - Small Products (600点)]( https://atcoder.jp/contests/abc132/tasks/abc132_f )
    * [ABC135 D - Digits Parade (400点)]( https://atcoder.jp/contests/abc135/tasks/abc135_d )



## bitDP
整数の2進数表記を用いて、サイズNの部分集合を全列挙するなどして行うDPのこと。

例
* 巡回セールスマン問題(TSP)

問題
* [JOI Flag]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0559 )
* [ABC041 D - 徒競走]( https://atcoder.jp/contests/abc041/tasks/abc041_d )
* [ABC113 D - Number of Amidakuji (400点)]( https://atcoder.jp/contests/abc113/tasks/abc113_d )
* [ABC142 E - Get Everything (500点)]( https://atcoder.jp/contests/abc142/tasks/abc142_e )


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

次の簡易的な実装だと$O\left(|V|^2\right)$。$|V| \leq 10^3$で$|E| = O\left(|V|^2\right)$とかだとこっちの方が早かったりする
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
* [ARC E - Cosmic Rays (600点)]( https://atcoder.jp/contests/arc064/tasks/arc064_c )
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
* [ABC061 D - Score Attack (400点)]( https://atcoder.jp/contests/abc061/tasks/abc061_d )
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
正整数$n$の約数の一覧は$O(\sqrt{n})$で取得できる。
```python
def get_divisor(n: int) -> list:
    divisor = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            divisor.append(i)
            if n // i != i:
                divisor.append(n // i)
    # divisor.sort() # if you want sorted divisors
    return divisor
```

## GCD / LCM
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
正整数$n$の素因数分解は[Trial-Division]( https://en.wikipedia.org/wiki/Trial_division )と呼ばれるナイーブなアルゴリズムで$O(\sqrt{n})$で可能。
また一般に、正整数$n$の素因数の個数は$O(\log n)$。
```python
from collections import defaultdict
def factorize(n: int) -> dict:
    f = defaultdict(int)
    while n % 2 == 0:
        f[2] += 1
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            f[p] += 1
            n //= p
        p += 2
    if n != 1:
        f[n] += 1
    return f
```
問題
* [ABC052 C - Factors of Factorial (300点)]( https://atcoder.jp/contests/abc052/tasks/arc067_a )
* [ABC142 D - Disjoint Set of Common Divisors (400点)]( https://atcoder.jp/contests/abc142/tasks/abc142_d )

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
* [ABC042 D - いろはちゃんとマス目 / Iroha and a Grid (400点)]( https://atcoder.jp/contests/abc042/tasks/arc058_b )
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


# 文字列系
## suffix array
 * https://qiita.com/flare/items/20439a1db54b367eea70

## LCP array
* https://blog.shibayu36.org/entry/2017/01/06/103956

## KMP法
長さ$N$の文字列$S$に対して、
* $\mathrm{KMP}[i] = $( 文字列$S[:i]$の接頭辞と接尾辞が最大何文字一致しているか)

を$0\leq i < N$なるすべての$i$について、$O(N)$で計算するアルゴリズム。
```
S  : aabaabaaa
KMP: _010123452 (_=-1)
```
解説
* https://snuke.hatenablog.com/entry/2014/12/01/235807
* http://potetisensei.hatenablog.com/entry/2017/07/10/174908

使い道
* 最小の周期長を求める
    * 「文字列Sの最小の周期長」＝「k 文字ずらしたものが元の文字列と一致するような最小の k (k>0)」
        * 例えば`ababa`の最小の周期長は2
          ```
          ababa
          __ababa
          ```
  * 1-indexedで `i-KMP[i]`
    * 具体例
        ```
        S  : aabaabaaa
        KMP: _010123452 (_=-1)
        mpl: 113333337
        ```
* 文字列検索
    * 文字列`S`の中に`T`が含まれるか検索したい時には、`kmp(T+'#'+S)`をすると良い

```python
def kmp(s):
    n = len(s)
    kmp = [0] * (n+1)
    kmp[0] = -1
    j = -1
    for i in range(n):
        while j >= 0 and s[i] != s[j]:
            j = kmp[j]
        j += 1
        kmp[i+1] = j

    return kmp
```


## Manacherのアルゴリズム
回文関連のやつ
* https://snuke.hatenablog.com/entry/2014/12/02/235837


## Z Algorithm
長さ$N$の文字列$S$に対して、
* $Z[i] = $($S$と$S[i:]$の最長共通接頭辞(LCP)の長さ)

を$0\leq i < N$なるすべての$i$について、$O(N)$で計算するアルゴリズム。例えば具体例はこんな感じ。
```
S:aaabaaaab
Z:921034210
```

使い道
* LCP
* 文字列検索
    * 文字列`S`の中に`T`が含まれるか検索したい時には、`z_algorithm(T+'#'+S)`をすると良い


解説
* https://snuke.hatenablog.com/entry/2014/12/03/214243
* http://codeforces.com/blog/entry/3107

```python
def z_algorithm(s):
    n = len(s)
    z = [0] * n
    z[0] = n

    i = 1
    lcp = 0
    while i < n:
        while i+lcp < n and s[i+lcp] == s[lcp]:
            lcp += 1
        z[i] = lcp

        if lcp == 0:
            i += 1
            continue

        k = 1
        while i+k < n and k+z[k] < lcp:
            z[i+k] = z[k]
            k += 1
        i += k
        lcp -= k

    return z
```

問題
* [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
* [ABC135 F - Strings of Eternity (600点)]( https://atcoder.jp/contests/abc135/tasks/abc135_f )


## Rooling Hash
* https://odan3240.hatenablog.com/entry/2015/02/16/111938
* https://ei1333.github.io/luzhiled/snippets/string/rolling-hash.html
* https://scrapbox.io/pocala-kyopro/ローリングハッシュ
* http://perogram.hateblo.jp/entry/rolling_hash
* アリ本 第２版 「4-7 文字列を華麗に扱う」

### ハッシュ関数
そもそもハッシュ関数とは、文字列・数列といった何かしらのデータが与えられた時に、そのデータに対応したなんらかの数値を得るなんらかの操作(関数)のこと。
データをハッシュ関数にかけて得られた数値のことをハッシュ値という。
元データの比較処理が重いような場合(文字列・数列など)、ハッシュ値に変換してから比較することで高速化が望めたりする。

### RollingHashの概要
ただし、ハッシュ値の計算に時間がかかっていては意味がない。
そこで数列に対するハッシュ関数として、高速で便利なのがローリングハッシュである。
ローリングハッシュ(多項式ハッシュ, Karp-Rabin Fingerprint)とは、数列$a ~=~[a_0, ~a_1, ~\cdots,~ a_{m-1} ]$に対して
$$
\begin{align*}
 H(a, b, h) &= \left[~ a_0~b^{m-1} + a_1~b^{m-2} + \cdots  + a_{m-1}~b^{0} ~\right] ~\mathrm{mod}~~ h \\\\
&= \left[~ \sum_{i=0}^{m-1} a_i ~b^{m-1-i} ~\right] ~\mathrm{mod}~~ h
\end{align*}
$$
と定義されるハッシュ関数のこと。文字列にも適用可能。（ 文字列$S=S_0S_1\cdots S_{m-1}$ を数列$a = \left[\mathrm{ord}(S_0), ~\mathrm{ord}(S_1), ~\cdots, ~\mathrm{ord}(S_{m-1}) \right]$ に変換すれば良い。$\mathrm{ord}(\cdot)$は文字の[アスキーコードを返す関数]( https://docs.python.org/ja/3/library/functions.html#ord )。）

多項式の形なので、**（累積和のようなイメージで）効率的に計算できる**のがミソ。具体的には、長さ$N$の数列$S$に対して$H(S[:i], b, h)$を全ての$i$に対して計算するという前処理$O(N)$を行なっておくと、$S$の任意の部分列$S[l:r]$のハッシュ値を$O(1)$で次式のように計算できるようになる。
$$
H(S[l:r], b, h) = \left[~ H(S[:r], b, h) - H(S[:l], b, h) ~ b^{r-l} ~\right] ~\mathrm{mod}~~ h \\\\
\left(
\begin{align*}
 H(S[:r], b, h) &= \left[~ S_0~b^{r-2} + \cdots + S_{l-1}~b^{r-l} + S_l~b^{r-l-1} + \cdots  + S_{r-1}~b^{0} ~\right] ~\mathrm{mod}~~ h \\\\
H(S[:l], b, h)&= \left[~ S_0~b^{l-2} + \cdots  + S_{l-1}~b^{0} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \right] ~\mathrm{mod}~~ h \\\\
H(S[l:r], b, h)&= \left[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ S_l~b^{r-l-1} + \cdots  + S_{r-1}~b^{0} ~\right] ~\mathrm{mod}~~ h
\end{align*}
\right)
$$



直接文字列を比較するのではなく、効率的に計算されるハッシュ値の比較をすることで処理の高速化を図る。

### ハッシュの衝突について
ハッシュは衝突することもある。
複数の$b$と$h$に対してハッシュを計算するようにしておくことで、衝突する確率を下げるのが比較的容易な対策の一つ。
* https://snuke.hatenablog.com/entry/2017/02/03/035524

```python
class RollingHash:
    def __init__(self, s: str, base: int=1007, mod: int=10**9+7):
        self.s = s
        self.n = len(s)
        self.base = base
        self.mod = mod

        # preprocess
        self.hash_cum = [0] * (self.n + 1) # hash_cum[i] = (hash of s[:i])
        self.base_pow = [1] * (self.n + 1) # base_pow[i] = base ** i
        for i in range(self.n):
            self.hash_cum[i+1] = (self.hash_cum[i] * base + ord(s[i])) % mod
            self.base_pow[i+1] = (self.base_pow[i] * base) % mod

    def get_hash(self, l: int, r: int) -> int: # get hash value of the substring: s[l:r]
        hash_val = self.hash_cum[r] - self.hash_cum[l] * self.base_pow[r-l] % self.mod
        if hash_val < 0:
            hash_val += self.mod
        return hash_val


class RollingHashMulti:
    def __init__(self, s: str, base_list: list=[1007, 2009], mod_list: list=[10**9+7, 10**9+9]):
        self.n = len(base_list)
        self.base_list = base_list
        self.mod_list = mod_list
        self.rh_list = [RollingHash(s, base_list[i], mod_list[i]) for i in range(self.n)]

    def get_hash(self, l: int, r: int) -> tuple:
        return tuple( self.rh_list[i].get_hash(l, r) for i in range(self.n) )

```
ToDo
* `RollingHashBase`という基底クラスを作って、`RollingHashStr`と`RollingHashStrMulti`と`RollingHash2dim`をそれを継承したクラスとして実現する

問題
* [ABC054 B - Template Matching (200点)]( https://atcoder.jp/contests/abc054/tasks/abc054_b )
    * 二次元のRollingHashでも解ける
* [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
    * RollingHashと二分探索


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
* [ABC049 D - 連結 / Connectivity (400点)]( https://atcoder.jp/contests/abc049/tasks/arc065_b )
* [ABC075 C - Bridge (300点)]( https://atcoder.jp/contests/abc075/tasks/abc075_c )
* [ABC097 D - Equals (400点)]( https://atcoder.jp/contests/abc097/tasks/arc097_b )
* [ABC120 D - Decayed Bridges (400点)]( https://atcoder.jp/contests/abc120/tasks/abc120_d )
* [ABC126 E - 1 or 2 (500点)]( https://atcoder.jp/contests/abc126/tasks/abc126_e )
* [ABC131 F - Must Be Rectangular! (600点)]( https://atcoder.jp/contests/abc131/tasks/abc131_f )


## Segment Tree / BIT
* https://www.slideshare.net/iwiwi/ss-3578491
* https://www.creativ.xyz/segment-tree-entrance-999/
* http://koba-e964.hatenablog.com/entry/2016/12/14/214132#f-888cad5c

問題
* [ABC136 F - Enclosed Points (600点)]( https://atcoder.jp/contests/abc136/tasks/abc136_f )



# 何とも言えないけど競プロっぽいやつ
うまく言語化できないけど、競プロっぽい問題はたくさんあるし、慣れないと解けない。
ちょっとずつこれらのまとめもしていきたい。

問題
* ゲーム系
    * [ABC059 D - Alice&Brown (500点)]( https://atcoder.jp/contests/abc059/tasks/arc072_b )
    * [ABC067 D - Fennec VS. Snuke (400点)]( https://atcoder.jp/contests/abc067/tasks/arc078_b )
    * [ABC078 D - ABS (500点)]( https://atcoder.jp/contests/abc078/tasks/arc085_b )
* その他
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
* Pythonは割り算(`/`)するとdoubleの演算になって精度が64bitじゃなくなる
    * https://twitter.com/chokudai/status/1168159665433149440?s=20
* DPの配列の初期値にINFを入れたいときに、`INF = float("inf")`を使うと遅いっぽい
    * 問題に応じて適宜`INF = 10**9`とかにした方が良い
* PythonのListのランダムアクセス（して代入するの）はかなり遅いっぽい。
    * DPなどで
        ```python
        dp[j | c] = min(dp[j] + a, dp[j | c])
        ```
        と書くのであれば、
        ```python
        if dp[j] + a < dp[j | c]:
            dp[j | c] = dp[j] + a
        ```
        と、if文を書いた方が早い。

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

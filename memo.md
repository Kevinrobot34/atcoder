競技プログラミングのメモ


# コンテストサイト
* [AtCoder]( http://atcoder.jp )
    * my account : https://atcoder.jp/users/Kevinrobot34
    * 過去の自分の解答 : https://github.com/Kevinrobot34/atcoder
* [Codeforces]( https://codeforces.com )
    * my account : https://codeforces.com/profile/Kevinrobot34
* [AOJ]( http://judge.u-aizu.ac.jp/onlinejudge/ )
    * my account : http://judge.u-aizu.ac.jp/onlinejudge/user.jsp?id=Kevinrobot34#0

# 入出力

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

# 変数・データ構造
## 文字列
**CPP** \
http://vivi.dyndns.org/tech/cpp/string.html


## 配列

### sort
**C++** \
https://cpprefjp.github.io/reference/algorithm/sort.html \
https://qiita.com/a4rcvv/items/7cd217cc5fafef700dff


**python** \
https://docs.python.org/ja/3.7/howto/sorting.html


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
pythonのheapはmin-heapなことに注意。つまり、
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

# 探索
## 全探索
問題
* [ABC099 C - Strange Bank]( https://atcoder.jp/contests/abc099/tasks/abc099_c )
* [ABC099 D - Good Grid]( https://atcoder.jp/contests/abc099/tasks/abc099_d )
* [ABC104 C - All Green]( https://atcoder.jp/contests/abc104/tasks/abc104_c )
    * bitを使った全探索（各問題を全部解くor全く解かない）
* [ABC107 C - Candles]( https://atcoder.jp/contests/abc107/tasks/arc101_a )
* [ABC114 C - 755]( https://atcoder.jp/contests/abc114/tasks/abc114_c )
* [ABC119 C - Synthetic Kadomatsu]( https://atcoder.jp/contests/abc119/tasks/abc119_c )


### DFS - 深さ優先探索
実装方法
* 再帰関数
* stack

### BFS - 幅優先探索
実装方法
* queue


## 二分探索
https://qiita.com/drken/items/97e37dd6143e33a64c8c

**C++**

**python** \
https://docs.python.org/ja/3/library/bisect.html#bisect.bisect_right

* `bisect.bisect_left(a, x)`
  * 昇順ソート済みlist`a`の中で、`a[index] >= x`という条件を満たす最小の`index`を返す
* `bisect.bisect_right(a, x)`
  * 昇順ソート済みlist`a`の中で、`a[index] > x`という条件を満たす最小の`index`を返す

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
* [ABC119 D - Lazy Faith]( https://atcoder.jp/contests/abc119/tasks/abc119_d )


# アルゴリズム
## いもす法

## 累積和
問題
* [ABC098 C - Attention]( https://atcoder.jp/contests/abc098/tasks/arc098_a )
* [ABC106 D - AtCoder Express 2]( https://atcoder.jp/contests/abc106/tasks/abc106_d )

## Run-length圧縮

## しゃくとり法


# 動的計画法
## DP
問題
* フィボナッチ数列の延長
    * [ABC129 C - Typical Stairs]( https://atcoder.jp/contests/abc129/tasks/abc129_c )
* ナップザック
* その他
    * [ABC132 F - Small Products]( https://atcoder.jp/contests/abc132/tasks/abc132_f )

## 桁DP
問題
* [JOI Flag]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0559 )
* [Zigzag Number]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0570 )
* xor系
    * [ABC117 D - XXOR]( https://atcoder.jp/contests/abc117/tasks/abc117_d )
    * [ABC129 E - Sum Equals Xor]( https://atcoder.jp/contests/abc129/tasks/abc129_e )
        * http://drken1215.hatenablog.com/entry/2019/06/10/150000

# グラフ
## 最短経路
### Dijkstra法
負の辺が存在しないグラフに対して、単一始点最短路問題を$O(|E|\log|V|)$で解けるアルゴリズム。
辺の数が多くないか注意してから使おう。

問題
* 変形Dijkstra
    * [ABC132 E - Hopscotch Addict]( https://atcoder.jp/contests/abc132/tasks/abc132_e )
        * 良問
    * https://yukicoder.me/problems/no/807

### Warshall-Floyd法
全点対最短路問題を$O(|V|^3)$で解けるアルゴリズム。

## 最小全域木


## 木
問題
* 数え上げ
    * [ABC133 E - Virus Tree 2]( https://atcoder.jp/contests/abc133/tasks/abc133_e )


## LCA
https://en.wikipedia.org/wiki/Lowest_common_ancestor

問題
* [ABC133 F - Colorful Tree]( https://atcoder.jp/contests/abc133/tasks/abc133_f )
    * LCAに更にもう一捻りしてあるので難しそう


## その他
問題
* [ABC131 E - Friendships]( https://atcoder.jp/contests/abc131/tasks/abc131_e )

# 数学
## GCD / LCM
最大公約数(GCD - Greatest Common Divisor) と 最小公倍数(LCM - Least Common Multiple)
キーワード
* GCD, LCM
* ユークリッドの互除法
```cpp
int GCD(int a, int b) { return b ? GCD(b, a % b) : a; }
int LCM(int a, int b) { return a * b / GCD(a, b) }
```
```python
def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)
def LCM(a, b):
    return a * b // GCD(a, b)    
```
問題
* [ABC131 C - Anti-Divisor]( https://atcoder.jp/contests/abc131/tasks/abc131_c )

## Combination
combinationの計算を効率よくやるには工夫が必要。\
階乗とその逆元の事前計算をしておくことで高速にcombinationができるようになる。以下のFermatの小定理を使うことで、「素数を法とする時(mod p の時)の$a$の逆元は$a^{p-2}$であることがわかる」ということがポイント。
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

def comb(n, k):
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n-k] % MOD
```


問題
* [ABC110 D - Factorization]( https://abc110.contest.atcoder.jp/tasks/abc110_d )
* [ABC132 D - Blue and Red Balls]( https://atcoder.jp/contests/abc132/tasks/abc132_d )


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
* [ABC097 D - Equals]( https://atcoder.jp/contests/abc097/tasks/arc097_b )
* [ABC120 D - Decayed Bridges]( https://atcoder.jp/contests/abc120/tasks/abc120_d )
* [ABC131 F - Must Be Rectangular!]( https://atcoder.jp/contests/abc131/tasks/abc131_f )

## Segment Tree


# Others
* pythonの謎の`RE`について。
    * 可能性の一つとして`RecursionError: maximum recursion depth exceeded in comparison` がある。
    * 対策は以下。
       ```python
      import sys
      sys.setrecursionlimit(100000)
      ```

# Reference
* [AtCoder 版！蟻本 (初級編)]( https://qiita.com/drken/items/e77685614f3c6bf86f44 )

**Python関連**
* [Pythonで競技プログラミング]( https://qiita.com/knakajima3027/items/b871631b8997a6d67223 )
    * pythonの各種アルゴリズムなどがまとまってる
* [Pythonistaなら知らないと恥ずかしい計算量のはなし]( https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb )
    * PythonのList, Deque, Dictの計算量の話

**C++関連**
* [Macで#include<bits/stdc++.h>を導入]( http://perogram.hateblo.jp/entry/2019/04/15/094647 )
    * Macだとそのままではcppで`#include<bits/stdc++.h>`は使えないが、自分で`/usr/local/include/bits/stdc++.h`を作ってしまえば使えるようになる。
    * https://gist.github.com/Kevinrobot34/cd95d23d6917c30a39df854481d7468e
* [AtCoder Programming Guide for beginners (APG4b)]( https://atcoder.jp/contests/APG4b/tasks )
    * C++を使った競技プログラミング入門

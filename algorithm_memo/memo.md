競技プログラミングのメモ \
基本的に蟻本([Amazonのリンク]( https://www.amazon.co.jp/dp/4839941068/ref=cm_sw_em_r_mt_dp_U_ZTWrDb9R924BK ))に書かれているアルゴリズムの実装や関連問題(主にAtCoder)をメモしている。

# コンテストサイト
* [AtCoder]( http://atcoder.jp )
    * my account : https://atcoder.jp/users/Kevinrobot34
        * [AtCoder Problems]( https://kenkoooo.com/atcoder/#/user/Kevinrobot34 )
            * 似た難易度の問題を探すのに役立つ。便利。
        * [AtCoder Scores]( http://atcoder-scores.herokuapp.com/?user=Kevinrobot34 )
        * [AtCoder Tags]( https://atcoder-tags.herokuapp.com/graph/Kevinrobot34? )
            * 特定ジャンルの問題を探したいときに参考になる。
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
* [ABC137 D - Summer Vacation (400点)]( https://atcoder.jp/contests/abc137/tasks/abc137_d )


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
* [ABC029 C - Brute-force Attack]( https://atcoder.jp/contests/abc029/tasks/abc029_c )
* [ABC045 C - たくさんの数式 / Many Formulas (300点)]( https://atcoder.jp/contests/abc045/tasks/arc061_a )
* [ABC062 C - Chocolate Bar (400点)]( https://atcoder.jp/contests/abc062/tasks/arc074_a )
* [ABC080 C - Shopping Street (300点)]( https://atcoder.jp/contests/abc080/tasks/abc080_c )
* [ABC099 C - Strange Bank (300点)]( https://atcoder.jp/contests/abc099/tasks/abc099_c )
* [ABC099 D - Good Grid (400点)]( https://atcoder.jp/contests/abc099/tasks/abc099_d )
* [ABC107 C - Candles (300点)]( https://atcoder.jp/contests/abc107/tasks/arc101_a )
* [ABC112 C - Pyramid (300点)]( https://atcoder.jp/contests/abc112/tasks/abc112_c )
* [ABC128 D - equeue (400点)]( https://atcoder.jp/contests/abc128/tasks/abc128_d )
* [ABC144 C - Walk on Multiplication Table (300点)]( https://atcoder.jp/contests/abc144/tasks/abc144_c )
* [ABC145 C - Average Length (300点)]( https://atcoder.jp/contests/abc145/tasks/abc145_c )
* bit全探索
    * [ABC104 C - All Green (300点)]( https://atcoder.jp/contests/abc104/tasks/abc104_c )
    * [ABC147 C - HonestOrUnkind2 (300点)]( https://atcoder.jp/contests/abc147/tasks/abc147_c )

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
* [ABC007 C - 幅優先探索]( https://atcoder.jp/contests/abc007/tasks/abc007_3 )
    * 典型的な幅優先探索の問題
* [ABC088 D - Grid Repainting (400点)]( https://atcoder.jp/contests/abc088/tasks/abc088_d )
* [AGC033 A - Darker and Darker (300点)]( https://atcoder.jp/contests/agc033/tasks/agc033_a )


## 二分探索
https://qiita.com/drken/items/97e37dd6143e33a64c8c

### ソート済み配列を探索するタイプの二分探索
`lower_bound`や`bisect_left`を使う

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
    * [ABC143 D - Triangles (400点)]( https://atcoder.jp/contests/abc143/tasks/abc143_d )


### 答えを決め打つタイプの二分探索
https://betrue12.hateblo.jp/entry/2019/05/11/013403

「答えを決め打つ」タイプの二分探索で問題を解くために必要な条件は
* 「ある値`x`に対して、ある条件を満たすことができるか」という判定問題が解きやすい
* 上記の判定問題の答えに単調性があるか（Yes/Noの境界が一つか）



いくつか典型のパターンがある
* 「〜〜を満たす最大(最小値)値を求めよ」
* 「〜〜の最大値の最小化（最小値の最大化）」
    * 「〜〜の最大値をX以下にできるか」「任意の〜〜をX以下にできるか」などと言い換えて、二分探索に持ち込む
* 「平均の最大化」
    * 「数列`{x[i]}`の平均値が`a`」は「数列`{x[i]-a}`の総和が0」
* 「K番目の要素の値」
    * 「K番目の要素の値がX以下である」と「X以下の要素がK個以上ある」は同値
    * 「X以下の要素がK個以上ある」という判定問題を解く
        * 単調性は「K番目の要素の値がX以下である」に戻っと考えるとほぼ自明
* 「方程式の解を一つだけ求めよ」
    * 条件(True/False)の切り替わる境界（方程式の解）が複数あっても、それを一つ見つけるだけで良いなら二分探索が使える。
    * こういう方程式の数値的な解析は「二分法」というっぽい？

```python
def check(x):
    # xが条件を満たすか判定する関数
    pass

lb = -1    # False
ub = hoge  # True
while ub - lb > 1:
    mid = (ub + lb) // 2
    if check(mid):
        ub = mid
    else:
        lb = mid
# lbがFalseの最大、ubがTrueの最小
```

問題
* 「〜〜を満たす最大(最小)値を求めよ」的な問題
    * [ABC020 C - 壁抜け]( https://atcoder.jp/contests/abc020/tasks/abc020_c )
    * [ABC063 D - Widespread (400点)]( https://atcoder.jp/contests/abc063/tasks/arc075_b )
    * [ABC144 E - Gluttony (500点)]( https://atcoder.jp/contests/abc144/tasks/abc144_e )
    * [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
        * RollingHashと組み合わせた二分探索
    * [ABC146 C - Buy an Integer (300点)]( https://atcoder.jp/contests/abc146/tasks/abc146_c )
* 「〜〜の最大値の最小化（最小値の最大化）」
    * [ABC023 D - 射撃王]( https://atcoder.jp/contests/abc023/tasks/abc023_d )
    * [ARC003 C - 暗闇帰り道]( https://atcoder.jp/contests/arc003/tasks/arc003_3 )
* 「平均の最大化」
    * [ABC034 D - 食塩水]( https://atcoder.jp/contests/abc034/tasks/abc034_d )
* 「K番目の要素の値」
    * [ABC107 D - Median of Medians (700点)]( https://atcoder.jp/contests/abc107/tasks/arc101_b )
    * [ARC037 C - 億マス計算]( https://atcoder.jp/contests/arc037/tasks/arc037_c )
* 「方程式の解を一つだけ見つける問題」
    * [ABC026 D - 高橋君ボール1号]( https://atcoder.jp/contests/abc026/tasks/abc026_d )



## 半分全列挙




# アルゴリズム
## 貪欲
[AtCoder 版！蟻本 (初級編) : 2-2 猪突猛進！ "貪欲法"]( https://qiita.com/drken/items/e77685614f3c6bf86f44#2-2-%E7%8C%AA%E7%AA%81%E7%8C%9B%E9%80%B2-%E8%B2%AA%E6%AC%B2%E6%B3%95 )

問題
* [ABC011 C - 123引き算]( https://atcoder.jp/contests/abc011/tasks/abc011_3 )
* [ABC083 C - Multiple Gift (300点)]( https://atcoder.jp/contests/abc083/tasks/arc088_a )
* [ABC141 D - Powerful Discount Tickets (400点)]( https://atcoder.jp/contests/abc141/tasks/abc141_d )


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
* [ABC146 E - Rem of Sum is Num (500点)]( https://atcoder.jp/contests/abc146/tasks/abc146_e )
    * 累積和的な見方をして、条件の式を変形すると見えてくるものがある
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
* [ABC139 F - Engines (600点)]( https://atcoder.jp/contests/abc139/tasks/abc139_f )


## いもす法
https://imoz.jp/algorithms/imos_method.html

問題
* [ABC014 C - AtColor]( https://atcoder.jp/contests/abc014/tasks/abc014_3 )
* [ABC035 C - オセロ]( https://atcoder.jp/contests/abc035/tasks/abc035_c )
* [ABC080 D - Recording (400点)]( https://atcoder.jp/contests/abc080/tasks/abc080_d )


## 座標圧縮
```python
def compress_coordinate(x: list, key=None, reverse=False):
    zipped = {}
    unzipped = {}
    for i, xi in enumerate(sorted(set(x), key=None, reverse=reverse)):
        zipped[xi] = i
        unzipped[i] = xi
    return zipped, unzipped
```

問題
* [ARC008 D - タコヤキオイシクナール]( https://atcoder.jp/contests/arc008/tasks/arc008_4 )
    * メインテーマはセグツリーだが、座標圧縮の必要性も感じられる問題
* [ABC036 C - 座圧]( https://atcoder.jp/contests/abc036/tasks/abc036_c )
* [ABC113 C - ID (300点)]( https://atcoder.jp/contests/abc113/tasks/abc113_c )


## Run-length圧縮


## 繰り返し二乗法・ダブリング




# 動的計画法
メモ化再帰とか漸化式立てて解くやつ。
[Educational DP Contest]( https://atcoder.jp/contests/dp )とか練習になりそうだし解きたい

## 典型的なDP
いろんなパターンがある。それぞれの詳細については別途記載。
* ナップザック
* [LIS - 最長増加部分列]( https://github.com/Kevinrobot34/atcoder/blob/master/algorithm_memo/LIS.md )

問題
* フィボナッチ数列の延長
  * [ABC129 C - Typical Stairs (300点)]( https://atcoder.jp/contests/abc129/tasks/abc129_c )
* ナップザック問題系
    * [ABC032D - ナップサック問題]( https://atcoder.jp/contests/abc032/tasks/abc032_d )
    * [ABC060 D - Simple Knapsack (400点)]( https://atcoder.jp/contests/abc060/tasks/arc073_b )
    * [ABC145 E - All-you-can-eat (500点)]( https://atcoder.jp/contests/abc145/tasks/abc145_e )
* LIS (Longest Increasing Subsequence)系
    * [ABC006 D - トランプ挿入ソート]( https://atcoder.jp/contests/abc006/tasks/abc006_4 )
    * [ABC134 E - Sequence Decomposing (500点)]( https://atcoder.jp/contests/abc134/tasks/abc134_e )
* DAG上のDP
    * [ABC144 F - Fork in the Road (600点)]( https://atcoder.jp/contests/abc144/tasks/abc144_f )
* tree上のDP
    * [ABC036 D - 塗り絵]( https://atcoder.jp/contests/abc036/tasks/abc036_d )
* その他
    * [ABC011 C - 123引き算]( https://atcoder.jp/contests/abc011/tasks/abc011_3 )
    * [ABC037 D - 経路]( https://atcoder.jp/contests/abc037/tasks/abc037_d )
        * メモ化再帰の練習になる
    * [ABC044 C - 高橋君とカード / Tak and Cards (300点)]( https://atcoder.jp/contests/abc044/tasks/arc060_a )
    * [ABC054 D - Mixing Experiment (400点)]( https://atcoder.jp/contests/abc054/tasks/abc054_d )
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
* http://drken1215.hatenablog.com/entry/2019/02/04/013700
* https://torus711.hatenablog.com/entry/20150423/1429794075

```
dp[i][smaller] :=
  * (smaller = 0) 上からi桁がsと完全一致してる範囲の数で条件を満たしている数
  * (smaller = 1) 上からi桁が既にsより小さい範囲の数で条件を満たしている数
```

問題
* [Zigzag Numbers]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0570 )
* [ABC007 D - 禁止された数字]( https://atcoder.jp/contests/abc007/tasks/abc007_4 )
* [ABC029 D - 1]( https://atcoder.jp/contests/abc029/tasks/abc029_d )
* xor系
  * 2進数表記で、桁ごとに考えると良いことが多い
  * [ABC117 D - XXOR (400点)]( https://atcoder.jp/contests/abc117/tasks/abc117_d )
  * [ABC129 E - Sum Equals Xor (500点)]( https://atcoder.jp/contests/abc129/tasks/abc129_e )
      * http://drken1215.hatenablog.com/entry/2019/06/10/150000




# グラフ
## グラフの基本
グラフの頂点集合を$V$、辺の集合を$E$とする

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
    * メモリが$O(|V|+|E|)$かかる。
* 隣接行列
    * メモリが$O\left(|V|^2\right)$かかる。ワーシャルフロイド(時間計算量$O\left(|V|^3\right)$)が使えるくらいの問題じゃないと使えない。


## 最短経路
### Dijkstra法
負の辺が存在しないグラフに対して、単一始点最短路問題を$O(|E|\log|V|)$で解けるアルゴリズム。
辺の数が多くないか注意してから使おう。

```python
from heapq import heappush, heappop
def dijkstra(graph: list, n: int, v_s: int, INF: int = float('inf')) -> list:
    # graph[v_from] = [(cost, v_to), ...]
    dist = [INF] * n

    dist[v_s] = 0
    heap = [(0, v_s)]  # heap = [(dist[v], v), ...]
    while heap:
        _, v_from = heappop(heap)
        for cost, v_to in graph[v_from]:
            dist_cand = dist[v_from] + cost
            if dist_cand < dist[v_to]:
                dist[v_to] = dist_cand
                heappush(heap, (dist[v_to], v_to))
    return dist
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
* [ABC035 D - トレジャーハント]( https://atcoder.jp/contests/abc035/tasks/abc035_d )
* [ABC132 E - Hopscotch Addict (500点)]( https://atcoder.jp/contests/abc132/tasks/abc132_e )
* [ARC064 E - Cosmic Rays (600点)]( https://atcoder.jp/contests/arc064/tasks/arc064_c )
* [第２回日経コン D - Shortest Path on a Line (600点)]( https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d )
* https://yukicoder.me/problems/no/807


### Bellman-Ford法
単一始点最短路問題を$O(|V| |E|)$で解けるアルゴリズム。
$\text{dist}[i]=$(頂点$i$までの最短路)とした時、

$$ \text{dist}[i] = \min \\{ \text{dist}[j] + \text{cost}_{j\to i}  \\:| \\: (j, i) \in E  \\} $$

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
グラフを表す隣接行列を更新し、全点間の最短経路が入った行列にする。
$d[i][j] = $($i$から$j$への最短経路の長さ)として、初期化は
* $d[i][i] = 0$
* $d[i][j] =\text{INF}~$($i$と$j$の間に辺がないとき)
* $d[i][j] = \text{cost}[i][j]$

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


### 経路復元
最短経路の長さを更新するときに、直前もしくは直後にどの点を通ったかといった情報も更新・保持するようにすればよい。

経路復元付きWarshall-Floydのコードは上のWarshal-Floydの説参照。

* Warshall-Floyd法の経路復元
    * http://zeosutt.hatenablog.com/entry/2015/05/05/045943
    * [ABC051 D - Candidates of No Shortest Paths (400点)]( https://atcoder.jp/contests/abc051/tasks/abc051_d )が参考になる

問題
* [ABC051 D - Candidates of No Shortest Paths (400点)]( https://atcoder.jp/contests/abc051/tasks/abc051_d )

### 最短経路数
最短経路を求める時、どんな手法でも最短経路の配列の緩和処理をしていくはず。
緩和処理する際に、最短経路数も適宜更新するようにすればOK。
* $\text{num}[i] ~=~$(スタート地点から$i$までの最短経路の数)
* 初期化
    * $\text{num}[v_{\rm start}] ~=~ 1$
    * $\text{num}[v_{\rm others}] ~=~ 0$ （なんでもいい）

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
結局辺のソートの部分に一番時間がかかり、$|E| \leq |V|^2$なので$O(|E|\log |E|) = O(|E| \log |V|)$で最小全域木のコストが求まる。
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
* [ABC146 D - Coloring Edges on Tree (400点)]( https://atcoder.jp/contests/abc146/tasks/abc146_d )


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
* Python3.5以降には`math`にgcdは実装してある。https://docs.python.org/ja/3/library/math.html#math.gcd
    * ただし、Python3.4.3では最大公約数を求めるgcdは”math"ではなくて、"fractions"の中にある: `from fractions import gcd`

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
def eratosthenes(n: int) -> list:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n // 2 + 1):
        if is_prime[i]:
            for j in range(2, n // i + 1):
                is_prime[i * j] = False
    return is_prime
```

問題
* [ABC084 D - 2017-like Number (400点)]( https://atcoder.jp/contests/abc084/tasks/abc084_d )


## Permutation
自分で再帰とかで書いても良いけど、permutationとかの生成にはitertoolsが便利。
* https://docs.python.org/ja/3/library/itertools.html
* **ToDo** 早いのかどうか確認
```python
from itertools import permutations
for p in permutations(range(3)):
    print(p)
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)
```


## Combination
$$ _nC_k = \frac{n!}{k!(n-k)!} = \frac{n\cdot (n-1)\cdot \cdots \cdot (n-k+1)}{1\cdot2\cdot \cdots \cdot k} $$
combinationの計算を効率よくやるには工夫が必要。

### DPによる計算
$$
{}_{n+1}C_k = {}_nC_k +  {}_nC _{k-1}
$$
を利用して、combinationのテーブルを作る方法。パスカルの三角形的な表を上の漸化式で作るという話。
$n\leq N$の範囲で、テーブルを作る前処理に$O(N^2)$、${}_n C_k$の計算に$O(1)$の時間がかかる。

### Fermatの小定理を利用した高速な計算
$$ _nC_k = n! \times (k!)^{-1} \times ((n-k)!)^{-1}  $$
上記の式より、階乗とその逆元の事前計算をしておくことで高速にcombinationができるようになる。
以下のFermatの小定理を使うことで、「素数を法とする時(mod p の時)の$a$の逆元は$a^{p-2}$であることがわかる」ということがポイント。
> **Fermatの小定理**
> $p$を素数、$a$を$p$の倍数でない整数とする時、
> $$ a^{p-1} \equiv 1 ~\text{ (mod $p$)} $$
> [ $\Rightarrow$  $p$を素数、$a$を任意の整数とする時、$a^p \equiv a ~\text{ (mod $p$)}$ ]

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
この方法だと$n\leq N$なる${}_n C_k$の計算をできるようにするために、前処理で$O(N\log \text{MOD})$、${}_n C_k$の計算で$O(1)$の時間がかかる。

このままだと$a!$の逆元計算部分の`pow`が遅い。
* $\text{MOD}=10^9+7$に対して、$(a!)^{\text{MOD}-2}$を計算しないといけない。
* ダブリング使った実装だとしても$O(\log \text{MOD})$かかる（多分）。


### 更なる高速化
実はこの$a!$の逆元計算はさらに高速化できる。まず$(a!)^{-1} = ((a-1)!)^{-1} \cdot a^{-1}$と表せるので、$a^{-1}$が高速に計算できれば再帰的に$(a!)^{-1} $の計算が高速にできることになる。
ここで、以下合同式は全てmod $p$として、
$$
\begin{align}
&p = (p//a) \cdot a + (p\\%a) \\\\
\Leftrightarrow~ & (p//a) \cdot a + (p\\%a) \equiv 0 \\\\
\Leftrightarrow~ & (p\\%a) \equiv -(p//a) \cdot a  \\\\
\Leftrightarrow~ & (p\\%a) \cdot a^{-1}  \equiv -(p//a)   \\\\
\Leftrightarrow~ & a^{-1}  \equiv - (p\\%a)^{-1} \cdot (p//a)
\end{align}
$$
（最初の式は$p$を$a$で割った商と余りに分けただけの式）
と表せる。$(p\\%a) < a$であることに注意すると、上式を用いれば$a^{-1}$は1から順次高速に計算できることが分かる。
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
MAX = 7 * 10**5
fact = [1] * (MAX + 1)  # i!
finv = [1] * (MAX + 1)  # (i!)^{-1}
iinv = [1] * (MAX + 1)  # i^{-1}
for i in range(2, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD
    iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * iinv[i] % MOD

def comb(n: int, k: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    return (fact[n] * finv[k] % MOD) * finv[n - k] % MOD
```
この方法だと$n\leq N$なる${}_n C_k$の計算をできるようにするために、前処理で$O(N)$、${}_n C_k$の計算で$O(1)$の時間がかかる。


### 前処理しないシンプルな実装
$$ _nC_k = \frac{n}{1} \cdot \frac{n-1}{2} \cdot \frac{n-2}{3} \cdot\cdots\cdot \frac{n-k+1}{k}  = \prod _{i=1}^{k} (n-i+1)\cdot i^{-1} $$
combinationを**1回求めるだけ**なら以下でもOK。
上記のcombinationの表式を前から愚直に計算していくと同時に、$i^{-1}$を求めていく。
${}_nC_k$の計算に$O(\min(k, n-k))$かかる。
```python
def comb(n: int, k: int, MOD: int) -> int:
    if n < k or n < 0 or k < 0:
        return 0
    k = min(k, n - k)
    if k == 0:
        return 1
    iinv = [1] * (k + 1)
    ans = n
    for i in range(2, k + 1):
        iinv[i] = MOD - iinv[MOD % i] * (MOD // i) % MOD
        ans *= (n + 1 - i) * iinv[i] % MOD
        ans %= MOD
    return ans
```


問題
* [ABC034 C - 経路]( https://atcoder.jp/contests/abc034/tasks/abc034_c )
* [ABC042 D - いろはちゃんとマス目 / Iroha and a Grid (400点)]( https://atcoder.jp/contests/abc042/tasks/arc058_b )
* [ABC110 D - Factorization (400点)]( https://atcoder.jp/contests/abc110/tasks/abc110_d )
* [ABC132 D - Blue and Red Balls (400点)]( https://atcoder.jp/contests/abc132/tasks/abc132_d )
* [ABC145 D - Knight (400点)]( https://atcoder.jp/contests/abc145/tasks/abc145_d )


## bit演算
### bit演算テクニック
* `x`の最下位の1bit分だけ取り出す
    * `(x & (-x))`
    * 負の数は「全てのbitを反転して1を足す」という補数で表現されていることを利用した技
        * BITの実装などに使える

    | $x_{(10)}$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | $x_{(2)}$                  | 00001 | 00010 | 00011 | 00100 | 00101 | 00110 | 00111 | 01000 |
    | $-x_{(2)}$                | 11111 | 11110 | 11101 | 11100 | 11011 | 11010 | 11001 | 11000 |
    | $(x \\& -x)_{(2)}$ | 00001 | 00010 | 00001 | 00100 | 00001 | 00010 | 00001 | 01000 |

* `x|y = x + y - (x & y)`
* `x^y = x + y - 2*(x & y)`


### XOR
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


# 幾何
## 平面幾何
### 二次元ベクトルのクラス
```python
class P2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return P2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return P2(self.x - other.x, self.y - other.y)

    def smul(self, a):
        return P2(self.x * a, self.y * a)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x
```


### 点が線分上にあるか
```python
def on_seg(p1, p2, q) -> bool:
    is_online = (p1 - q).det(p2 - q) == 0
    is_between = (p1 - q).dot(p2 - q) <= 0
    return is_online and is_between
```

### 線分の交差判定
```python
def is_crossing(p1, p2, q1, q2) -> bool:
    ta = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    tb = (p2 - p1).det(p1 - q1) / (p2 - p1).det(q2 - q1)
    return (0.0 <= ta <= 1.0) and (0.0 <= tb <= 1.0)
```
問題
* [ABC016 D - 一刀両断]( https://atcoder.jp/contests/abc016/tasks/abc016_4 )

### 線分の交点
```python
def intersection(p1, p2, q1, q2):
    t = (q2 - q1).det(q1 - p1) / (q2 - q1).det(p2 - p1)
    return p1 + (p2 - p1).smul(t)
```

## 誤差を考慮した計算
* アリ本 P228


# 構築系
https://www.hamayanhamayan.com/entry/2017/08/21/102212

問題
* [ABC069 D - Grid Coloring (400点)]( https://atcoder.jp/contests/abc069/tasks/arc080_b )
* [ABC081 D - Non-decreasing (600点)]( https://atcoder.jp/contests/abc081/tasks/arc086_b )
* [ABC108 D - All Your Paths are Different Lengths (700点)]( https://atcoder.jp/contests/abc108/tasks/arc102_b )


# ゲーム系
https://www.hamayanhamayan.com/entry/2017/02/27/025050

問題
* [ABC046 D - AtCoDeerくんと変なじゃんけん / AtCoDeer and Rock-Paper]( https://atcoder.jp/contests/abc046/tasks/arc062_b )
* [ABC067 D - Fennec VS. Snuke (400点)]( https://atcoder.jp/contests/abc067/tasks/arc078_b )


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
そもそも[ハッシュ関数]( https://ja.wikipedia.org/wiki/ハッシュ関数  )とは、文字列・数列といった何かしらのデータが与えられた時に、そのデータに対応したなんらかの数値を得るなんらかの操作(関数)のこと。
データをハッシュ関数にかけて得られた数値のことをハッシュ値という。
元データの比較処理が重いような場合(文字列・数列など)、ハッシュ値に変換してから比較することで高速化が望めたりする。
$$
\text{HashFunction} : \text{Data(str, series, ...)} \mapsto \text{HashValue}
$$

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
H(S[:l], b, h)&= \left[~ S_0~b^{l-2} + \cdots  + S_{l-1}~b^{0}  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  \right] ~\mathrm{mod}~~ h \\\\
H(S[l:r], b, h)&= \left[  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  S_l~b^{r-l-1} + \cdots  + S_{r-1}~b^{0} ~\right] ~\mathrm{mod}~~ h
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

### シンプルな実装
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


### ちょっと工夫した実装
更に上手に実装すると、
* rank of union (蟻本はこっち)
* size of union (今回はこっち)

を持つこともできる。(参考 : http://drken1215.hatenablog.com/entry/2019/03/03/224600) \
ポイントとしては、`par`という配列を
* 全て-1で初期化。
* rootのnodeについては、`-(size of union)`を保持する。（逆に負の数であればroot。）
* root以外のnodeについては、parentのidを保持する。（逆に正の数であればleaf。）
* (size of union)に簡単にアクセスできるようになったので、merge techniqueとして、 **サイズが大きなものに小さなものを結合する**ようにする。
    * [データ構造をマージする一般的なテク]( https://topcoder.g.hatena.ne.jp/iwiwi/20131226/1388062106 )
        > 大きさに気をつけて小さい方を大きい方にくっつけるという考え方を応用することで，色々な普通のデータ構造にマージ機能を追加することができます．

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
* [ABC040 D - 道路の老朽化対策について]( https://atcoder.jp/contests/abc040/tasks/abc040_d )
    * UnionFindのちょっとした応用問題。Pythonだと際どい。
* [ABC049 D - 連結 / Connectivity (400点)]( https://atcoder.jp/contests/abc049/tasks/arc065_b )
* [ABC075 C - Bridge (300点)]( https://atcoder.jp/contests/abc075/tasks/abc075_c )
* [ABC097 D - Equals (400点)]( https://atcoder.jp/contests/abc097/tasks/arc097_b )
* [ABC120 D - Decayed Bridges (400点)]( https://atcoder.jp/contests/abc120/tasks/abc120_d )
* [ABC126 E - 1 or 2 (500点)]( https://atcoder.jp/contests/abc126/tasks/abc126_e )
* [ABC131 F - Must Be Rectangular! (600点)]( https://atcoder.jp/contests/abc131/tasks/abc131_f )


## Segment Tree
長さ$N$の列に対して、

* ある区間全体に対する演算
* ある点の値の変更

を$O(\log N)$で可能なデータ構造。[モノイド]( https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%8E%E3%82%A4%E3%83%89 )と関わりが深く、面白い。構築は$O(N)$でできる。

具体的な実装の注意点
* 二分木を0-indexedで持つか、1-indexedで持つか。
    * 0-indexedの場合、ノード`k`について
        * left-child : `2*k+1`
        * right-child : `2*k+2`
        * parent : `(k-1) // 2`
    * 1-indexedの場合、ノード`k`について
        * left-child : `2*k`
        * right-child : `2*k+1`
        * parent : `k // 2`
* queryの書き方
    * アリ本的な再帰を用いた実装（こっちの方がわかりやすい）
    * 再帰を使わず、木を登りながら計算する実装（こっちの方がpythonでは早い）


### 抽象化セグメントツリー(0-indexed)
queryを再帰で書いたアリ本的な0-indexed Segment Tree。

```python
class SegmentTree0():
    """
    0-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1 << (n_ - 1).bit_length()
        self.data = [ele_id] * (2 * self.n - 1)
        self.ele_id = ele_id
        self.operation_func = operation_func

    def __getitem__(self, idx):
        return self.data[idx + self.n - 1]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n - 1] = data_init[i]
        for i in range(self.n - 2, -1, -1):
            self.data[i] = self.operation_func(self.data[2 * i + 1],
                                               self.data[2 * i + 2])

    def update(self, idx, x):
        # change idx-th element to x (idx : 0-indexed)
        idx += self.n - 1
        self.data[idx] = x
        while idx > 0:
            idx = (idx - 1) // 2
            self.data[idx] = self.operation_func(self.data[2 * idx + 1],
                                                 self.data[2 * idx + 2])

    def query(self, a, b):
        # query for interval [a, b) (a, b : 0-indexed)
        return self.query_(a, b, 0, 0, self.n)

    def query_(self, a, b, k, l, r):
        if r <= a or b <= l:
            # [a, b)が[l, r)と交差しない
            return self.ele_id
        if a <= l and r <= b:
            # [a, b)が[l, r)を完全に含む
            return self.data[k]
        else:
            # [a, b)と[l, r)は一部被る
            child_l = self.query_(a, b, 2 * k + 1, l, (l + r) // 2)
            child_r = self.query_(a, b, 2 * k + 2, (l + r) // 2, r)
            return self.operation_func(child_l, child_r)

```

### 抽象化セグメントツリー(1-indexed)
queryを再帰ではなくループで書いた1-indexed Segment Tree 。
```python
class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, operation_func):
        self.n = 1 << (n_ - 1).bit_length()   # size
        self.data = [ele_id] * (2 * self.n)   # binary tree
        self.ele_id = ele_id                  # identity element
        self.operation_func = operation_func  # binary operation of monoid

    def __getitem__(self, idx):
        return self.data[idx + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]
        for i in range(self.n - 1, 0, -1):
            self.data[i] = self.operation_func(self.data[2 * i],
                                               self.data[2 * i + 1])

    def update(self, idx, x):
        # change idx-th element to x (idx : 0-indexed)
        idx += self.n
        self.data[idx] = x
        while idx > 1:
            idx = idx >> 1
            self.data[idx] = self.operation_func(self.data[2 * idx],
                                                 self.data[2 * idx + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.operation_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.operation_func(ret, self.data[r])
            # go to parent-nodes
            l = l >> 1
            r = r >> 1
        return ret
```
* https://www.geeksforgeeks.org/segment-tree-efficient-implementation/

### RMQ - Range Minimum Query
```python
INF = (1 << 31) - 1
st_rmq = SegmentTree0(n, INF, lambda a, b: min(a, b))
```
* https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

### RMQ with index
ある範囲の最小値の値とそのindexも必要なqueryに答えなければならない場合、
ただのRMQを改良し、セグ木に`(値, index)`を持たせるようにすれば良い。
`operation_func`も最初の要素の大小を比較するように明記すればOK。

```python
INF = (10**10, -1)
operation_func = lambda a, b: a if a[0] < b[0] else b
st_rmq = SegmentTree0(n, INF, operation_func)
```

### RSQ - Range Sum Query
```python
st_rsq = SegmentTree0(n, 0, lambda a, b: a + b)
```
* https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B


### Range GCD Query
GCDをユークリッドの互除法で適宜書く時、整数に対するGCDはモノイドをなす。単位元は0。
```python
from fractions import gcd
st_gcd = SegmentTree0(n, 0, gcd)
```

* [ABC125 C - GCD on Blackboard (300点)]( https://atcoder.jp/contests/abc125/tasks/abc125_c )

Reference
* https://www.slideshare.net/iwiwi/ss-3578491
  - 秋葉さんによるデータ構造の解説
* [セグメント木について by beet]( http://beet-aizu.hatenablog.com/entry/2017/09/10/132258 )
    * [セグ木の実装例 by beet]( http://beet-aizu.hatenablog.com/entry/2017/09/14/122311 )
    * [セグ木に載せるモノイドまとめ（未完） by beet]( http://beet-aizu.hatenablog.com/entry/2019/03/12/171221 )
    * [遅延伝播セグメント木について]( http://beet-aizu.hatenablog.com/entry/2017/12/01/225955 )
    * [「セグ」で検索した結果 in beetさんブログ]( http://beet-aizu.hatenablog.com/search?q=%E3%82%BB%E3%82%B0 )
* https://www.creativ.xyz/segment-tree-entrance-999/
* https://www.creativ.xyz/segment-tree-abstraction-979/
  - セグツリーの抽象化について
* https://ei1333.github.io/luzhiled/snippets/structure/segment-tree.html
  - セグツリーの抽象化と遅延評価について
* http://koba-e964.hatenablog.com/entry/2016/12/14/214132
* [蟻本　python セグメント木　競技プログラミング　Atcoder]( https://juppy.hatenablog.com/entry/2019/05/02/%E8%9F%BB%E6%9C%AC_python_%E3%82%BB%E3%82%B0%E3%83%A1%E3%83%B3%E3%83%88%E6%9C%A8_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder )
* https://www.onakasuitacity.com/segment-tree-fenwick-tree/

問題
* [ARC008 D - タコヤキオイシクナール]( https://atcoder.jp/contests/arc008/tasks/arc008_4 )
    * 座標圧縮 + 関数の合成についてのsegtree
*  [ABC125 C - GCD on Blackboard (300点)]( https://atcoder.jp/contests/abc125/tasks/abc125_c )
    * Range GCD Queryを解く問題としてSegmentTreeを使うこともできる。
* [第２回日経コン D - Shortest Path on a Line (600点)]( https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d )
    * DPの漸化式更新のためにRMQする
* [ABC146 F - Sugoroku (600点)]( https://atcoder.jp/contests/abc146/tasks/abc146_f )
    * DPの漸化式更新のためにRMQする


## BIT (fenwick tree)
> Fenwick Tree とも呼ばれる。数列に対し, ある要素に値を加える操作と, 区間和を求める操作をそれぞれ対数時間で行うことが出来るデータ構造。セグメント木や平衡二分探索木の機能を制限したものであるが, 実装が非常に単純で定数倍も軽いなどの利点がある。

BITはセグ木を制限したものなので、応用範囲は狭いが、実装が簡単で定数倍が軽いのが特徴らしい。
なので当然BITの問題はセグ木でも出来る。

$v_1, v_2, \cdots, v_N$という数列を考えた時に、

* 前から$m$項分の和の計算: $~ {\rm sum}(m) = \sum_{i=1}^{m} v_i$
    * 特に${\rm sum}(0) = 0$
* 第$i$項に加算: $~ v_i += x$

を$O(\log N)$で可能なデータ構造。
また特に、常に$v_i \geq 0$を満たす場合には

* 二分探索: $~ {\rm sum}({\rm index}) \geq x$を満たす最小のindexを見つける

も$O(\log N)$で可能。

```python
class BIT1():
    """
    Binary Indexed Tree (1-indexed)
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (self.n + 1)
        self.data = [0] * (self.n + 1)

    def build(self, data):
        pass

    def add(self, idx, x):
        # add x to idx-th element
        # idx: 1-indexed
        self.data[idx] += x
        while idx <= self.n:
            self.bit[idx] += x
            idx += (idx & (-idx))

    def sum(self, idx):
        # get sum of [1, idx]
        # idx: 1-indexed
        s = 0
        while idx:
            s += self.bit[idx]
            idx -= (idx & (-idx))
        return s

    def bisect_left(self, w):
        # condition : always all element is not minus
        # return minimum idx where bit.sum(idx) >= w
        if w <= 0:
            return 0
        idx = 0  # self.bit[idx] < w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k <= self.n and self.bit[idx + k] < w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1

    def bisect_right(self, w):
        # condition : always all element is not minus
        # return minimum idx where bit.sum(idx) > w
        if w < 0:
            return 0
        idx = 0  # self.bit[idx] <= w
        k = 1 << ((self.n).bit_length() - 1)
        while k > 0:
            if idx + k <= self.n and self.bit[idx + k] <= w:
                w -= self.bit[idx + k]
                idx += k
            k = k >> 1
        return idx + 1
```

値の範囲($1 \sim N$)が分かっている場合のstd::setライクな使い方ができる。具体的には
* $v_i=~$(数$i$が集合に入っていれば1、そうでなければ0)

として、この数列にBITを適用することで、

* 集合への要素の追加・削除 (add)
* 指定された要素は何番目に小さいか (sum)
* $x$番目に小さい要素は何か (bisect_left)

を全て$O(\log N)$で出来る。
（セグ木でも出来るが、bisect_leftが遅くなる or 実装が面倒）

Reference
* https://ei1333.github.io/luzhiled/snippets/structure/binary-indexed-tree.html
* http://hos.ac/slides/20140319_bit.pdf

問題
* 転倒数([参考]( https://qiita.com/wisteria0410ss/items/296e0daa9e967ca71ed6 ))関連
    * [ARC088 E - Papple Sort (800点)]( https://atcoder.jp/contests/arc088/tasks/arc088_c )
* [ABC136 F - Enclosed Points (600点)]( https://atcoder.jp/contests/abc136/tasks/abc136_f )
* std::setライクな使い方をする問題
    * [AGC005 B - Minimum Sum (400点)]( https://atcoder.jp/contests/agc005/tasks/agc005_b )
    * [ARC033 C - データ構造]( https://atcoder.jp/contests/arc033/tasks/arc033_3 )
    * [ABC140 E - Second Sum (500点)]( https://atcoder.jp/contests/abc140/tasks/abc140_e )

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
    * `sys.stdin.buffer.readline` も最近見かける。こいつは一体...???
* pythonでtupleのlistやlistのlistをソートするのはそもそも遅い。keyにitemgetterを指定すると速くなったりする。
    ```python
    from operator import itemgetter
    x = [(1,2), (3, 4), (2, 5), (1, 0), (5, 2)]
    x.sort(key=itemgetter(0))
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
* [「Pythonで競プロ」という選択について]( https://maspypy.com/atcoder-%e6%a9%992400%e3%81%ab%e3%81%aa%e3%82%8a%e3%81%be%e3%81%97%e3%81%9f#toc8 )

**C++関連**
* [Macで#include<bits/stdc++.h>を導入]( http://perogram.hateblo.jp/entry/2019/04/15/094647 )
    * Macだとそのままではcppで`#include<bits/stdc++.h>`は使えないが、自分で`/usr/local/include/bits/stdc++.h`を作ってしまえば使えるようになる。
    * https://gist.github.com/Kevinrobot34/cd95d23d6917c30a39df854481d7468e
* [AtCoder Programming Guide for beginners (APG4b)]( https://atcoder.jp/contests/APG4b/tasks )
    * C++を使った競技プログラミング入門

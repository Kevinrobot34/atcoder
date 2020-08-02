競技プログラミングのメモ \
基本的に蟻本([Amazonのリンク]( https://www.amazon.co.jp/dp/4839941068/ref=cm_sw_em_r_mt_dp_U_ZTWrDb9R924BK ))に書かれているアルゴリズムの実装や関連問題(主にAtCoder)をメモしている。

ここでは主にPythonでメモをする


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


# Chrome拡張について
[Tampermonkey]( https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=ja )を使うと、いろんな便利機能を追加できる

* [ac-predictor]( https://greasyfork.org/ja/scripts/369954-ac-predictor )
    * 順位表にパフォーマンス・レート変化を追記してくれるやつ
* [AtCoderPerformanceColorizer]( https://greasyfork.org/ja/scripts/371693-atcoderperformancecolorizer )
    * 成績表ページでパフォーマンスとレートに色をつけてくれるやつ
* [AtCoder Submission Status]( https://greasyfork.org/ja/scripts/383817-atcoder-submission-status )
    * SubmissionページでテストケースのAC/WAの統計情報を表示してくれるやつ


# 入出力
基本的に競技プログラミングは**標準入力**から特定のフォーマットの入力を受け取り、
**標準出力** から特定のフォーマットに従って出力をする。


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
$ python hoge.py < test.txt
```
とすると、`test.txt`の内容を標準入力として入力しファイルを実行することができる。



# 基本的なデータ構造
## 文字列

pythonのstringはimmutableだぞっ。
https://qiita.com/Amtkxa/items/a03dabe050d8c648f098

### char <-> ascii
* char -> ascii : [ord(c)]( https://docs.python.org/ja/3/library/functions.html#ord )
* ascii -> char :  [chr(i)]( https://docs.python.org/ja/3/library/functions.html#chr )
```python
print(ord('a')) # 97
print(chr(98))  # b
```

### string <-> int
```python
print(int('123'))
print(str(123))
```


## 配列

### sort
$`O(N\log N)`$でソート済み配列を取得する。

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

https://docs.python.org/ja/3/library/collections.html#collections.deque \
`append(i)`, `appendleft(i)`, `pop()`, `popleft()`, が$`O(1)`$で出来る。
* > list オブジェクトでも(dequeと)同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします。
* listでもlast要素のpop（つまりただの`.pop()`）であれば$`O(1)`$。https://wiki.python.org/moin/TimeComplexity

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

問題
* [ABC158 D - String Formation (400点)]( https://atcoder.jp/contests/abc158/tasks/abc158_d )


## stack
LIFO(Last In First Out)なコンテナ。
DFSの実装などに使える。再帰関数でも同様な動作。

stackはない。dequeをよしなに使うとよい。 \
listの`append(hoge)`と`pop()`を使うことでも実装可能([参考：リストをスタックとして使う]( https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-stacks ))。


## queue
FIFO(First In First Out)なコンテナ。待ち行列とも。
BFSの実装などに使える。

queueはない（`queue.Queue`は並行実行のためのmoduleで、純粋なデータ型ではない）。dequeをよしなに使うのが良さそう（[参考：リストをキューとして使う]( https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-queues )）。


## priority_queue
優先度付きキュー。挿入された順番通りにpopするのではなく(FIFOではなく)、優先度の高い要素から先に取り出すようになっているキュー。 \
[二分ヒープ]( https://ja.wikipedia.org/wiki/二分ヒープ )を用いて実現している。

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
* [ARC028 B - 特別賞]( https://atcoder.jp/contests/arc028/tasks/arc028_2 )


## 平行二分探索木
C++の`set/map`に相当するもの。
Pythonにそんなものはない。対処法はいくつかある。

1. Treapなどを自分で実装する
2. BIT(+ 座標圧縮)で代用する
3. priority_queueを２本使う（参考：[【Python】平衡二分木が必要な時に代わりに何とかするテク【競プロ】]( https://qiita.com/Salmonize/items/638da118cd621d2628d1 )）

    ```python
    class PseudoSet():
        def __init__(self):
            self.s = []  # set
            self.e = []  # erase candidate

        def insert(self, x):
            heappush(self.s, x)

        def erase(self, x):
            heappush(self.e, x)

        def get_min(self):
            while self.e and self.e[0] == self.s[0]:
                _ = heappop(self.s)
                _ = heappop(self.e)
            return self.s[0] if len(self.s) > 0 else None
    ```


## ハッシュテーブル
* set: https://docs.python.org/ja/3/library/stdtypes.html#set-types-set-frozenset
* dict: https://docs.python.org/ja/3/library/stdtypes.html#mapping-types-dict
    * `key in dict`と書くと早い。`key in dict.keys()`とかやってると$`O(N)`$になるので注意。



# 探索
## 全探索
競プロでは文字通りの全列挙で解ける問題もしばしば出題されるので、DFS・BFS・bit使って全列挙などパッと書けるようになるのが大事。
また完全な意味での全列挙でなくても、「ある変数$`x`$を固定するとそれ以外の変数については最適なパターンが決まるので、変数$`x`$について全探索する」的な解法もしばしばある。

問題
* [ABC029 C - Brute-force Attack]( https://atcoder.jp/contests/abc029/tasks/abc029_c )
* [ABC031 D - 語呂合わせ]( https://atcoder.jp/contests/abc031/tasks/abc031_d )
    * 3bitの全探索
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
* [ABC165 C - Many Requirements (300点)]( https://atcoder.jp/contests/abc165/tasks/abc165_c )
* [ARC034 B - 方程式]( https://atcoder.jp/contests/arc034/tasks/arc034_2 )
* [JSUTC202004 C - Numbering Blocks (300点)]( https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_c )
* [エイジング2020 C - XYZ Triplets (300点)]( https://atcoder.jp/contests/aising2020/tasks/aising2020_c )
* bit全探索
    * [ABC002 D - 派閥]( https://atcoder.jp/contests/abc002/tasks/abc002_4 )
    * [ABC104 C - All Green (300点)]( https://atcoder.jp/contests/abc104/tasks/abc104_c )
    * [ABC128 C - Switches (300点)]( https://atcoder.jp/contests/abc128/tasks/abc128_c )
    * [ABC147 C - HonestOrUnkind2 (300点)]( https://atcoder.jp/contests/abc147/tasks/abc147_c )
    * [ABC159 E - Dividing Chocolate (500点)]( https://atcoder.jp/contests/abc159/tasks/abc159_e )
        * bit全探索+貪欲
        * ちょっと難しい
    * [ABC167 C - Skill Up (300点)]( https://atcoder.jp/contests/abc167/tasks/abc167_c )
    * [ABC173 C - H and V (300点)]( https://atcoder.jp/contests/abc173/tasks/abc173_c )
    * [ARC007 C - 節約生活]( https://atcoder.jp/contests/arc007/tasks/arc007_3 )

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
* [ABC025 C - 双子と○×ゲーム]( https://atcoder.jp/contests/abc025/tasks/abc025_c )
    * ゲーム木の全探索
* [ABC007 C - 幅優先探索]( https://atcoder.jp/contests/abc007/tasks/abc007_3 )
    * 典型的な幅優先探索の問題
* [ABC088 D - Grid Repainting (400点)]( https://atcoder.jp/contests/abc088/tasks/abc088_d )
* [AGC033 A - Darker and Darker (300点)]( https://atcoder.jp/contests/agc033/tasks/agc033_a )
* [ABC151 D - Maze Master (400点)]( https://atcoder.jp/contests/abc151/tasks/abc151_d )
* [ABC168 D - .. (Double Dots) (400点)]( https://atcoder.jp/contests/abc168/tasks/abc168_d )


## 二分探索
[二分探索アルゴリズムを一般化 〜 めぐる式二分探索法のススメ 〜]( https://qiita.com/drken/items/97e37dd6143e33a64c8c )

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
    * まず「K番目の要素の値がX以下である」という判定問題を考えると、`X`を二分探索可能。
        * この判定問題はほぼ自明に単調生がある。
        * さらに以下のように言い換えが可能なので、解きやすい。
            * 「K番目の要素の値がX以下である」と「X以下の要素がK個以上ある」は同値
            * 「X以下の要素がK個以上ある」という判定問題を解く
* 「方程式の解を一つだけ求めよ」
    * 条件(True/False)の切り替わる境界（方程式の解）が複数あっても、 **それを一つ見つけるだけ** で良いなら二分探索が使える。
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
* bisect_leftとほぼ同じだけど自分で書かないといけない問題
    * [JSUTC202004 D - Calculating GCD (400点)]( https://atcoder.jp/contests/judge-update-202004/tasks/judge_update_202004_d )
* 「〜〜を満たす最大(最小)値を求めよ」的な問題
    * [ABC020 C - 壁抜け]( https://atcoder.jp/contests/abc020/tasks/abc020_c )
    * [ABC063 D - Widespread (400点)]( https://atcoder.jp/contests/abc063/tasks/arc075_b )
    * [ABC144 E - Gluttony (500点)]( https://atcoder.jp/contests/abc144/tasks/abc144_e )
    * [ABC141 E - Who Says a Pun? (500点)]( https://atcoder.jp/contests/abc141/tasks/abc141_e )
        * RollingHashと組み合わせた二分探索
    * [ABC146 C - Buy an Integer (300点)]( https://atcoder.jp/contests/abc146/tasks/abc146_c )
    * [AGC041 B - Voting Judges (700点)]( https://atcoder.jp/contests/agc041/tasks/agc041_b )
* 「〜〜の最大値の最小化（最小値の最大化）」
    * [ABC023 D - 射撃王]( https://atcoder.jp/contests/abc023/tasks/abc023_d )
    * [ABC149 E - Handshake (500点)]( https://atcoder.jp/contests/abc149/tasks/abc149_e )
        * 問題の言い換えが難しい
    * [ARC003 C - 暗闇帰り道]( https://atcoder.jp/contests/arc003/tasks/arc003_3 )
    * [ARC049 B - 高橋ノルム君]( https://atcoder.jp/contests/arc049/tasks/arc049_b )
* 「平均の最大化」
    * [ABC034 D - 食塩水]( https://atcoder.jp/contests/abc034/tasks/abc034_d )
* 「K番目の要素の値」
    * [ABC107 D - Median of Medians (700点)]( https://atcoder.jp/contests/abc107/tasks/arc101_b )
    * [ARC037 C - 億マス計算]( https://atcoder.jp/contests/arc037/tasks/arc037_c )
    * [ABC155 D - Pairs (400点)]( https://atcoder.jp/contests/abc155/tasks/abc155_d )
        * ARC037 Cの難しいVer
        * 地味に計算が重いので、尺取と組み合わせて高速化が必要
* 「方程式の解を一つだけ見つける問題」
    * [ABC026 D - 高橋君ボール1号]( https://atcoder.jp/contests/abc026/tasks/abc026_d )
* 幾何との組み合わせ
    * [ABC151 F - Enclose All (600点)]( https://atcoder.jp/contests/abc151/tasks/abc151_f )
        * 最小包含円の半径を求める問題だが、「求める半径が$R$以下である」という判定問題に落とし込むのが結構難しい
    * [ABC157 F - Yakiniku Optimization Problem (600点)]( https://atcoder.jp/contests/abc157/tasks/abc157_f )
        * 「時間 $`t`$ 経った後、肉が$`K`$枚以上焼けてることはありあえるか」という判定問題に落とし込めばOK
        * ABC151FもABC157Fも、「二円の交点を列挙しておけばそれが解の候補となる」ことがポイント



## 半分全列挙
$`O(2^N)`$の全探索は間に合わないが、$`O(2^{N/2})`$の探索は間に合うときの解法。
半分に関しては全探索(全列挙)し、もう一方のグループについてはハッシュテーブル・二分探索・貪欲法などで高速に処理をする。
問題
* [ABC018 D - バレンタインデー]( https://atcoder.jp/contests/abc018/tasks/abc018_4 )
* [ABC032 D - ナップサック問題]( https://atcoder.jp/contests/abc032/tasks/abc032_d )
    * 重さと価値に制限のないナップザック問題の場合、DPはできないが、荷物が少なければ半分全列挙で解ける
* [ARC017 C - 無駄なものが嫌いな人]( https://atcoder.jp/contests/arc017/tasks/arc017_3 )
* [AGC026 C - String Coloring (600点)]( https://atcoder.jp/contests/agc026/tasks/agc026_c )
    * ハッシュテーブル(Pythonのset/dict)を上手に使う
* [東京海上日動コン2020 D - Knapsack Queries on a tree (700点)]( https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_d )
    * 木の上で、半分全列挙を使ったナップザック問題を解く問題
* [CodeThanksFestival2017 G - Mixture Drug (600点)]( https://atcoder.jp/contests/code-thanks-festival-2017-open/tasks/code_thanks_festival_2017_g )



# アルゴリズム
## 貪欲
[AtCoder 版！蟻本 (初級編) : 2-2 猪突猛進！ "貪欲法"]( https://qiita.com/drken/items/e77685614f3c6bf86f44#2-2-%E7%8C%AA%E7%AA%81%E7%8C%9B%E9%80%B2-%E8%B2%AA%E6%AC%B2%E6%B3%95 )

問題
* [ABC011 C - 123引き算]( https://atcoder.jp/contests/abc011/tasks/abc011_3 )
* [ABC083 C - Multiple Gift (300点)]( https://atcoder.jp/contests/abc083/tasks/arc088_a )
* [ABC091 C - 2D Plane 2N Points (400点)]( https://atcoder.jp/contests/abc091/tasks/arc092_a )
* [ABC141 D - Powerful Discount Tickets (400点)]( https://atcoder.jp/contests/abc141/tasks/abc141_d )
* [ABC149 D - Prediction and Restriction (400点)]( https://atcoder.jp/contests/abc149/tasks/abc149_d )
* [ABC155 E - Payment (500点)]( https://atcoder.jp/contests/abc155/tasks/abc155_e )
    * こういう貪欲法苦手。DPでもできるので、それも要確認。
* [ABC167 F - Bracket Sequencing (600点)]( https://atcoder.jp/contests/abc167/tasks/abc167_f )
    * 類題：[ARC053 C - 魔法使い高橋君]( https://atcoder.jp/contests/arc053/tasks/arc053_c )
* [ARC053 C - 魔法使い高橋君]( https://atcoder.jp/contests/arc053/tasks/arc053_c )
    * 良い問題
    * 解説がわかりやすい
* [エイジング2020 E - Camel Train (500点)]( https://atcoder.jp/contests/aising2020/tasks/aising2020_e )
    * 難しい
* [キーエンス2020 B - Robot Arms (200点)]( https://atcoder.jp/contests/keyence2020/tasks/keyence2020_b )
* [M-SOLUTIONS 2020 D - Road to Millionaire (400点)]( https://atcoder.jp/contests/m-solutions2020/tasks/m_solutions2020_d )


## 累積和
数列$$a_0, a_1, ..., a_{N-1}$$がある時に、$$\sum_{i=l}^r a_i$$を計算する問題を考える。
ナイーブに足し算をすると$$O(N)$$かかりうる。
しかしあらかじめ$$b_0 = 0, ~~ b_{n+1} = \sum_{j=0}^{n} a_j = b_n + a_n$$という数列を用意しておくと、
$$\sum_{i=l}^r a_i = b_{r+1} - b_l$$と$$O(1)$$で計算できる。

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

二次元累積和
```python
for i in range(n):
    for j in range(n):
        ds[i + 1][j + 1] = ds[i + 1][j] + ds[i][j + 1] - ds[i][j] + d[i][j]
```


問題
* [ABC084 D - 2017-like Number (400点)]( https://atcoder.jp/contests/abc084/tasks/abc084_d )
* [ABC098 C - Attention (300点)]( https://atcoder.jp/contests/abc098/tasks/arc098_a )
* [ABC106 D - AtCoder Express 2 (400点)]( https://atcoder.jp/contests/abc106/tasks/abc106_d )
* [ABC122 C - GeT AC (300点)]( https://atcoder.jp/contests/abc122/tasks/abc122_c )
* [ABC146 E - Rem of Sum is Num (500点)]( https://atcoder.jp/contests/abc146/tasks/abc146_e )
    * 累積和的な見方をして、条件の式を変形すると見えてくるものがある
* 二次元累積和
    * [ABC005 D - おいしいたこ焼きの焼き方]( https://atcoder.jp/contests/abc005/tasks/abc005_4 )
    * [ABC075 D - Axis-Parallel Rectangle (400点)]( https://atcoder.jp/contests/abc075/tasks/abc075_d )
    * [ABC086 D - Checker (500点)]( https://atcoder.jp/contests/abc086/tasks/arc089_b )
    * [ABC130 E - Common Subsequence (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_e )
        * DPを二元累積和で高速化する


## しゃくとり法
* [しゃくとり法 (尺取り法) の解説と、それを用いる問題のまとめ]( https://qiita.com/drken/items/ecd1a472d3a0e7db8dce )
* [えびちゃんさんのツイート]( https://twitter.com/rsk0315_h4x/status/1213808364225871873?s=21 )
    *  > 尺取り，できるだけ区間を長くしたいときは左端をループ変数にして，短くしたいときは右端をループ変数にしてる気がする
        > ```
        > for (固定したい方) {
        >   while (条件がいい感じ)
        >     ++固定されない方;
        > }
        > ```

ある長さ`N`の配列`a[i]`を考える。
任意の`i`に対し、条件を満たすindexの範囲(`[0, j)`や`[j, N)`)の境界`j`を求めたい。
もし`j`が`i`に対して単調な振る舞いをする場合、これを$`O(N)`$で求めることができる。

```python
right = 1
for left in range(n):
    while right < n and (some conditions):
        # some process
        right += 1

    # Segment [left, right) satisfies conditions
    # someprocess
```

典型的な例
* 正数からなる数列において、総和がK以上となっている連続する部分列の個数
    * 任意の`i`に対して初めて`sum(a[i:j]) >= K`となる`j`を知りたい
* 正数からなる配列において、2つの要素の積がK以上となるペアの数
    * 昇順ソート済みとする
    * 任意の`i`に対して、`a[j] >= K / a[i]`となる`j`を知りたい
* ある数列において、狭義単調増加となっている連続する部分列の個数
* ある数列において重複する項がないような連続する部分列の列挙
* スライド最小値

問題
* [ABC017 D - サプリメント]( https://atcoder.jp/contests/abc017/tasks/abc017_4 )
    * しゃくとり法とDPの組み合わせ、難しい
* [ABC032 C - 列]( https://atcoder.jp/contests/abc032/tasks/abc032_c )
    * 典型的なしゃくとり法
* [ABC038 C - 単調増加]( https://atcoder.jp/contests/abc038/tasks/abc038_c )
    * 典型的なしゃくとり法
* [ABC124 D - Handstand (400点)]( https://atcoder.jp/contests/abc124/tasks/abc124_d )
* [ABC130 D - Enough Array (500点)]( https://atcoder.jp/contests/abc130/tasks/abc130_d )
    * 典型的なしゃくとり法
* [ABC098 D - Xor Sum 2 (500点)]( https://atcoder.jp/contests/abc098/tasks/arc098_b )
* [ABC102 D - Equal Cut (600点)]( https://atcoder.jp/contests/abc102/tasks/arc100_b )
* [ABC139 F - Engines (600点)]( https://atcoder.jp/contests/abc139/tasks/abc139_f )
* [ABC153 F - Silver Fox vs Monster (600点)]( https://atcoder.jp/contests/abc153/tasks/abc153_f )
* [ABC155 D - Pairs (400点)]( https://atcoder.jp/contests/abc155/tasks/abc155_d )
* [ARC022 B - 細長いお菓子]( https://atcoder.jp/contests/arc022/tasks/arc022_2 )
    * 典型的なしゃくとり法


## いもす法
https://imoz.jp/algorithms/imos_method.html

問題
* [ABC014 C - AtColor]( https://atcoder.jp/contests/abc014/tasks/abc014_3 )
* [ABC035 C - オセロ]( https://atcoder.jp/contests/abc035/tasks/abc035_c )
* [ABC080 D - Recording (400点)]( https://atcoder.jp/contests/abc080/tasks/abc080_d )
* [ABC153 F - Silver Fox vs Monster (600点)]( https://atcoder.jp/contests/abc153/tasks/abc153_f )
* [ARC045 B - ドキドキデート大作戦高橋君]( https://atcoder.jp/contests/arc045/tasks/arc045_b )


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
* [ARC075 E - Meaningful Mean (600点)]( https://atcoder.jp/contests/arc075/tasks/arc075_c )
    * 大事なのは式変形・累積和・BITあたりだが、BITを使うために座標圧縮が必要になる
* [ARC008 D - タコヤキオイシクナール]( https://atcoder.jp/contests/arc008/tasks/arc008_4 )
    * メインテーマはセグツリーだが、座標圧縮の必要性も感じられる問題
* [ABC036 C - 座圧]( https://atcoder.jp/contests/abc036/tasks/abc036_c )
* [ABC113 C - ID (300点)]( https://atcoder.jp/contests/abc113/tasks/abc113_c )
* [ABC168 F - . (Single Dot) (600点)]( https://atcoder.jp/contests/abc168/tasks/abc168_f )
    * 二次元グリッドをそのままでは扱えないので座標圧縮する


## 適切な前計算による高速化
繰り返し行われる処理に関して事前に計算をしていくことで高速化することも大事。
累積和・Combinationの事前計算などもこのようなニュアンスでの高速化。

問題
* [ABC005 D - おいしいたこ焼きの焼き方]( https://atcoder.jp/contests/abc005/tasks/abc005_4 )
* [ABC159 D - Banned K (400点)]( https://atcoder.jp/contests/abc159/tasks/abc159_d )
* [Panasonic2020 E - Three Substrings (500点)]( https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_e )
* 愚直にやると$`O(N^2)`$の比較が必要そうだけど、適切に式変形して整理すると必要な前処理が分かるやつ
    * $`f(i, j) = g(i, j) \Leftrightarrow h(i)=h(j)`$的な
    * [ABC146 E - Rem of Sum is Num (500点)]( https://atcoder.jp/contests/abc146/tasks/abc146_e )
        * $`(S_j - S_i) \% K = j - i ~(j>i) \Leftrightarrow (S_j - j)\%K = (S_i - i)\%K ~(0<j-i<K)`$
    * [ABC166 E - This Message Will Self-Destruct in 5s (500点)]( https://atcoder.jp/contests/abc166/tasks/abc166_e )
        * $`A_j + A_i = \left|j-i \right| (i<j) \Leftrightarrow A_i + i = j - A_j`$
    * [ARC075 E - Meaningful Mean (600点)]( https://atcoder.jp/contests/arc075/tasks/arc075_c )
        * $` \frac{S_j - S_i}{j-i} \geq K ~(j>i) ~\Leftrightarrow~ S_j - Kj \geq S_i -Ki ~(j>i) `$


## よく考えると実は少ない計算量で済むなってやつ
うまく言えん...
問題
* [ARC034 B - 方程式]( https://atcoder.jp/contests/arc034/tasks/arc034_2 )
* [東京海上日動コン2020 C - Lamps (500点)]( https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c )


## イベントソート
問題
* [ABC128 E - Roadwork (500点)]( https://atcoder.jp/contests/abc128/tasks/abc128_e )


## Run-length圧縮
問題
* [ABC019 B - 高橋くんと文字列圧縮]( https://atcoder.jp/contests/abc019/tasks/abc019_2 )


## 繰り返し二乗法・ダブリング
### 冪乗の高速な計算
**python**

* 組み込み関数 [pow(base, exp[, mod])]( https://docs.python.org/ja/3/library/functions.html?highlight=round#pow )
    * 多分繰り返し二乗法で実装されてる[要検証]

問題
* [ABC129 F - Takahashi's Basics in Education and Learning (600点)]( https://atcoder.jp/contests/abc129/tasks/abc129_f )
    * 行列累乗を繰り返し二乗法で高速化
* [ABC156 D - Bouquet (400点)]( https://atcoder.jp/contests/abc156/tasks/abc156_d )
* [ABC167 D - Teleporter (400点)]( https://atcoder.jp/contests/abc167/tasks/abc167_d )
* [ARC020 C - A mod B Problem]( https://atcoder.jp/contests/arc020/tasks/arc020_3 )
    * 一般の整数でのMODが無理なので、ダブリングして計算する的なやつ
    * 本質的にダブリングが必要と感じる問題


# 動的計画法 - Dynamic Programming
[DP]( ./dp.md )


# グラフ
[graph]( ./graph.md )

# 数学
[math]( ./math.md )


# 幾何
[geometry]( ./geometry.md )


# 構築系
https://www.hamayanhamayan.com/entry/2017/08/21/102212
「条件を満たす(数列|グラフ|操作列|その他)を一つ構成せよ」というタイプの問題。
難しい。

* 条件によく注目する
* まず特定の条件で解を構築してみる
* 小さい具体例で構成してみる

といったことをして、解の構成方法の糸口を探すしかない(?)。


問題
* [ABC068 D - Decrease (Contestant ver.) (600点)]( https://atcoder.jp/contests/abc068/tasks/arc079_b )
* [ABC069 D - Grid Coloring (400点)]( https://atcoder.jp/contests/abc069/tasks/arc080_b )
* [ABC081 D - Non-decreasing (600点)]( https://atcoder.jp/contests/abc081/tasks/arc086_b )
* [ABC092 D - Grid Components(500点)]( https://atcoder.jp/contests/abc092/tasks/arc093_b )
* [ABC108 D - All Your Paths are Different Lengths (700点)]( https://atcoder.jp/contests/abc108/tasks/arc102_b )
* [ABC135 E - Golf (500点)]( https://atcoder.jp/contests/abc135/tasks/abc135_e )
* [ABC165 E - Rotation Matching (500点)]( https://atcoder.jp/contests/abc165/tasks/abc165_e )
* [ABC166 F - Three Variables Game (600点)]( https://atcoder.jp/contests/abc166/tasks/abc166_f )
* [AGC038 A - 01 Matrix (300点)]( https://atcoder.jp/contests/agc038/tasks/agc038_a )
* [AGC041 C - Domino Quality (900点)]( https://atcoder.jp/contests/agc041/tasks/agc041_c )
* [日立コン2020 C - ThREE (600点)]( https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_c )
    * 木が二部グラフと捉えられることに着目して考えると良い
* [diverta 2019 procon2 C - Successive Subtraction (500点)]( https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_c )



# ゲーム関係
[game]( ./game.md )


# 文字列系
[string]( ./string.md )


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
* (size of union)に簡単にアクセスできるようになったので、merge techniqueとして、 **サイズが大きなものに小さなものを結合する** ようにする。
    * [データ構造をマージする一般的なテク]( https://topcoder.g.hatena.ne.jp/iwiwi/20131226/1388062106 )
        > 大きさに気をつけて小さい方を大きい方にくっつけるという考え方を応用することで，色々な普通のデータ構造にマージ機能を追加することができます．

という形で実装すること。

```python
class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n

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
* [ABC157 D - Friend Suggestions (400点)]( https://atcoder.jp/contests/abc157/tasks/abc157_d )
* [ABC168 F - . (Single Dot) (600点)]( https://atcoder.jp/contests/abc168/tasks/abc168_f )
    * 二次元グリッドをそのままでは扱えないので座標圧縮する
    * セル同士が連結かどうかの判定にUFを使う

* [ARC056 B - 駐車場]( https://atcoder.jp/contests/arc056/tasks/arc056_b )
    * Editorialはdijkstra風なやつだが、頂点が大きい方から見てUnionFind使うことでも解ける


## Segment Tree
長さ$`N`$の列に対して、

* ある区間全体に対する演算
* ある点の値の変更

を$`O(\log N)`$で可能なデータ構造。[モノイド]( https://ja.wikipedia.org/wiki/%E3%83%A2%E3%83%8E%E3%82%A4%E3%83%89 )と関わりが深く、面白い。
構築は$`O(N)`$でできる。

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
* 動作確認済み
    * RMQ : http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4223494#1
    * RSQ : http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4223496#1
```python
class SegmentTree0():
    """
    0-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, op_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n - 1)  # binary tree (0-indexed)
        self.ele_id = ele_id  # identity element
        self.op_func = op_func  # binary operation of monoid

    def __getitem__(self, i):
        return self.data[i + self.n - 1]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n - 1] = data_init[i]  # set data in leaf
        for i in range(self.n - 2, -1, -1):
            self.data[i] = self.op_func(self.data[2 * i + 1],
                                        self.data[2 * i + 2])

    def update(self, i, x):
        # change i-th element to x (i : 0-indexed)
        i += self.n - 1
        self.data[i] = x
        while i > 0:
            i = (i - 1) // 2  # go to parenet-node
            self.data[i] = self.op_func(self.data[2 * i + 1],
                                        self.data[2 * i + 2])

    def query(self, a, b):
        # query for interval [a, b) (a, b : 0-indexed)
        return self.query_(a, b, 0, 0, self.n)

    def query_(self, a, b, k, l, r):
        if r <= a or b <= l:
            # [a, b) and [l, r) have no intersection
            return self.ele_id
        if a <= l and r <= b:
            # [a, b) includes [l, r)
            return self.data[k]
        else:
            # [a, b) and [l, r) have some overlap
            child_l = self.query_(a, b, 2 * k + 1, l, (l + r) // 2)
            child_r = self.query_(a, b, 2 * k + 2, (l + r) // 2, r)
            return self.op_func(child_l, child_r)
```

### 抽象化セグメントツリー(1-indexed)
queryを再帰ではなくループで書いた1-indexed Segment Tree 。
* 動作確認済み
    * RMQ : http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4223486#1
    * RSQ : http://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=4223480#1
```python
class SegmentTree1():
    """
    1-indexed Segment Tree
    """
    def __init__(self, n_, ele_id, op_func):
        self.n = 1 << (n_ - 1).bit_length()  # size
        self.data = [ele_id] * (2 * self.n)  # binary tree (1-indexed)
        self.ele_id = ele_id  # identity element
        self.op_func = op_func  # binary operation of monoid

    def __getitem__(self, i):
        return self.data[i + self.n]

    def build(self, data_init):
        for i in range(len(data_init)):
            self.data[i + self.n] = data_init[i]  # set data in leaf
        for i in reversed(range(self.n)):
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def update(self, i, x):
        # change i-th element to x (i : 0-indexed)
        i += self.n
        self.data[i] = x
        while i > 1:
            i = i >> 1  # go to parenet-node
            self.data[i] = self.op_func(self.data[2 * i], self.data[2 * i + 1])

    def query(self, l, r):
        # query for interval [l, r) (l, r : 0-indexed)
        l += self.n
        r += self.n
        ret = self.ele_id
        while l < r:
            if l & 1:  # right child
                ret = self.op_func(ret, self.data[l])
                l += 1
            if r & 1:  # right child
                r -= 1
                ret = self.op_func(ret, self.data[r])
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
* [ABC038 D - プレゼント]( https://atcoder.jp/contests/abc038/tasks/abc038_d )
    * DPの漸化式の更新にRangeMaximumQueryを使う
*  [ABC125 C - GCD on Blackboard (300点)]( https://atcoder.jp/contests/abc125/tasks/abc125_c )
    * Range GCD Queryを解く問題としてSegmentTreeを使うこともできる。
* [第２回日経コン D - Shortest Path on a Line (600点)]( https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_d )
    * DPの漸化式更新のためにRMQする
* [ABC146 F - Sugoroku (600点)]( https://atcoder.jp/contests/abc146/tasks/abc146_f )
    * DPの漸化式更新のためにRMQする
* [ABC157 E - Simple String Queries (500点)]( https://atcoder.jp/contests/abc157/tasks/abc157_e )
    * BitSet + SegmentTree
    * 26個のSegTree( or  BIT)でRSQしてもOK
* [ARC008 D - タコヤキオイシクナール]( https://atcoder.jp/contests/arc008/tasks/arc008_4 )
    * 座標圧縮 + 関数の合成についてのsegtree
* [ARC026 C - 蛍光灯]( https://atcoder.jp/contests/arc026/tasks/arc026_3 )
    * DPの更新にSegmentTreeが必要




## BIT (fenwick tree)
> Fenwick Tree とも呼ばれる。数列に対し, ある要素に値を加える操作と, 区間和を求める操作をそれぞれ対数時間で行うことが出来るデータ構造。セグメント木や平衡二分探索木の機能を制限したものであるが, 実装が非常に単純で定数倍も軽いなどの利点がある。

BITはセグ木を制限したものなので、応用範囲は狭いが、実装が簡単で定数倍が軽いのが特徴らしい。
なので当然BITの問題はセグ木でも出来る。

$`v_1, v_2, \cdots, v_N`$という数列を考えた時に、

* 前から$`m`$項分の和の計算: $`~ {\rm sum}(m) = \sum_{i=1}^{m} v_i`$
    * 特に$`{\rm sum}(0) = 0`$
* 第$`i`$項に加算: $`~ v_i += x`$

を$`O(\log N)`$で可能なデータ構造。
また特に、常に$`v_i \geq 0`$を満たす場合には

* 二分探索: $`~ {\rm sum}({\rm index}) \geq x`$を満たす最小のindexを見つける

も$`O(\log N)`$で可能。

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

値の範囲($`1 \sim N`$)が分かっている場合の`std::set`ライクな使い方ができる。具体的には
* $`v_i=~`$(数$`i`$が集合に入っていれば1、そうでなければ0)

として、この数列にBITを適用することで、

* 集合への要素の追加・削除 (`add`)
* 指定された要素は何番目に小さいか (`sum`)
* $`x`$番目に小さい要素は何か (`bisect_left`)

を全て$`O(\log N)`$で出来る。
（セグ木でも出来るが、`bisect_left`が遅くなる or 実装が面倒）

Reference
* https://ei1333.github.io/luzhiled/snippets/structure/binary-indexed-tree.html
* http://hos.ac/slides/20140319_bit.pdf
* https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree
* https://ikatakos.com/pot/programming_algorithm/data_structure/binary_indexed_tree

### 区間加算の対応
頑張るとできる


問題
* [AOJ DSL_2_B Range Sum Query (RSQ)]( http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B )
* 転倒数([参考]( https://qiita.com/wisteria0410ss/items/296e0daa9e967ca71ed6 ))関連
    * 定義
        * 長さ$`n`$の数列$`\{ a_n \}`$について、$`0 \leq i < j < n`$かつ$`a_i > a_j`$なる$`(i, j)`$のペア数
        * BITを使いながら前から見ていき($`j`$を0から$`n`$まで動かすイメージ)、その時点での$`a_j`$より大きい数を数えればいいだけ
    * [ABC107 D - Median of Medians (700点)]( https://atcoder.jp/contests/abc107/tasks/arc101_b )
        * 二分探索のcheck関数のところで転倒数的なものを求める
    * [ARC088 E - Papple Sort (800点)]( https://atcoder.jp/contests/arc088/tasks/arc088_c )
* [ABC136 F - Enclosed Points (600点)]( https://atcoder.jp/contests/abc136/tasks/abc136_f )
* [ABC153 F - Silver Fox vs Monster (600点)]( https://atcoder.jp/contests/abc153/tasks/abc153_f )
    * 区間加算に対応する必要あり
    * https://drken1215.hatenablog.com/entry/2020/01/26/234000
* [ARC075 E - Meaningful Mean (600点)]( https://atcoder.jp/contests/arc075/tasks/arc075_c )
* std::setライクな使い方をする問題
    * [AGC005 B - Minimum Sum (400点)]( https://atcoder.jp/contests/agc005/tasks/agc005_b )
    * [ARC033 C - データ構造]( https://atcoder.jp/contests/arc033/tasks/arc033_3 )
    * [ABC140 E - Second Sum (500点)]( https://atcoder.jp/contests/abc140/tasks/abc140_e )
    * [ABC157 E - Simple String Queries (500点)]( https://atcoder.jp/contests/abc157/tasks/abc157_e )



# 何とも言えないけど競プロっぽいやつ
うまく言語化できないけど、競プロっぽい問題はたくさんあるし、慣れないと解けない。
ちょっとずつこれらのまとめもしていきたい。

問題
* その他
    * [AGC034 A - Kenken Race (400点)]( https://atcoder.jp/contests/agc034/tasks/agc034_a )
    * [AGC034 B - ABC (600点)]( https://atcoder.jp/contests/agc034/tasks/agc034_b )
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
  input = lambda: sys.stdin.readline().rstrip() # sys.stdin.readlineは改行文字を含んでしまうので注意
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
* [数え上げテクニック集 by DEGwer]( https://drive.google.com/file/d/1WC7Y2Ni-8elttUgorfbix9tO1fvYN3g3/view )

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

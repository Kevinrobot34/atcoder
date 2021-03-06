# LIS
**LIS = Longest Increasing Subsequenc, 最長増加部分列**

## Setup
* 数列`{a_i | i = 0,2, ..., N-1}`が与えられるのでLISの長さを求めよ
* 例
  - `a = [4, 2, 3, 1, 5]` の時、`[2,3,5]`がLISで答えは3

## 考察
DPする。発想としては「`a[0]`から`a[i]`の中から作った長さ`j`の増加部分列が複数ある時、最終要素が小さいほど有利」なので、それを保持する配列`dp[i][j]`を用意する。\
`dp[i][j] = (a[0]からa[i]まで見て作った長さj+1の増加部分列の最終要素の最小値)`\
`dp[n-1][j]`を計算し、それが最大となるjが探せばLISの長さが求まることになる。

* 初期化
  - `dp[0][0] = a[0]`
  - その他全ての`j`に対して`dp[0][j] = inf`
* 更新式
  - `i`まで`dp[i][j]`が求まっているとして、`dp[i+1][j]`を各`j`に対して求める
  - `j=0`の時か`a[i+1] > dp[i][j-1]` (=`a[i+1]`を`j`個目の増加部分列の要素として追加できる)の時、`dp[i+1][j] = min(a[i+1], dp[i][j])`と更新していけば良い。
  - pythonでのざっくりイメージ
    ```python
    for i in range(1, n):
        for j in range(n):
            if j == 0 or a[i] > dp[i-1][j-1]:
                dp[i][j] = min(dp[i][j], a[i])
    ```
  - 実は固定した`i`に対して`{dp[i][j] | j=0, 1, 2, ...}`は単調増加な列になる。（以下の実験参照。）
    - この事実を踏まえて上記のプログラムをよく見ると`a[i]`を用いて配列`dp`を更新するのはただ一度のみであることが分かる。
    - これを二分探索で求めればO(NlogN)だよねっていうのが蟻本のアルゴリズム。
    - これらを具体例を挙げて考えてみよう。

---
**実験１**

| j          | 0      | 1   | 2   | 3   | ... |
| ---------- | ------ | --- | --- | --- | --- |
| `dp[0][j]` | `a[0]` | inf | inf | inf | ... |

`a[1]`を追加することを考える。
* `a[1] <= a[0]` の時

  | j          | 0      | 1   | 2   | 3   | ... |
  | ---------- | ------ | --- | --- | --- | --- |
  | `dp[0][j]` | `a[0]` | inf | inf | inf | ... |
  | `dp[1][j]` | `a[1]` | inf | inf | inf | ... |

* `a[0] < a[1]` の時

  | j          | 0      | 1      | 2   | 3   | ... |
  | ---------- | ------ | ------ | --- | --- | --- |
  | `dp[0][j]` | `a[0]` | inf    | inf | inf | ... |
  | `dp[1][j]` | `a[0]` | `a[1]` | inf | inf | ... |

配列`dp[i][j]`は各`i`に対して単調増加なまま。

---

**実験２**

| j          | 0   | 1   | 2   | 3   | ... |
| ---------- | --- | --- | --- | --- | --- |
| `dp[i][j]` | a   | b   | inf | inf | ... |

(ただし a < b)

上記のような状況で、`a[i+1] = c`を追加することを考える。

* `c <= a < b` の時

  | j            | 0   | 1   | 2   | 3   | ... |
  | ------------ | --- | --- | --- | --- | --- |
  | `dp[i][j]`   | a   | b   | inf | inf | ... |
  | `dp[i+1][j]` | c   | b   | inf | inf | ... |


* `a < c <= b` の時

  | j            | 0   | 1   | 2   | 3   | ... |
  | ------------ | --- | --- | --- | --- | --- |
  | `dp[i][j]`   | a   | b   | inf | inf | ... |
  | `dp[i+1][j]` | a   | c   | inf | inf | ... |

* `a < b < c` の時

  | j            | 0   | 1   | 2   | 3   | ... |
  | ------------ | --- | --- | --- | --- | --- |
  | `dp[i][j]`   | a   | b   | inf | inf | ... |
  | `dp[i+1][j]` | a   | b   | c   | inf | ... |

どの場合もdpは単調増加なまま

---

以上の実験から、`dp[i][j]`という二次元配列を用意して`a[i]`という要素を追加して更新をしようとしても**ただ一箇所しか更新されない**ことが分かる。更に`i`に対して`{dp[i][j] | j=0, 1, 2, ...}`は常に**単調増加な列**になることも分かる。

よって結局、
* `dp[j] = (長さj+1の増加部分列の最終要素の最小値)` を用意
* 初めはすべての要素をinfで初期化しておく
* 更新について
  - `j=0`でかつ`a[i] < dp[0]`の時、`dp[0] = a[i]`
  - `j>0`でかつ`dp[j-1] < a[i] <= dp[j]`の時、`dp[j] = a[i]`
* dp[j]は更新を経ても単調増加なまま
* dp[j]は単調増加なので、更新はただ一つのjに対してのみ起こる
  - lower_bound(bisect_left)を用いて更新される場所を二分探索すれば良い

pythonでの実装イメージ
```python
from bisect import bisect_left
dp = [a[0]]
for i in range(1, n):
    if a[i] > dp[-1]:
        dp.append(a[i])
    else:
        idx = bisect_left(dp, a[i])
        dp[idx] = a[i]
ans = len(dp)
```
```python
from bisect import bisect_left
INF = 10**8
dp = [INF] * n
for i in range(n):
    idx = bisect_left(dp, w[i])
    dp[idx] = w[i]
ans = bisect_left(dp, INF)
```


こうして蟻本に載っているO(NlogN)のアルゴリズムができた。


## Reference
LISの関連する問題
* [ABC006 D - トランプ挿入ソート]( https://atcoder.jp/contests/abc006/tasks/abc006_4 )
* [ABC134 E - Sequence Decomposing (500点)]( https://atcoder.jp/contests/abc134/tasks/abc134_e )


解説記事
* https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
* https://www.slideshare.net/chokudai/abc006

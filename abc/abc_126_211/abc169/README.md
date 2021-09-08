# ABC169
* https://atcoder.jp/contests/abc169


## C - Multiplication 3 (300点)
* keywords
  - 数値誤差、Decimal
* 解法
  - 誤差が怖いので、`.`を無くしてから`a`と`b`を読み込み`a*b//100`
* comments
  - floatはなるべく避けよう
  - maspyさんが実験してくれてる [参考ツイート]( https://twitter.com/maspy_stars/status/1267089335150493699 )
    - ```python
      x = 2.51
      y = x * 100
      print(x, y, int(y), int(y + 0.5))
      2.51 250.99999999999997 250 251
      ```
    - Pythonには[Decimal]( https://docs.python.org/ja/3/library/decimal.html )があるよ


## D - Div Game (400点)
* keyword
  - 素因数分解
* 解法
  - `N`をはじめに素因数分解する
  - 素因数ごとに`z`をいくつ構成できるか考える
    - 素因数`p`の指数を`m`とする
    - `a_k = 1+2+ ... + k`とする
    - `a_k <= m < a_{k+1}`なる`k`個だけ相異なるzを構成できることがわかる
    - 上記`k`を各素因数に対して足し合わせたものが答え
  - `n=1`のコーナーケースに注意


## E - Count Median (500点)
* keyword
  - median(中央値)、連続性
* 解法
  - 全てを`a_i`で構成した数列を`X`とし、そのmedianを`X_med`とする
  - 全てを`b_i`で構成した数列を`Y`とし、そのmedianを`Y_med`とする
    - `X_med <= Y_med`となる
  - `n`の偶奇で場合わけ
    - `n`が偶数の時、medianは`X_med`から`Y_med`までの半整数全てをとりうる
    - `n`が奇数の時、medianは`X_med`から`Y_med`までの整数すべてをとりうる
  - 上記を数えるだけ
* comment
  - 証明ができない...
    - editorial見ると、ほぼ同じことを考えていた



## F - Knapsack for All Subsets (600点)
* keywords
  - ナップザック問題、部分和問題
* 解法
  - 部分和問題を解くためのDPをうまく変更して解けないかなぁという気持ち
    - `dp[i][j] = i番目まで見て和がjとなるような場合の数`
      - 初期値
        - `dp[0][0] = 1`
      - 漸化式
        - `dp[i + 1][j] = dp[i][j] + dp[i][j - ai]` when `j-ai>=0`
        - `dp[i + 1][j] = dp[i][j]` otherwise
      - 答え
        - `dp[n][s]`
      - 計算量
        - `O(ns)`
  - ある部分集合 `T' = {x_1, ..., x_k}`が、`a_{x_j}`の和を`S`に出来たとする
    - これが`f(T)`で何回数えられるか？という視点で考える
    - `n-k`個の残りの要素を含む・含まないの自由度があるので、`2^{n-k}`通りの`T`に`T'`は部分集合として含む
  - 上記を踏まえるとただの部分和問題を以下のように変更できる
    - `dp[i][j] = i番目まで見て和がjとなるような場合の数`
      - 初期値
        - `dp[0][0] = 1`
      - 漸化式
        - `dp[i + 1][j] = (dp[i][j] * 2 + dp[i][j - ai]) % MOD` when `j-ai>=0`
        - `dp[i + 1][j] = dp[i][j] * 2 % MOD` otherwise
        - `dp[i][j]`による寄与は`a_i`を使わなかった時なので、２倍して数えれば良い
      - 答え
        - `dp[n][s]`
      - 計算量
        - `O(ns)`

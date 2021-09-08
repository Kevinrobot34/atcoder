# ABC159
* https://atcoder.jp/contests/abc000


## C - Maximum Volume (300点)
* 数学


## D - Banned K (400点)
* 事前計算が必要な算数


## E - Dividing Chocolate (500点)
* bit全探索
* なんかスマートにかけない


## F - Knapsack for All Segments (600点)
* `f(L, R)`を求めるだけの問題を考える
  - 数列`{A[i] | i=L, ..., R}`に対して部分和が`S`となるような部分列の数
  - DP
    - `dp[i][j] = (i番目まで見て和がjとなる場合の数)`
    - 漸化式
      - `dp[0][0] = 1`
      - `dp[i+1][j+a[i]] += dp[i][j]`
      - `dp[i+1][j] += dp[i][j]`

# EDPC
* https://atcoder.jp/contests/dp/tasks/dp_a


## A - Frog 1
* `dp[i] = (足場iにたどり着いた時点でのコストの最小値)`
  - 初期値
    - `dp[0] = 0`
    - `dp[i] = 0 (i > 0)`
  - 漸化式
    - 書き方その１
      - `dp[i] = min(dp[i-1] + abs(h[i]+h[i-1]), dp[i-2] + abs(h[i]+h[i-2]))`
    - 書き方その２
  - 計算量
    - `O(N)`
  - 答え
    - `dp[n - 1]`


## B - Frog 2
* `dp[i] = (足場iにたどり着いた時点でのコストの最小値)`
  - 初期値
    - `dp[0] = 0`
    - `dp[i] = 0 (i > 0)`
  - 漸化式
    - `dp[i] = min(dp[j] + abs(h[i]-h[j]) | j = i-k, ..., i-2, i-1)`
  - 計算量
    - `O(NK)`
  - 答え
    - `dp[n - 1]`



## C - Vacation
* `dp[i][j] = (i日にjをするような場合の幸福度の最大値)`
  - 初期値
  - 漸化式
  - 計算量
    - `O(N)`
  - 答え

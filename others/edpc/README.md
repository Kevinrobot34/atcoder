# EDPC
* https://atcoder.jp/contests/dp/tasks/dp_a


## A - Frog 1
* `dp[i] = (足場iにたどり着いた時点でのコストの最小値)`
  - 初期値
    - `dp[0] = 0`
    - `dp[i] = INF (i > 0)`
  - 漸化式
      - `i >= 2`に対して、
        ```python
        dp[i] = min(dp[i - 1] + abs(h[i] + h[i - 1]),
                    dp[i - 2] + abs(h[i] + h[i - 2]))
        ```
  - 計算量
    - `O(N)`
  - 答え
    - `dp[n - 1]`


## B - Frog 2
* `dp[i] = (足場iにたどり着いた時点でのコストの最小値)`
  - 初期値
    - `dp[0] = 0`
    - `dp[i] = INF (i > 0)`
  - 漸化式
    - `dp[i] = min(dp[j] + abs(h[i]-h[j]) | j = i-k, ..., i-2, i-1)`
  - 計算量
    - `O(NK)`
  - 答え
    - `dp[n - 1]`



## C - Vacation
* `dp[i][j] = (i日にjをするような場合の幸福度の最大値)`
  - 初期値
    - `dp[i][j] = 0`
  - 漸化式
    - ```python
      dp[i + 1][0] = max(dp[i][1], dp[i][2]) + happy[i][0]
      dp[i + 1][1] = max(dp[i][2], dp[i][0]) + happy[i][1]
      dp[i + 1][2] = max(dp[i][0], dp[i][1]) + happy[i][2]
      ```
  - 計算量
    - `O(N)`
  - 答え
    - `max(dp[n])`


## D - Knapsack 1
* 典型的なKnapsack問題
* `dp[i][j] = (iまでの品物で重さの総和がj以下であるように選んだ際の価値の総和の最大値)`
  - 初期化
    - `dp[i][j] = 0`
  - 漸化式
    - `j >= wi`の時
      - `dp[i+1][j] = max(dp[i][j], dp[i][j-wi] + vi)`
    - そうでない時
      - `dp[i+1][j] = dp[i][j]`
  - 計算量
    - `O(NW)`
  - 答え
    - `dp[n][w]`


## E - Knapsack 2
* 重さが大きくなりうるタイプのKnapsack問題
* `dp[i][j] = (iまでの品物で価値の総和がjであるように選んだ際の重さの総和の最小値)`
  - 初期化
    - `dp[0][0] = 0`
    - `dp[i][j] = INF (otherwise)`
  - 漸化式
    - `j >= wi`の時
      - `dp[i+1][j] = max(dp[i][j], dp[i][j-vi] + wi)`
    - そうでない時
      - `dp[i+1][j] = dp[i][j]`
  - 計算量
    - `V' = 10**5`として`O(NV')`
  - 答え
    - `dp[n]`内の`dp[n][j] <= w`を満たす最大の`j`


## F - LCS
* Longest Common Substring
  - 最長共通部分文字列


## I - Coins
* 確率DP
* `dp[i][j] = (コインiまで見て、表がj枚出ている確率)`

# ARC026
* https://atcoder.jp/contests/arc026


## C - 蛍光灯
* keywords
  - DP、SegmentTree、RMQ
* 解法
  - 蛍光灯情報は`l_i`でソートしておく
  - DP
    - `dp[i] = (西端からiメートルのところまでを照らすのに必要な最小の費用)`
    - 初期化
      - `dp[0] = 0`
      - `dp[i] = INF` (otherwise)
    - 漸化式
      - `dp[r[i]] = min(dp[r[i]], min(dp[l[i]:r[i]+1])+c[i])`
  - 直接`dp`をセグメントツリーに載せちゃうと楽

# ABC185
* https://atcoder.jp/contests/abc185


## C - Duodecim Ferra (300点)
* keywords
  - Combination、数学
* 解法
  - `comb(l-1, 11)`なだけ
  - C++などの場合はオーバーフローに注意が必要
    - 順次割りながら計算する
    - パスカルの三角形なDPで計算する


## D - Stamp (400点)
* keywords
  - 貪欲
* 解法
  - kとしてはなるべく大きい方が良いことがちょっと考えるとわかる
    - ただ、連続する白マスの長さより大きくは取れない
    - よって `k = min({連続する白マスの長さ})`
  - あとは「連続する白マスの長さ」をkで割って切り上げた数値の和が答え


## E - Sequence Matching (500点)
* keywords
  - DP、編集距離
* 解法1
  - `dp[i][j] = (a[:i]とb[:j]だった場合の答え)`
    - 初期値
      - 片方が空文字列の時、全削除しかないので初期値は以下
      - `dp[i][0] = i`
      - `dp[0][j] = j`
    - `dp[i+1][j+1] = min(dp[i+1][j]+1, dp[i][j+1]+1, dp[i][j]+int(a[i]!=b[j]))`
      - LCSに近い感じ


## F - Range Xor Query (600点)
* keywords
  - セグメントツリー、BIT、XOR
* 解法
  - 演算:Xor、単位元:0をセグメントツリーやBITに載せるだけ

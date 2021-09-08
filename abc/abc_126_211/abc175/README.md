# ABC175
* https://atcoder.jp/contests/abc175


## C - Walking Takahashi (300点)
* keyword
  - シミュレーション
* 解法
  - `abs(x) > k * d`の場合は、`abs(x) - k * d`が答え
  - そうでない場合についてはちょっと面倒
    - 移動の概要
      - `abs(x) % d`まで、`abs(x) // d`回で移動する
      - その後は`abs(x) % d`と`d - abs(x) % d`を交互に移る
    - 後者の部分について、`k - abs(x) // d`の偶奇で場合わけするだけ


## D - Moving Piece (400点)
* keyword
  - 順列、置換、巡回置換
* 解法
  - 順列(置換)はいくつかのサイクルの部分に分解できる
    - 数学的には「任意の置換は巡回置換の積で表せる」ということ
  - それぞれの巡回部分についてシミュレーションして、最大のスコアを計算する
    - `K`が大きく、また一周して正の点数が取れる場合もあることに注意
  - `O(N^2)`
* 解法2
  - ダブリングでもよいかも



## E - Picking Goods (500点)
* keyword
  - DP
* 解法
  - DPする
    - `dp[i][j][m] = (i行j列で、その行でm個のitemを取得時の価値の最大値)`
  - `O(RC)`
* comment
  - Pythonという縛りプレイは辛い


## F - Making Palindrome (600点)
* keyword
  - 回文
* 解法

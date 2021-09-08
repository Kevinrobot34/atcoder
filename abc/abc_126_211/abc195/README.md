# ABC195
* https://atcoder.jp/contests/abc195
* 参加記 :


## B - Many Oranges (200点)
* keywords
  - 全探索
* 解法1
  - 選んだみかんの個数を全探索
* 解法2
  - `w`は1000倍しておく
  - 最小値の候補：`w/b`の切り上げ` =: x`
  - 最大値の候補：`w/a`の切り捨て` =: y`
  - 整数に丸めなければ `w / b <= w / a` だが、入力例３のような場合は`x > y`となる
    - この時が`UNSATISFIABLE`


## C - Comma (300点)
* keywords
* 解法
  - `10**(3*i)`のカンマは`10**(3*i)`以上の全ての数に一つずつある
  - これを数えて足すだけ


## D - Shipping Center (400点)
* keywords
  - 貪欲法
* 解法1
* 解法2
  - フロー（最小費用流）で解けるらしい


## E - Lucky 7 Battle (500点)
* keywords
  - ゲーム系
* 解法
  - 後ろから考える
  - `dp[i][j] = (iラウンド目までで余りがjの時、Trueなら高橋くんが、Falseなら青木くんが勝確)`
    - 初期値
      - `dp[n][0] = True`
      - `dp[n][i] = False (i=1,2,3,4,5,6)`
    - 漸化式
      - ゲームは完全二分木になっているので、二つ先でどちらも0or1かを確認する
    - 答え
      - `dp[0][0]`がTrueなら高橋君の、Falseなら青木君の勝確
    - 計算量`O(N)`


## F - Coprime Present (600点)
* keywords
  - bitDP
* 解法
  - 72以下の素数は20個
  - forの順番注意

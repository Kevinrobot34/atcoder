# Chokudai SpeedRun 001
* https://atcoder.jp/contests/chokudai_S001

全ての問題が長さ`N`の整数列`A`が与えられる形式のコンテスト。
AtCoderの負荷チェックとして出題されたようだが、典型問題が並んでいて勉強になる。


## A - 最大値 (100点)
* 解法
  - [max]( https://docs.python.org/ja/3/library/functions.html#max )


## B - 和 (100点)
* 解法
  - [sum]( https://docs.python.org/ja/3/library/functions.html#sum )


## C - カンマ区切り (200点)
* 解法
  - [print]( https://docs.python.org/ja/3/library/functions.html#print )の`sep`を`,`にする


## D - ソート (200点)
* 解法
  - [list.sort]( https://docs.python.org/ja/3/library/stdtypes.html#list.sort )


## E - 1は何番目？ (200点)
* 解法
  - [list.index]( https://docs.python.org/ja/3/tutorial/datastructures.html )
    - > リスト中で x と等しい値を持つ最初の要素の位置をゼロから始まる添字で返します。


## F - 見える数 (300点)
* 解法
  - 前から累積max取りながら各数を比較する


## G - あまり (300点)
* 解法1
  - `ai`ごとに毎回MODを取りながら少しずつ計算する
* 解法2
  - 数列を直接連結してMODを取っちゃう


## H - LIS (400点)
* keywords
  - LIS、DP
* 解法
  - `dp[i] = (長さ(i+1)の増加部分列での末尾の項がとりうる最小値)`
  - `O(NlogN)`


## I - 和がNの区間 (400点)
* keywords
  - 二分探索、しゃくとり法
* 解法1
  - 累積和とって、その要素毎に`+N`された要素がないか二分探索
  - `O(NlogN)`
* 解法2
  - しゃくとり
  - `O(N)`


## J - 転倒数 (400点)
* keywords
  - 転倒数、バブルソート、BIT
* 解法
  - 数列`A`を前から見ていき、BITでそれまでに各数字がいくつずつ存在するかを管理しておく


## K - 辞書順で何番目？ (500点)
* keywords
  - 辞書順、BIT


## L - N回スワップ (500点)


## References
* https://nemupm.com/blog/2019/03/03/chokudai-speed-run-001/
* https://eromog.hatenablog.com/entry/2019/07/26/025035

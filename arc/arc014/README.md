# ARC014
* https://atcoder.jp/contests/arc014


## C - 魂の還る場所
* keywords
* 解法
  - RGBそれぞれの個数を見た時、奇数であれば１個残り得て、偶数であれば全て消しうる
    - よって `sum(v % 2 for v in Counter(s).values())` が自明な下界
  - これを実現できることを、途中の状態を具体的に構成して示すことができる


## D - grepマスター

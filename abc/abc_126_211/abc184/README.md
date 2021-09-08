# ABC184
* https://atcoder.jp/contests/abc184


## C - Super Ryuma (300点)
* keywords
  - 移動方法、パリティ、コーナーケース
* 解法


## D - increment of coins (400点)
* keywords
  - DP、確率DP
* 解法
  - `f(x,y,z) = ((x,y,z)の時の求める期待値)`
    - 初期化
      - どれか一つでも100なら0
    - 漸化式
      - `(x,y,z)`の状態は`(x+1)/(x+y+z)`の確率で`(x+1,y,z)`になる
        - よってこの確率で`f(x+1,y,z) + 1`回でどれかが100枚になる
      - `f(x,y,z) = [x*(f(x+1,y,z)+1) + y*(f(x,y+1,z)+1) + z*(f(x,y,z+1)+1)] / (x+y+z)`
  - メモ化再帰して解く


## E -  (500点)
* keywords
* 解法


## F - Programming Contest (600点)
* keywords
  - 部分和問題、半分全列挙
* 解法
  - `O(N * 2^(N/2))` の半分全列挙で解ける

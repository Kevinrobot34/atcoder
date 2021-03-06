# ABC187
* https://atcoder.jp/contests/abc187
* [ABC187参加記]( https://medium.com/@kevinrobot34/abc187-c2fb559ad2d8 )


## C - 1-SAT (300点)
* keywords
  - set
* 解法
  - `!`から始まる文字列集合と、そうでない文字列集合について、先頭の`!`を除き一致するものがあるか調べれば良い
  - 実装方法は何でもいいけどset使う感じ


## D - Choose Me (400点)
* keywords
  - 貪欲法
* 解法
  - 青木氏に対する高橋氏の相対的な得票数を考えると見通しが良くなる
    - 青木氏への投票は負、高橋氏への投票は正として得票数を数えると言うこと
    - このとき、得票数が0より大きくなることが必要
  - まず全ての街で演説しなかったとすると、 `-sum(bi)`の得票数があることになる
  - ある街で演説することにすると、合計で`2*ai + bi`得票数が増えることになる
  - よって`2*ai + bi`が大きい町から順に演説をして、得票数が0を超えるまでこれを続ければ良い
* 類題
  - [CODE FESTIVAL 2015 予選A C - 8月31日]( https://atcoder.jp/contests/code-festival-2015-quala/tasks/codefestival_2015_qualA_c )


## E - Through Path (500点)
* keywords
  - グラフ、木、imos
* 解法
  - 木の上でimos法的なことをする
* 類題
  - [ABC138 D - Ki (400点)]( https://atcoder.jp/contests/abc138/tasks/abc138_d )


## F - Close Group (600点)
* keywords
  - DP、`O(3^N)`
* 解法1
  - memo化再帰でDPする
  - PyPyだと重くてしんどい、枝刈りが必要
* 解法2 (editorial)
  - ループで上手に書く
* 類題
  - [EDPC U - Grouping]( https://atcoder.jp/contests/dp/tasks/dp_u )

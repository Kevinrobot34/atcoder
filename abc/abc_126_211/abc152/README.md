# ABC000
* https://atcoder.jp/contests/abc000


## C - Low Elements (300点)



## D - Handstand 2 (400点)



## E - Flatten (500点)
* keywords
  - LCM、素因数分解
* 解法1(editorial)
  - LCMを直接計算すると大きな数になりうる
  - 素因数分解した結果を持っておき、それを利用して素因数分解された形でLCMを求める
  - 上記結果をMODを取りながら計算
  - 逆元も計算しておいて、割り算
* 解法2
  - PythonだとLCMを何も考えずに計算してもOK
* 解法3
  - 素因数分解を高速化する


## F - Tree and Constraints (600点)
* keywords
  - 包除原理、木、LCA、累積和、pathのencoding
* 解法1 (editorial)
  - 事前にLCAを全て計算しておく
  - 包除原理
    - 注目している条件のパスの和集合を求めるために木上の累積和(imos法)的なことをする
  - `f_tle.py`
* 解法2
  - pathを整数でencoding
  - https://drken1215.hatenablog.com/entry/2020/01/26/164200
  - `f.py`

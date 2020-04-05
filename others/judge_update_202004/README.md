# Judge System Update Test Contest 202004
* https://atcoder.jp/contests/judge-update-202004


## C - Numbering Blocks (300点)
* 解法１
  - `O(N!)`通りの数字の書き込み方を列挙し、条件を満たす数を数える
* 解法２
  - ヤング図形的な？


## D - Calculating GCD (400点)
* 解法１
  - まず`A[i]`から`A_gcd[i] = gcd(a[:i])`なる累積gcdを取る
    - `O(NlogA)`
    - `A_gcd`は単調減少
  - 次に、各`S[i]`に対して、`S[i]`とgcdをとって1になるindexを二分探索する
